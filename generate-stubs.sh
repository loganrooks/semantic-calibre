#!/bin/bash

# Unique session identifier and timestamp
SESSION_ID=$(uuidgen | cut -c1-8)
CURRENT_TS=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_DIR="/workspace/logs"
mkdir -p "$LOG_DIR"

DEBUG_LOG="$LOG_DIR/stubgen_${SESSION_ID}_${CURRENT_TS}.log"

# Initialize log with metadata
echo "🆔 Session: $SESSION_ID | 🕒 Started: $(date +'%Y-%m-%d %H:%M:%S') | 💻 Host: $(hostname)" | tee "$DEBUG_LOG"

# Parse arguments
DEBUG_MODE=false
PYTHON_CMD=("python3")
while [[ $# -gt 0 ]]; do
    case $1 in
        --debug)
            DEBUG_MODE=true
            PYTHON_CMD=("python3" "-m" "debugpy" "--listen" "0.0.0.0:5678" "--wait-for-client")
            echo "🔧 Debug mode activated | Port 5678" | tee -a "$DEBUG_LOG"
            shift
            ;;
        *)
            shift
            ;;
    esac
done

# Set output handling
if [ "$DEBUG_MODE" = true ]; then
    echo "----- Debug mode enabled. Mirroring output to $DEBUG_LOG -----"
    # Use tee for simultaneous terminal/file output without redirection
    exec 3>&1  # Save original stdout
    exec > >(tee -a "$DEBUG_LOG") 2>&1
else
    # Regular mode - just append to log file
    exec >> "$DEBUG_LOG" 2>&1
fi

echo "Generating Calibre stubs..."

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
CALIBRE_PYQT_DIR="/opt/calibre/lib/calibre-extensions"
QT6_MODULES=(
    QtWidgets QtGui QtWebEngineCore QtWebEngineWidgets 
    QtNetwork QtPrintSupport QtSql QtSvg QtCore sip
)

mkdir -p /tmp/stubgen/PyQt6
for module in "${QT6_MODULES[@]}"; do
    ln -sf "$CALIBRE_PYQT_DIR/PyQt6.${module}.so" "/tmp/stubgen/PyQt6/${module}.so"
    /opt/calibre/calibre-debug "$SHIM_SCRIPT" "PyQt6.${module}" "$CALIBRE_STUBS_DIR"
done

# Generate Calibre stubs (now processes ALL submodules recursively)
CALIBRE_MODULES=(
)

for module in "${CALIBRE_MODULES[@]}"; do
    /opt/calibre/calibre-debug "$SHIM_SCRIPT" "calibre.$module" "$CALIBRE_STUBS_DIR"
done


# 3. Merge stubs with verbose delta reporting
find "$CALIBRE_STUBS_DIR" -name '*.pyi' | while read -r CALIBRE_STUB; do
    MODULE_NAME=$(basename "$CALIBRE_STUB")
    OFFICIAL_STUB="$OFFICIAL_STUBS_DIR/PyQt6-stubs/$MODULE_NAME"

    if [[ -f "$OFFICIAL_STUB" ]]; then
        echo "Merging $MODULE_NAME"
        # Use the configured PYTHON_CMD ▼
        echo "Running: ${PYTHON_CMD[@]} /usr/local/bin/merger.py $CALIBRE_STUB $OFFICIAL_STUB"
        "${PYTHON_CMD[@]}" /usr/local/bin/merger.py "$CALIBRE_STUB" "$OFFICIAL_STUB"

        black --quiet "$CALIBRE_STUB" 2>/dev/null || true
    else
        echo "Skipping: No official stub for $MODULE_NAME"
    fi
done

# 4. Cleanup
rm -rf "$OFFICIAL_STUBS_DIR"
echo "Merged stubs generated at: $CALIBRE_STUBS_DIR"

chmod -R a+rw "$CALIBRE_STUBS_DIR"
echo "Stub generation complete!"