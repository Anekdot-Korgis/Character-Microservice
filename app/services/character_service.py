from fastapi import Depends
from app.models.character import Character

from app.repositories.character_repo import CharacterRepo


class CharacterService:
    character_repo: CharacterRepo

    def __init__(self, character_repo: CharacterRepo = Depends(CharacterRepo)) -> None:
        self.character_repo = character_repo

    def get_characters(self) -> list[Character]:
        return self.character_repo.get_characters()

    def create_character(self, character: Character) -> Character:
        return self.character_repo.create_character(character)
