FROM python:3.11.2-alpine3.17 as build

RUN apk update && apk add --no-cache \
    bash \
    gcc \
    libc-dev \
    libffi-dev \
    libpq-dev

RUN pip install poetry==1.3.2

WORKDIR /app

COPY ./pyproject.toml .

COPY ./poetry.lock .

COPY ./README.md .

RUN mkdir "src" && echo "import this" > src/main.py

RUN poetry install

FROM python:3.11.2-alpine3.17

# Если docker compose выбрасывает ошибку на стадии установки Poetry в runtime,
# попробуйте добавить дополнительные пакеты на второй стадии сборки:
# RUN apk update && apk add --no-cache \
#     gcc \
#     libc-dev \
#     libffi-dev \
#     libpq-dev

COPY --from=build /root/.cache/pypoetry/virtualenvs/ /root/.cache/pypoetry/virtualenvs/

RUN pip install poetry==1.3.2

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .
