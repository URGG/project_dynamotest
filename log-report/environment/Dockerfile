FROM ubuntu@sha256:278628f08d4979fb9af9ead44277dbc9c92c2465922310916ad0c46ec9999295

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-pytest && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY access.log /app/access.log