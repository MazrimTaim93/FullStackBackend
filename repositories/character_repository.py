import json
from fastapi import Depends
from sqlalchemy.orm import Session
from xml.dom.minidom import CharacterData
from models.character_model import Character
from typing import List

class CharacterRepository:
    def __init__(self, db):
        self.db = db.get_session()

    #return a character with a given number
    def readCharacterByNumber(self, id: int) -> Character:
        try:
            #print("DEBUG: Calling readCharacterByNumber in character_repository.")
            newCharacter = self.db.query(Character).filter(Character.id == id).first()
            #print("DEBUG: Returning character: ", newCharacter)
            return newCharacter
        except Exception as e:
            self.db.rollback()
            print(f"DEBUG: Error returning character {id}: {str(e)}")
            raise Exception(f"Failed to read character {id}: {str(e)}")

    #write a given character to the database
    def writeCharacter(self, new_char: Character) -> None:
        try:
            print("DEBUG: character_repository.py received request to create character.")
            self.db.add(new_char)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"DEBUG: Error while writing new character: {str(e)}")
            raise Exception(f"Failed to write character to DB: {str(e)}")

    #count the number of characters in the db
    def getCharCount(self) -> int:
        try:
            return self.db.query(Character).count()
        except Exception as e:
            print(f"Character count failed.")
            self.db.rollback()
            raise Exception(f"Failed to count characters: {str(e)}")

    #delete a character
    def deleteCharacter(self, id: int) -> bool:
        try:
            character = self.db.query(Character).filter(Character.id == id).first()
            if character:
                self.db.delete(character)
                self.db.commit()

        except Exception as e:
            self.db.rollback()
            print(f"DEBUG: Error deleting character {id}: {str(e)}")
            raise Exception(f"Failed to delete character {id}: {str(e)}")

    #get all character ids and return a list
    def getAll(self) -> List[int]:
        try:
            ids = self.db.query(Character.id).all()
            return [id[0] for id in ids]

        except Exception as e:
            self.db.rollback()
            print(f"DEBUG: Error getting all characters: {str(e)}")
            raise Exception(f"Failed to get all characters: {str(e)}")