# /app/models/character.py

from uuid import UUID
from typing_extensions import Annotated
from pydantic import BaseModel, Field, ConfigDict
from app.models.equipment import Equipment

class Character(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: Annotated[UUID, Field(default_factory=lambda: UUID(int=0))]
  name: str
  class_name: str
  level: int
  experience: int
  strength: int
  agility: int
  intelligence: int
  luck: int

