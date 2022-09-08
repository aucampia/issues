FROM docker.io/mikefarah/yq:4@sha256:495c1e1db2d653cce61a06da52cfca0c7d68d6249cc6e61b2a134d92c609c016 AS yq
FROM docker.io/bufbuild/buf:1.7.0@sha256:21aaf6aae139b668fb23daeaef5b2b2172893a8a7d9071c8fd965cd7dd9764b1 AS buf
FROM docker.io/jbangdev/jbang-action:0.98.0@sha256:d6c55f555177d226dcd3e85d9da6fe95833a9d102438d75ed8ea12273eb329a7 AS jbang-action
FROM jbang-action AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN \
    apt-get update && \
    apt-get install -y \
        --no-install-recommends \
        protobuf-compiler \
        make \
        socat \
        ca-certificates \
        curl \
        busybox \
        git \
        rsync \
        libarchive-tools \
        && \
    rm -vr /var/lib/apt/lists/* && \
    true


COPY --from=yq /usr/bin/yq /usr/local/bin/
COPY --from=buf /usr/local/bin/buf /usr/local/bin/


RUN \
    jbang trust add https://github.com/datahub-project/datahub/ && \
    jbang trust add  https://raw.githubusercontent.com/datahub-project/datahub/ && \
    true

ENTRYPOINT []
