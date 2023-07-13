FROM docker.io/library/python:3.11-slim-bookworm@sha256:364ee1a9e029fb7b60102ae56ff52153ccc929ceab9aa387402fe738432d24cc AS python

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

FROM python AS toolchain

RUN \
    apt-get update && \
    apt-get install --no-install-recommends -y jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    true

COPY requirements-toolchain.txt /var/tmp/requirements-toolchain.txt

RUN \
    pip install  --no-cache-dir -r /var/tmp/requirements-toolchain.txt && \
    rm -rf /var/tmp/requirements-poetry.txt && \
    true

ENTRYPOINT [ ]

FROM toolchain AS check

COPY poetry.lock pyproject.toml /var/tmp/project/

WORKDIR /var/tmp/project

# Install dependencies
RUN \
    poetry install && \
    poetry show --tree && \
    true

# Update sqlparse
RUN \
    poetry update sqlparse && \
    poetry show --tree && \
    true

# Check that sqlparse is not a pre-release version
RUN \
    set -x && \
    poetry show dbt-core && \
    poetry run dbt --version && \
    DBT_VERSION=$(tomlq -r '.package[] | select( .name == "dbt-core" ) | .version' poetry.lock) && \
    1>&2 echo "Check that dbt ${DBT_VERSION} is not a pre-release version" && \
    ! { echo "${DBT_VERSION}" | grep -E -- '[ab][0-9]$'; } && \
    true
