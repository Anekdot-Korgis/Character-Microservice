from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Annotated
import app.models as models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session

api = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Equipment(BaseModel):
    id: int
    name: str
    strengh_impact: int
    dex_impact: int
    intelligence_impact: int
    luck_impact: int
    character_id: int

class Character(BaseModel):
    id: int
    name: str
    class_name: str
    level: int
    experience: int
    strength: int
    agility: int
    intelligence: int
    luck: int
    equipment: List[Equipment]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@api.get("/hello_world")
def hello_world():
    return {"message": 1243256324}

@api.post("/create_character")
def create_character(character: Character, db: db_dependency):
    db_character = models.Character(
        name = character.name,
        class_name = character.class_name,
        level = character.level,
        experience = character.experience,
        strength = character.strength,
        agility = character.agility,
        intelligence = character.intelligence,
        luck = character.luck,
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)

    for equipment in character.equipment:
        db_equipment = models.Equipment(
            name = equipment.name,
            strength_impact = equipment.strengh_impact,
            dex_impact = equipment.dex_impact,
            intelligence_impact = equipment.intelligence_impact,
            luck_impact = equipment.luck_impact,
            character_id = db_character.id
        )
        db.add(db_equipment)
    db.commit()
    return {"message": "Character created"}

@api.get("/get_character/{character_id}")
def get_character(character_id: int, db: db_dependency):
    db_character = db.query(models.Character).get(character_id)
    character = Character(
        id = db_character.id,
        name = db_character.name,
        class_name = db_character.class_name,
        level = db_character.level,
        experience = db_character.experience,
        strength = db_character.strength,
        agility = db_character.agility,
        intelligence = db_character.intelligence,
        luck = db_character.luck,
        equipment = []
    )
    return {"character": character}

@api.post("/edit_character")
def edit_character(character: Character):

    return {"message": "Character modified"}

@api.post("/select_equipment")
def select_equipment(character: Character):

    return {"message": "Equipment selected"}
