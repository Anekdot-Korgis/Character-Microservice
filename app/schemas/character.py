# /app/schemas/character.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base

class Character(Base):
   __tablename__ = 'character'

   id = Column(UUID(as_uuid=True), primary_key=True, index=True)
   name = Column(String)
   class_name = Column(String)
   level = Column(Integer)
   experience = Column(Integer)
   strength = Column(Integer)
   agility = Column(Integer)
   intelligence = Column(Integer)
   luck = Column(Integer)

