# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT=3
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

# Install gauge
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -SsL https://downloads.gauge.org/stable | sh

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 install --upgrade pip \
     && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
     && rm -rf /tmp/pip-tmp

# Check gauge installed successfully and install plugins
RUN gauge -v \
     && gauge install python \
     && gauge install html-report \
     && gauge install screenshot \
     && gauge install spectacle

ARG CHROMIUM_VERSION="83.0.4103.116-1~deb10u3"
# [Optional] Uncomment this section to install additional OS packages.
RUN  apt-get update && export DEBIAN_FRONTEND=noninteractive \
   && apt-get -y install --no-install-recommends chromium=${CHROMIUM_VERSION} \
# Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
