from fastapi import APIRouter, Depends, HTTPException, Body

from app.models.character import Character
from app.models.equipment import Equipment

characters_router = APIRouter(prefix='/characters', tags=['Characters'])

