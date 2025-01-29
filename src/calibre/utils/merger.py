import ast
import astunparse
import sys
import logging
import pdb
# At the top of merger.py
import os


if os.environ.get("DEBUG_MODE"):
    import time
    import debugpy
    debugpy.listen(5678)
    print("⏳ Debugger ready at port 5678 - Attach when needed")
    
    # Silent wait without spam
    debugpy.wait_for_client()
    
    print("🔌 Debugger attached at", time.strftime("%Y-%m-%d %H:%M:%S"))
    debugpy.breakpoint()


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='stubgen-merger.log',  # Separate merger-specific log
    filemode='a'  # Append mode
)

class StubMerger(ast.NodeTransformer):
    def __init__(self, official_ast):
        self.official_ast = official_ast

    def visit_ClassDef(self, node):
        logging.info(f"Processing class: {node.name}")
        print(f"\nMerging class: {node.name}")
        official_class = next(
            (n for n in self.official_ast.body 
             if isinstance(n, ast.ClassDef) and n.name == node.name),
            None
        )
        if node.name == "MatchFlags":
            pdb.set_trace()
        if official_class:
            logging.info(f"Found official class: {node.name}")
            print(f"Found official class: {node.name}")  # Debug
            calibre_members = set()
            # Extract Calibre members (including nested attributes)
            for m in node.body:
                if isinstance(m, (ast.FunctionDef, ast.ClassDef)):
                    calibre_members.add(m.name)
                elif isinstance(m, ast.AnnAssign):
                    if isinstance(m.target, ast.Name):
                        calibre_members.add(m.target.id)
                    elif isinstance(m.target, ast.Attribute):
                        calibre_members.add(m.target.attr)
                elif isinstance(m, ast.Assign):
                    for target in m.targets:
                        if isinstance(target, ast.Name):
                            calibre_members.add(target.id)
                        elif isinstance(target, ast.Attribute):
                            calibre_members.add(target.attr)
            
            # Merge missing members from official stub
            for official_member in official_class.body:
                member_name = None
                if isinstance(official_member, (ast.FunctionDef, ast.ClassDef)):
                    member_name = official_member.name
                elif isinstance(official_member, ast.AnnAssign):
                    if isinstance(official_member.target, ast.Name):
                        member_name = official_member.target.id
                    elif isinstance(official_member.target, ast.Attribute):
                        member_name = official_member.target.attr
                elif isinstance(official_member, ast.Assign):
                    for target in official_member.targets:
                        if isinstance(target, ast.Name):
                            member_name = target.id
                        elif isinstance(target, ast.Attribute):
                            member_name = target.attr
                
                if member_name and member_name not in calibre_members:
                    logging.info(f"Added member: {member_name} to {node.name}")
                    print(f"Adding member: {member_name}")
                    node.body.append(official_member)
        
        self.generic_visit(node)  # Process nested classes
        return node

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: merger.py <calibre_stub> <official_stub>")
        sys.exit(1)

    calibre_path, official_path = sys.argv[1], sys.argv[2]

    with open(calibre_path) as f:
        calibre_ast = ast.parse(f.read())
    with open(official_path) as f:
        official_ast = ast.parse(f.read())

    merged_ast = StubMerger(official_ast).visit(calibre_ast)
    with open(calibre_path, 'w') as f:
        f.write(astunparse.unparse(merged_ast))