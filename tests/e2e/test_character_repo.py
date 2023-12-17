# /tests/e2e/test_character_repo.py

from fastapi.testclient import TestClient
from app.endpoints.character_router import characters_router

client = TestClient(characters_router)

def test_get_characters():
  response = client.get('/characters')
  assert response.status_code == 200
  assert isinstance(response.json(), list)

def test_create_character():
  character = {
      'id': 1,
      'name': 'test',
      'class_name': 'test',
      'level': 1,
      'experience': 0,
      'strength': 0,
      'agility': 0,
      'intelligence': 0,
      'luck': 0
  }
  response = client.post('/characters/create_character', json=character)
  assert response.status_code == 200
  assert response.json() == character
