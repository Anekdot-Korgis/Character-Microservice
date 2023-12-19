import pytest
from fastapi.testclient import TestClient
import app
import uuid

client = TestClient(app)

def test_create_character():
   character = {
       'id': str(uuid.uuid4()),
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
   assert response.json() == {
       'name': character['name'],
       'class_name': character['class_name'],
       'level': character['level'],
       'experience': character['experience'],
       'strength': character['strength'],
       'agility': character['agility'],
       'intelligence': character['intelligence'],
       'luck': character['luck']
   }
