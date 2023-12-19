# test_character_service.py

from app.services.character_service import CharacterService
from app.repositories.character_repo import CharacterRepo
from app.models.character import Character
import uuid
from unittest.mock import Mock

def test_character_service():
 repo = Mock(spec=CharacterRepo)
 service = CharacterService(repo)

 character = Character(id=str(uuid.uuid4()), name='test', class_name='test', level=1, experience=0, strength=0, agility=0, intelligence=0, luck=0)

 repo.create_character.return_value = character
 created_character = service.create_character(character)

 repo.get_characters.return_value = [created_character]
 characters = service.get_characters()

 assert len(characters) == 1
 assert characters[0].id == created_character.id
 assert characters[0].name == created_character.name
 assert characters[0].class_name == created_character.class_name
 assert characters[0].level == created_character.level
 assert characters[0].experience == created_character.experience
 assert characters[0].strength == created_character.strength
 assert characters[0].agility == created_character.agility
 assert characters[0].intelligence == created_character.intelligence
 assert characters[0].luck == created_character.luck
