import traceback
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.character import Character
from app.models.equipment import Equipment
from app.schemas.character import Character as DBCharacter


class CharacterRepo:
    db: Session

    def __init__(self):
        self.db = next(get_db())

    def __map_to_model(self, character: DBCharacter) -> Character:
        result = Character.model_validate(character, strict=False)
        return result

    def __map_to_schema(self, character: Character) -> DBCharacter:
        data = dict(character)
        return DBCharacter(**data)

    def get_characters(self) -> list[Character]:
        return [self.__map_to_model(c) for c in self.db.query(DBCharacter).all()]

    def create_character(self, character: Character) -> Character:
        try:
            db_character = self.__map_to_schema(character)
            self.db.add(db_character)
            self.db.commit()
            return self.__map_to_model(db_character)
        except:
            traceback.print_exc()
            raise KeyError
