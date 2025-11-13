"""Основной модуль приложения для создания FastAPI сервиса."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from loguru import logger

from app.api import answer, question
from app.db.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, Any, Any]:
    """Обработка событий жизненного цикла приложения FastAPI."""
    logger.info("Запуск приложения: создание таблиц базы данных")
    Base.metadata.create_all(bind=engine)
    yield
    logger.info("Таблицы базы данных успешно созданы")

app = FastAPI(
    title="QA-API",
    lifespan=lifespan)

@app.get("/")
def read_root() -> dict:
    """Тестовый эндпоинт."""
    return {"message": "Welcome to QA-API"}

@app.get("/health")
async def health_check() -> dict:
    """Эндпоинт проверки здоровья сервиса."""
    return {"status": "healthy"}

app.include_router(question.router, prefix="/questions", tags=["questions"])
app.include_router(answer.router, tags=["answers"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

