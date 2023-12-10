from fastapi import FastAPI, Depends, HTTPException
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
    is_active: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@api.get("/test")
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
        is_active = True,
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)

    all_characters = db.query(models.Character).all()

    for _character in all_characters:
        if _character.id != db_character.id:
            _character.is_active = False
    db.commit()


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
        is_active = db_character.is_active,
        equipment = []
    )
    return {"character": character}

@api.get("/get_active_character")
def get_active_character(db: db_dependency):
   db_character = db.query(models.Character).filter(models.Character.is_active == True).first()
   
   if db_character is None:
       raise HTTPException(status_code=404, detail="No active character found")

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
       is_active = db_character.is_active,
       equipment = []
   )
   return {"character": character}

@api.post("/edit_character")
def edit_character(character: Character, db: db_dependency):
   db_character = db.query(models.Character).filter(models.Character.id == character.id).first()
   
   if db_character is None:
       raise HTTPException(status_code=404, detail="Character not found")

   db_character.name = character.name
   db_character.class_name = character.class_name
   db_character.level = character.level
   db_character.experience = character.experience
   db_character.strength = character.strength
   db_character.agility = character.agility
   db_character.intelligence = character.intelligence
   db_character.luck = character.luck
   db_character.is_active = character.is_active

   db.commit()
   return {"message": "Character modified"}


@api.post("/select_equipment")
def select_equipment(character_id: int, equipment_id: int, db: db_dependency):
 db_character = db.query(models.Character).filter(models.Character.id == character_id).first()

 if db_character is None:
     raise HTTPException(status_code=404, detail="Character not found")

 db_equipment = db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()

 if db_equipment is None:
     raise HTTPException(status_code=404, detail="Equipment not found")

 if db_equipment.character_id is None:
     db_equipment.character_id = character_id
 else:
     db_equipment.character_id = None

 db.commit()
 return {"message": "Equipment selected"}

@api.post("/deselect_equipment")
def deselect_equipment(character_id: int, equipment_id: int, db: db_dependency):
 db_character = db.query(models.Character).filter(models.Character.id == character_id).first()

 if db_character is None:
    raise HTTPException(status_code=404, detail="Character not found")

 db_equipment = db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()

 if db_equipment is None:
    raise HTTPException(status_code=404, detail="Equipment not found")

 if db_equipment.character_id == character_id:
    db_equipment.character_id = None

 db.commit()
 return {"message": "Equipment deselected"}


