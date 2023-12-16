# /app/endpoints/character_router.py

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body

from app.models.character import Character
from app.models.equipment import Equipment
from app.services.character_service import CharacterService

characters_router = APIRouter(prefix='/characters', tags=['Characters'])

characters_service = Annotated[CharacterService, Depends(CharacterService)]

@characters_router.get('/')
def get_characters(
    service: characters_service
):
    return service.get_characters()

@characters_router.post('/create_character')
def create_character(
    character: Character,
    service: characters_service
):
    try:
        return service.create_character(character)
    except:
        raise HTTPException(418, 'Я чайник')
