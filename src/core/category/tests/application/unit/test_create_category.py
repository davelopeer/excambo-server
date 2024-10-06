from unittest.mock import MagicMock
import uuid

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.exceptions import InvalidCategoryData


class TestCreateCategory:
  def test_create_category_with_valid_data(self):
    mock_repository = MagicMock(CategoryRepository)
    use_Case = CreateCategory(repository=mock_repository)
    req = CreateCategoryRequest(
      name="Eletrônicos",
      is_active=True
    )

    res = use_Case.execute(req)

    assert res.id is not None
    assert isinstance(res.id, uuid.UUID)
    assert mock_repository.save.called

  def test_create_category_with_invalid_data(self):
    mock_repository = MagicMock(CategoryRepository)
    use_Case = CreateCategory(repository=mock_repository)
    req = CreateCategoryRequest(
      name=""
    )

    with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
      use_Case.execute(req)