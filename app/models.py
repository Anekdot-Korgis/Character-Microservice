from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)
    strengh_impact = Column(Integer, default=0)
    dex_impact = Column(Integer, default=0)
    intelligence_impact = Column(Integer, default=0)
    luck_impact = Column(Integer, default=0)
    character_id = Column(Integer, ForeignKey("character.id"))


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True, index=True)
    #user_id: Column()
    name = Column(String)
    class_name = Column(String)
    level = Column(Integer)
    experience = Column(Integer)
    strength = Column(Integer)
    agility = Column(Integer)
    intelligence = Column(Integer)
    luck = Column(Integer)
