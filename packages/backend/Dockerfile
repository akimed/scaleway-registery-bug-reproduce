FROM python:3.12

RUN pip3 install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN --mount=type=cache,target=/root/.cache/pypoetry/cache \
    --mount=type=cache,target=/root/.cache/pypoetry/artifacts \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY packages/__init__.py /app/packages/
COPY packages/backend/ /app/packages/backend

CMD uvicorn packages.backend.server.main:app --port=8080 --host=0.0.0.0