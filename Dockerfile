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

# Pybind11 stub prerequisites
RUN rm -rf /tmp/packages && \
    pip3 install --target=/tmp/packages/site-packages \
    "pybind11-stubgen>=2.5.0" mypy tomli typing_extensions

# Stub generation script
COPY generate-stubs.sh /usr/local/bin/generate-stubs
RUN chmod +x /usr/local/bin/generate-stubs

# Default command to generate stubs
WORKDIR /stubgen
CMD ["generate-stubs"]