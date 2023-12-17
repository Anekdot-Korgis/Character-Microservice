# /app/models/equipment.py

from uuid import UUID
from typing_extensions import Annotated
from pydantic import BaseModel, Field, ConfigDict

class Equipment(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: Annotated[UUID, Field(default_factory=lambda: UUID(int=0))]
  name: str
  strength_impact: int
  dex_impact: int
  intelligence_impact: int
  luck_impact: int
  character_id: UUID


