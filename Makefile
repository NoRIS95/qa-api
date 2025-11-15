DC = docker compose
NAME = new_migration

include .env
export $(shell sed 's/=.*//' .env)

.PHONY: migrations
migrations:
ifndef NAME
	$(error NAME is not set. Usage: make migrations NAME="migration_name")
endif
	docker compose exec app sh -c "cd /app/app && alembic revision --autogenerate -m '${NAME}'"

.PHONY: migrate
migrate:
	docker compose exec app sh -c "cd /app/app && uv run alembic upgrade head"

.PHONY: app
app:
	${DC} up -d --build

.PHONY: down
down:
	${DC} down

.PHONY: lint
lint:
	docker compose exec app sh -c "cd /app/app && ruff check ."

.PHONY: lint-fix
lint-fix:
	docker compose exec app sh -c "cd /app/app && ruff check --fix --select I"
	docker compose exec app sh -c "cd /app/app && ruff check --fix"
	docker compose exec app sh -c "cd /app/app && ruff format ."
	docker compose exec app sh -c "cd /app/app && ruff check ."

.PHONY: test
test:
	export POSTGRES_HOST=$(POSTGRES_HOST) && \
	export POSTGRES_USER=$(POSTGRES_USER) && \
	export POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) && \
	docker compose exec app sh -c "cd /app/app && pytest ."

.PHONY: test-unit
test-unit:
	docker compose exec app sh -c "cd /app/app && pytest tests/unit"

.PHONY: test-integ
test-integ:
	export POSTGRES_HOST=localhost
	docker compose exec app sh -c "cd /app/app && pytest tests/integ"