FROM  ghcr.io/astral-sh/uv:python3.11-alpine

ADD . /app

WORKDIR /app

RUN uv sync

ENTRYPOINT source entrypoint.sh
