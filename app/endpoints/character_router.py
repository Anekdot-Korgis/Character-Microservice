from fastapi import APIRouter, Depends, HTTPException, Body

from app.models.character import Character
from app.models.equipment import Equipment

# todo: from app.services.servicename import CharactersService

characters_router = APIRouter(prefix='/characters', tags=['Characters'])

@characters_router.get('/')
def get_characters():
    return None # сходить в сервис и получить список чопиксов

@characters_router.post('/create_character')
def create_character(
    character: Character,
    # todo: characters_service: Depends(CharactersService)
):
    try:
        return None # сходить в сервис и создать чопикса
    except:
        raise HTTPException(418, 'Я чайник')
