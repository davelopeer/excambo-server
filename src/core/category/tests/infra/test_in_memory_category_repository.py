from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestInMemoryCategoryRepository:
  def test_can_save_category(self):
    repository = InMemoryCategoryRepository()
    categoty = Category(
      name="Eletrônicos"
    )

    repository.save(categoty)

    assert len(repository.categories) == 1
    assert repository.categories[0] == categoty