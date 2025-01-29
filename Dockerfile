# COMMANDS TO GENERATE STUBS:
# docker build -t calibre-stubgen .
# docker run -it --rm  \
# -v "$(pwd)/calibre-stubs:/stubgen/calibre-stubs" \
# -v "$(pwd):/workspace" \
# calibre-stubgen 

# Dockerfile
FROM ubuntu:22.04

# Core utilities
RUN apt-get update && apt-get install -y \
    wget \
    python3-pip \
    patchelf \
    && apt-get clean

# Calibre dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libdbus-1-3 \
    libfontconfig1 \
    libglib2.0-0 \
    libasound2 \
    && apt-get clean

# PyQt6/Qt6 dependencies
RUN apt-get update && apt-get install -y \
    qt6-base-dev \
    libegl1 \
    libopengl0 \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender1 \
    libxcomposite1 \
    && apt-get clean

# XCB dependencies for Qt
RUN apt-get update && apt-get install -y \
    libx11-xcb1 \
    libxkbfile1 \
    libxcb-cursor0 \
    libxcb-xinerama0 \
    libxcb-util1 \
    libxcb-icccm4 \
    libxcb-keysyms1 \
    libxcb-image0 \
    libxcb-xinput0 \
    libxcb-dri3-0 \
    libxkbcommon-x11-0 \
    && apt-get clean 

# Calibre installation
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin \
    && rm -rf /var/lib/apt/lists/*

# Git
RUN apt-get update && apt-get install -y \
    git

# Pybind11 stub prerequisites
RUN rm -rf /tmp/packages && \
    pip3 install --target=/tmp/packages/site-packages \
    "pybind11-stubgen>=2.5.0" mypy tomli typing_extensions

# Force pybind11-stubgen to generate stubs for all modules
RUN sed -i \
    -e 's/if name.startswith("__")/if False/' \  
    -e 's/recursive=False/recursive=True/' \     
    /tmp/packages/site-packages/pybind11_stubgen/__init__.py

# Location for final generated stubs
ENV CALIBRE_STUBS_DIR="/stubgen/calibre-stubs"
RUN mkdir -p "$CALIBRE_STUBS_DIR"

# For merging stubs from official PyQt6-stubs
RUN pip3 install astunparse

ENV OFFICIAL_STUBS_DIR="/tmp/pyqt6-official-stubs"
RUN git clone --depth 1 https://github.com/python-qt-tools/PyQt6-stubs.git "$OFFICIAL_STUBS_DIR"

# Copy merger script to container
COPY src/calibre/utils/merger.py /usr/local/bin/

# Ensure execute permissions
RUN chmod +x /usr/local/bin/merger.py

# Stub generation script
COPY generate-stubs.sh /usr/local/bin/generate-stubs
RUN chmod +x /usr/local/bin/generate-stubs

# Install tee for output redirection
RUN apt-get update && apt-get install -y coreutils

# Ensure log directory exists
RUN mkdir -p /workspace/logs && chmod a+rw /workspace/logs

# Add debugpy installation
RUN pip3 install --force-reinstall "debugpy>=1.8.0"

# Add debug environment setup
ENV PYTHONBREAKPOINT=debugpy.breakpoint

# Mount points
VOLUME ["/stubgen/calibre-stubs", "/workspace"]

# Use system calibre installation
ENV PATH="/opt/calibre:${PATH}"
WORKDIR /stubgen

# Default command to generate stubs
ENTRYPOINT ["/usr/local/bin/generate-stubs"]
CMD []