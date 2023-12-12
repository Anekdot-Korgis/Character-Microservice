from sqlalchemy import Column, Integer, String
from app.schemas.base_schema import Base

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
