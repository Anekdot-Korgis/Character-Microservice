# test_character_service.py

from app.services.character_service import CharacterService
from app.repositories.character_repo import CharacterRepo
from app.models.character import Character
import uuid

def test_character_service():
 repo = CharacterRepo()
 service = CharacterService(repo)

 characters = service.get_characters()
 assert isinstance(characters, list)

 character = Character(id=str(uuid.uuid4()), name='test', class_name='test', level=1, experience=0, strength=0, agility=0, intelligence=0, luck=0)
 created_character = service.create_character(character)
 assert created_character.id == character.id
 assert created_character.name == character.name
 assert created_character.class_name == character.class_name
 assert created_character.level == character.level
 assert created_character.experience == character.experience
 assert created_character.strength == character.strength
 assert created_character.agility == character.agility
 assert created_character.intelligence == character.intelligence
 assert created_character.luck == character.luck
