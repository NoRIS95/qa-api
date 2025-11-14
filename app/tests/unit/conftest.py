"""Фикстуры для юнит-тестов."""

from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.common import Question


@pytest.fixture
def client() -> TestClient:
    """Фикстура клиента."""
    return TestClient(app)


@pytest.fixture
def sample_question() -> Question:
    """Фикстура тестового вопроса для тестов ответов."""
    question = Mock(spec=Question)
    question.id = 1
    question.title = "Тестовый вопрос"
    question.text = "Текст тестового вопроса"
    return question
