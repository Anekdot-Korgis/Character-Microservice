# /app/models/equipment.py

from pydantic import BaseModel, ConfigDict


class Equipment(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    strengh_impact: int
    dex_impact: int
    intelligence_impact: int
    luck_impact: int
    character_id: int
