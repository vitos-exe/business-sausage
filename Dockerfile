FROM  ghcr.io/astral-sh/uv:python3.13-alpine

ADD . /app

WORKDIR /app

RUN uv sync --frozen

ENTRYPOINT source entrypoint.sh 

