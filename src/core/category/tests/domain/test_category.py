import unittest
from uuid import UUID, uuid4
import pytest

from src.core.category.domain.category import Category


class TestCategory(unittest.TestCase):
  def test_name_is_required(self):
    with pytest.raises(TypeError):
      Category()

  def test_name_must_have_less_than_256_characters(self):
    with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
      Category(name="a"*256)
  
  def test_category_must_be_created_with_uuid_as_default(self):
    category = Category(name="Eletrônicos")
    assert isinstance(category.id, UUID)

  def test_create_category_with_default_values(self):
    category = Category(name="Eletrônicos")

    assert category.name == "Eletrônicos"
    assert category.is_active is True

  def test_create_category_with_default_values(self):
    category = Category(name="Eletrônicos")

    assert category.name == "Eletrônicos"
    assert category.is_active == True

  def test_create_category_with_provided_values(self):
    id = uuid4()
    category = Category(
      name="Eletrônicos",
      id=id,
      is_active=False
    )

    assert category.name == "Eletrônicos"
    assert category.is_active == False
    assert category.id == id

  def test_cannot_create_category_with_empty_name(self):
    with pytest.raises(ValueError, match="name cannot be empty"):
      Category(name="")


class TestUpdateCategory:
  def test_update_category_with_name(self):
    category = Category(name="Eletrônicos")

    category.update_category(name="Eletrodomésticos")

    assert category.name == "Eletrodomésticos"

  def test_update_category_with_invalid_name(self):
    category = Category(name="Eletrônicos")

    with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
      category.update_category(name="a"*256)

  def test_cannot_update_category_with_empty_name(self):
    category = Category(name="Eletrônicos")

    with pytest.raises(ValueError, match="name cannot be empty"):
      category.update_category(name="")


class TestActivateCategory:
  def test_activate_category(self):
    category = Category(
      name="Eletrônicos",
      is_active=False,
    )

    category.activate()

    assert category.is_active is True

  def test_activate_active_category(self):
    category = Category(
      name="Eletrônicos",
    )

    category.activate()

    assert category.is_active is True


class TestDeactivateCategory:
  def test_deactivate_category(self):
    category = Category(
      name="Eletrônicos",
    )

    category.deactivate()

    assert category.is_active is False

  def test_deactivate_inactive_category(self):
    category = Category(
      name="Eletrônicos",
      is_active=False,
    )

    category.deactivate()

    assert category.is_active is False


class TestEquality:
  def test_when_categories_have_same_id_are_equals(self):
    common_id = uuid4()
    category_1 = Category(name="Eletrônicos", id=common_id)
    category_2 = Category(name="Eletrônicos", id=common_id)

    assert category_1 == category_2

  def test_equality_with_different_classes(self):
    class Dummy:
      pass

    common_id = uuid4()
    category = Category(name="Eletrônicos", id=common_id)
    dummy = Dummy()
    dummy.id = common_id

    assert category != dummy