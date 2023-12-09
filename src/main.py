from fastapi import FastAPI
from pydantic import BaseModel

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




@app.post("/create_character")
def create_character(character: Character):
   # Connect to RabbitMQ
   character_channel = CharacterChannel(host='localhost', username='guest', password='guest')
   character_channel.connect()

   # Send a message to RabbitMQ
   character_channel.send_message('create_character_queue', character.json())

   # Close the connection
   character_channel.close()

   return {"message": "Character created"}

@app.post("/edit_character")
def edit_character(character: Character):
   # Connect to RabbitMQ
   character_channel = CharacterChannel(host='localhost', username='guest', password='guest')
   character_channel.connect()

   # Send a message to RabbitMQ
   character_channel.send_message('edit_character_queue', character.json())

   # Close the connection
   character_channel.close()

   return {"message": "Character modified"}

@app.post("/select_equipment")
def select_equipment(character: Character):
   # Connect to RabbitMQ
   character_channel = CharacterChannel(host='localhost', username='guest', password='guest')
   character_channel.connect()

   # Send a message to RabbitMQ
   character_channel.send_message('select_equipment_queue', character.json())

   # Close the connection
   character_channel.close()

   return {"message": "Equipment selected"}
