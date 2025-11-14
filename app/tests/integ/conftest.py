"""Фикстуры длдя интеграционных тестов."""

from collections.abc import Generator
from typing import Any

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.database import get_db
from app.main import app
from app.models.common import Base


@pytest.fixture(scope="module")
def test_db() -> Generator[Any, Any, Any]:
    """Фикстура для создания тестовой базы данных."""
    engine = create_engine("sqlite:///test_integ.db")
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(test_db: Engine) -> Generator[Session, Any]:
    """Фикстура для сессии БД, создаваемой для каждого теста."""
    SessionLocal = sessionmaker(bind=test_db)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def client(db_session: Session) -> Generator[TestClient, Any]:
    """Фикстура клиента с подменой БД."""

    def override_get_db() -> Generator[Session, Any]:
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def sample_question(client: TestClient) -> dict[str, Any]:
    """Фикстура создания тестового вопроса."""
    response = client.post("/questions/", json={"text": "Тестовый вопрос"})
    data_question = response.json()
    return data_question
