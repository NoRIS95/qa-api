"""Файл с общей фикстурой."""

import uuid

import pytest


@pytest.fixture
def answer_data() -> dict:
    """Фикстура данных для создания ответа."""
    return {
        "text": "Тестовый ответ на вопрос",
        "user_id": str(uuid.uuid4()),
    }

@pytest.fixture
def question_data() -> dict:
    """Фикстура данных для создания вопроса."""
    return {
        "text": "Тестовый вопрос",
    }

@pytest.fixture
def nonexistent_id() -> int:
    """Фикстура несуществующего ID."""
    return 82374682734628356
