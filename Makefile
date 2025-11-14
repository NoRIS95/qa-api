DC = docker compose
include .env
export $(shell sed 's/=.*//' .env)

.PHONY: migrations
migrations:
	cd app && alembic revision --autogenerate -m ${NAME}

.PHONY: migrate
migrate:
	cd app && alembic upgrade head

.PHONY: app
app:
	${DC} up -d --build

.PHONY: down
down:
	${DC} down

.PHONY: lint
lint:
	ruff check .

.PHONY: lint-fix
lint-fix:
	ruff check --fix --select I
	ruff check --fix
	ruff format
	ruff check

.PHONY: test
test:
	export POSTGRES_HOST=$(POSTGRES_HOST) && \
	export POSTGRES_USER=$(POSTGRES_USER) && \
	export POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) && \
	pytest .

.PHONY: test-unit
test-unit:
	pytest app/tests/unit

.PHONY: test-integ
test-integ:
	export POSTGRES_HOST=localhost
	pytest app/tests/integ