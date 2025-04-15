import json
from xml.dom.minidom import CharacterData
from models.character_model import Character

class CharacterRepository:
    def __init__(self, db):
        self.db = db.get_session()

    def readCharacterByName(self, name: str) -> Character:
        return self.db.query(Character).filter(Character.name == name).first()

    @staticmethod #return a character with a given number
    def readCharacterByNumber(self, id: int) -> Character:
        return self.db.query(Character).filter(Character.id == id).first()

    @staticmethod #Take character passed in and add to the database
    def writeCharacter(newChar: Character) -> None:
        try:
            with open("./db/characters.json", "r") as file:
                data = json.load(file) #read in file
                newChar = newChar.model_dump() #turn into json
                data["characters"].append(newChar) #add to file

            with open("./db/characters.json", "w") as file:
                json.dump(data, file, indent = 4) #write to document

        except FileNotFoundError:
            raise Exception("Character file not found")

    @staticmethod #count the number of characters in the db
    def getCharCount() -> int:
        try:
            with open("./db/characters.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    raise Exception("Error decoding JSON.")
                i = 0
                for char in data["characters"]:
                    i += 1
        except FileNotFoundError:
            raise Exception("Character file not found")

        return i