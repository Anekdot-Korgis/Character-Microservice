from sqlalchemy import Column, Integer, String, ForeignKey
from app.schemas.base_schema import Base

class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    strength_impact = Column(Integer, default=0)
    dex_impact = Column(Integer, default=0)
    intelligence_impact = Column(Integer, default=0)
    luck_impact = Column(Integer, default=0)
    character_id = Column(Integer, ForeignKey("character.id"))
