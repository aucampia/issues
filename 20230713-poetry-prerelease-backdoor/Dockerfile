FROM docker.io/library/python:3.11-slim-bookworm@sha256:364ee1a9e029fb7b60102ae56ff52153ccc929ceab9aa387402fe738432d24cc AS python


FROM python AS toolchain

COPY requirements-poetry.txt /var/tmp/requirements-poetry.txt

RUN \
    pip install  --no-cache-dir -r /var/tmp/requirements-poetry.txt && \
    rm -rf /var/tmp/requirements-poetry.txt && \
    true

ENTRYPOINT [ ]

FROM poetry AS project

COPY poetry.lock pyproject.toml /var/tmp/project/

RUN \
    cd /var/tmp/project && \
    poetry update sqlplus && \
    poetry run dbt --version && \
    true
