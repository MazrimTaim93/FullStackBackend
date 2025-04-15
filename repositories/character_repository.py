import json
from sqlalchemy.orm import Session
from xml.dom.minidom import CharacterData
from models.character_model import Character

class CharacterRepository:
    def __init__(self, db):
        self.db = db.get_session()

    def readCharacterByName(self, name: str) -> Character:
        return self.db.query(Character).filter(Character.name == name).first()

    #return a character with a given number
    def readCharacterByNumber(self, id: int) -> Character:
        return self.db.query(Character).filter(Character.id == id).first()

    #write a given character to the database
    def writeCharacter(self, new_char: Character) -> None:
        try:
            self.db.add(new_char)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Failed to write character to DB: {str(e)}")

    #count the number of characters in the db
    def getCharCount(self) -> int:
        try:
            return self.db.query(Character).count()
        except Exception as e:
            raise Exception(f"Failed to count characters: {str(e)}")