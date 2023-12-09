from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


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


@app.get("/hello_world")
def hello_world():
   return {"message": 1243256324}

@app.post("/create_character")
def create_character(character: Character):

   return {"message": "Character created"}

@app.post("/edit_character")
def edit_character(character: Character):

   return {"message": "Character modified"}

@app.post("/select_equipment")
def select_equipment(character: Character):

   return {"message": "Equipment selected"}
