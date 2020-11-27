FROM mcr.microsoft.com/vscode/devcontainers/universal:linux

USER root

# [Option] Install Docker CLI
ARG INSTALL_DOCKER="false"
COPY library-scripts/docker-debian.sh /tmp/library-scripts/
RUN if [ "${INSTALL_DOCKER}" = "true" ]; then \
        rm -f /usr/local/share/docker-init.sh \
        && bash /tmp/library-scripts/docker-debian.sh "true" "/var/run/docker-host.sock" "/var/run/docker.sock" "codespace"; \
    fi \
    && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/

COPY library-scripts/python-debian.sh /tmp/library-scripts/
RUN bash /tmp/library-scripts/python-debian.sh \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

ARG CHROMIUM_VERSION="73.0.3683.75-1~deb9u1"
# [Optional] Uncomment this section to install additional OS packages.
RUN  apt-get update && export DEBIAN_FRONTEND=noninteractive \
   && apt-get -y install --no-install-recommends chromium=${CHROMIUM_VERSION} \
# Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER codespace

# Install gauge
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -SsL https://downloads.gauge.org/stable | sh

# Check gauge installed successfully and install plugins
RUN gauge -v \
     && gauge install python \
     && gauge install html-report \
     && gauge install screenshot \
     && gauge install spectacle \
     # Install testrail plugin
     && git clone https://github.com/ajoecker/gauge-testrail.git \
     && mvn -f gauge-testrail/ clean install \
     && mvn -f gauge-testrail/ clean package \
     && gauge install testrail-sync -f gauge-testrail/gauge-testrail-sync/artifacts/testrail-sync-0.0.2.zip \
     && gauge -v
