# /app/models/character.py

from pydantic import BaseModel, ConfigDict

from app.models.equipment import Equipment


class Character(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    class_name: str
    level: int
    experience: int
    strength: int
    agility: int
    intelligence: int
    luck: int
