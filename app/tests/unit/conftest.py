"""Фикстуры для юнит-тестов."""

import uuid
from datetime import datetime
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.models.common import Answer, Question


@pytest.fixture
def client() -> TestClient:
    """Фикстура клиента."""
    return TestClient(app)


@pytest.fixture
def mock_db() -> Mock:
    """Фикстура мока базы данных."""
    return Mock(spec=Session)


@pytest.fixture
def sample_question() -> Question:
    """Фикстура тестового вопроса."""
    question = Mock(spec=Question)
    question.id = 1
    question.title = "Тестовый вопрос"
    question.text = "Текст тестового вопроса"
    return question


@pytest.fixture
def sample_question_for_api() -> Question:
    """Фикстура вопроса с полными данными для API тестов."""
    question = Mock(spec=Question)
    question.id = 1
    question.title = "Тестовый вопрос"
    question.text = "Текст тестового вопроса"
    question.created_at = datetime.now()
    question.answers = []
    return question


@pytest.fixture
def sample_answer_for_api() -> Answer:
    """Фикстура ответа с полными данными для API тестов."""
    answer = Mock(spec=Answer)
    answer.id = 1
    answer.title = "Тестовый ответ"
    answer.text = "Текст тестового ответа"
    answer.user_id = str(uuid.uuid4())
    answer.question_id = 1
    answer.created_at = datetime.now()
    answer.answers = []
    return answer


@pytest.fixture
def sample_answer() -> Answer:
    """Фикстура тестового ответа."""
    answer = Mock(spec=Answer)
    answer.id = 1
    answer.title = "Тестовый ответ"
    answer.text = "Текст тестового вопроса"
    answer.question_id = 1
    answer.user_id = str(uuid.uuid4())
    return answer
