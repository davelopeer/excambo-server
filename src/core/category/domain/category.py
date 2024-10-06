import uuid
from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class Category:
  name: str
  is_active: bool = True
  id: UUID = field(default_factory=uuid.uuid4)

  def __post_init__(self):
    self._validate()
  
  def __str__(self):
    is_active  = "Active" if self.is_active else "Inactive" 
    return f"{self.name} - {is_active}"
  
  def __repr__(self):
    return f"<Category {self.name} with id ({self.id})>"
  
  def __eq__(self, other):
    if not isinstance(other, Category):
      return False

    return self.id == other.id
  
  def _validate(self):
    if len(self.name) > 255:
      raise ValueError("name cannot be longer than 255 characters")
    
    if not self.name:
      raise ValueError("name cannot be empty")

  def update_category(self, name):
    self.name = name
    self._validate()

  def activate(self):
    self.is_active = True
    self._validate()

  def deactivate(self):
    self.is_active = False
    self._validate()
