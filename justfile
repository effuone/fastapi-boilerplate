default:
  just --list

install:
  venv/bin/poetry install --no-root

run *args:
  venv/bin/poetry run uvicorn src.main:app --reload {{args}}

mm *args:
  venv/bin/poetry run alembic revision --autogenerate -m "{{args}}"

seed: 
  chmod +x alembic/sql/seed.sh && ./alembic/sql/seed.sh

migrate:
  venv/bin/poetry run alembic upgrade head

downgrade *args:
  venv/bin/poetry run alembic downgrade {{args}}

ruff *args:
  venv/bin/poetry run ruff check {{args}} src

lint:
  venv/bin/poetry run ruff format src
  just ruff --fix

# docker
up:
  docker compose up -d

kill *args:
  docker compose kill {{args}}

build:
  docker compose build

ps:
  docker compose ps