# test_models.py

from app.models.character import Character
from app.models.equipment import Equipment

def test_character_model():
  character = Character(id=1, name='test', class_name='test', level=1, experience=0, strength=0, agility=0, intelligence=0, luck=0)
  assert character.id == 1
  assert character.name == 'test'
  assert character.class_name == 'test'
  assert character.level == 1
  assert character.experience == 0
  assert character.strength == 0
  assert character.agility == 0
  assert character.intelligence == 0
  assert character.luck == 0

def test_equipment_model():
  equipment = Equipment(id=1, name='test', strength_impact=0, dex_impact=0, intelligence_impact=0, luck_impact=0, character_id=1)
  assert equipment.id == 1
  assert equipment.name == 'test'
  assert equipment.strength_impact == 0
  assert equipment.dex_impact == 0
  assert equipment.intelligence_impact == 0
  assert equipment.luck_impact == 0
  assert equipment.character_id == 1