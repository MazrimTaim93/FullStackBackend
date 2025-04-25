import json
from fastapi import Depends
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
        print("DEBUG: Calling readCharacterByNumber in character_repository.")
        newCharacter = self.db.query(Character).filter(Character.id == id).first()
        print("DEBUG: Returning character: ", newCharacter)
        return newCharacter

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
            print(f"Character count failed.")
            raise Exception(f"Failed to count characters: {str(e)}")

    def getAllChars(self):
        try:
            characters = self.db.query(Character).all()
            return[char.to_dict() for char in characters]
        except Exception as e:
            print(f"Get all chars failed.")
            raise Exception(f"Failed to get characters: {str(e)}")