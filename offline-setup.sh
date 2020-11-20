#!/usr/bin/env bash

pip install getgauge && \
pip install selenium && \
pip install chromedriver-binary==83.0.4103.39 && \
mkdir tmp && cd tmp && \
# Install Gauge
# https://docs.gauge.org/getting_started/installing-gauge.html?os=linux&language=python&ide=vscode
wget https://github.com/getgauge/gauge/releases/download/v1.1.5/gauge-1.1.5-linux.x86_64.zip &&  \
unzip -o gauge-1.1.5-linux.x86_64.zip -d /usr/local/bin  && rm -rf gauge-1.1.5-linux.x86_64.zip && \
gauge -v && \
# Install html-report plugin
wget https://github.com/getgauge/html-report/releases/download/v4.0.12/html-report-4.0.12-linux.x86_64.zip && \
gauge install html-report --file html-report-4.0.12-linux.x86_64.zip && \
# Install screenshot plugin
wget https://github.com/getgauge/gauge_screenshot/releases/download/v0.0.1/screenshot-0.0.1-linux.x86_64.zip && \
gauge install screenshot --file screenshot-0.0.1-linux.x86_64.zip && \
# Install python plugin
# https://docs.gauge.org/plugin.html?os=linux&language=python&ide=vscode
wget https://github.com/getgauge/gauge-python/releases/download/v0.3.12/gauge-python-0.3.12.zip  && \
gauge install python --file gauge-python-0.3.12.zip && \
gauge -v
