"""Юнит-тесты для эндпоинта удаления вопроса."""

from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from app.models.common import Question
from app.services.question import QuestionService


def test_delete_question_success(mock_db: Mock) -> None:
    """Тест успешного удаления вопроса."""
    mock_question = Mock(spec=Question)

    with patch.object(QuestionService, 'get_question', return_value=mock_question):
        result = QuestionService.delete_question(mock_db, 1)

    mock_db.delete.assert_called_once_with(mock_question)
    mock_db.commit.assert_called_once()
    assert result == mock_question

def test_delete_question_not_found(mock_db: Mock, nonexistent_id: int) -> None:
    """Тест удаления несуществующего вопроса."""
    with patch.object(QuestionService, 'get_question',
                       side_effect=HTTPException(404, "Not found")):
        with pytest.raises(HTTPException) as exc_info:
            QuestionService.delete_question(mock_db, nonexistent_id)

        assert exc_info.value.status_code == 404
        mock_db.delete.assert_not_called()
        mock_db.commit.assert_not_called()
