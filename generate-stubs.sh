#!/bin/bash

STUB_DIR="/stubgen/calibre-stubs"
mkdir -p "$STUB_DIR"

SHIM_SCRIPT="/tmp/stubgen-shim.py"
# Updated SHIM_SCRIPT section with module type detection
cat << 'EOF' > "$SHIM_SCRIPT"
import sys
sys.path.insert(0, "/tmp/packages/site-packages")
sys.path.insert(0, "/tmp/stubgen")

import os
import importlib
import pkgutil
from pybind11_stubgen import main as pybind_main
from mypy.stubgen import main as mypy_main


def is_compiled_module(module: object) -> bool:
    """Check if module is a compiled C extension"""
    return getattr(module, '__file__', '').endswith(('.so', '.pyd'))

def generate_stubs(module_name: str, output_root: str) -> None:
    try:
        module = importlib.import_module(module_name)
        is_compiled = is_compiled_module(module)
        is_package = hasattr(module, '__path__') and not is_compiled
        print(f"Generating stubs for {module_name} (compiled: {is_compiled}, package: {is_package})")
        if is_package:
            print(f"Package path: {module.__path__}")

        sys.path.insert(0, "/opt/calibre/lib/calibre-extensions/python-lib.bypy.frozen")
            
        # Generate pybind stubs first
        if is_compiled:
            sys.argv = [
                "pybind11-stubgen", module_name,
                "-o", output_root,
                "--ignore-all-errors",
                "--root-suffix", ""
            ]
            pybind_main()

        if not is_compiled and is_package:
            # Special handling for frozen packages
            from pkgutil import iter_modules
            package_path = [p for p in sys.path if "calibre-extensions" in p]

            for _, sub_name, _ in iter_modules(package_path, prefix=f"{module_name}."):
                generate_stubs(sub_name, output_root)

    except Exception as e:
        print(f"Error processing {module_name}: {str(e)}", file=sys.stderr)
        raise  # Reraise to ensure clean exit

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print("Usage: python stubgen-shim.py <module_name> <output_dir>")
            sys.exit(1)
        generate_stubs(sys.argv[1], sys.argv[2])
    finally:
        sys.exit(0)  # Force clean exit to prevent interactive shell
EOF

# Generate PyQt6 stubs
QT6_MODULES=(
    QtWidgets QtGui QtWebEngineCore QtWebEngineWidgets 
    QtNetwork QtPrintSupport QtSql QtSvg QtCore sip
)

mkdir -p /tmp/stubgen/PyQt6
for module in "${QT6_MODULES[@]}"; do
    ln -sf "/opt/calibre/lib/calibre-extensions/PyQt6.${module}.so" "/tmp/stubgen/PyQt6/${module}.so"
    /opt/calibre/calibre-debug "$SHIM_SCRIPT" "PyQt6.${module}" "$STUB_DIR"
done

# Generate Calibre stubs (now processes ALL submodules recursively)
CALIBRE_MODULES=(
)

for module in "${CALIBRE_MODULES[@]}"; do
    /opt/calibre/calibre-debug "$SHIM_SCRIPT" "calibre.$module" "$STUB_DIR"
done

chmod -R a+rw "$STUB_DIR"
echo "Stub generation complete!"