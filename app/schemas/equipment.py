# /app/schemas/equipment.py

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base

class Equipment(Base):
   __tablename__ = 'equipment'

   id = Column(UUID(as_uuid=True), primary_key=True, index=True)
   name = Column(String)
   strength_impact = Column(Integer, default=0)
   dex_impact = Column(Integer, default=0)
   intelligence_impact = Column(Integer, default=0)
   luck_impact = Column(Integer, default=0)
   character_id = Column(UUID(as_uuid=True), ForeignKey("character.id"))
