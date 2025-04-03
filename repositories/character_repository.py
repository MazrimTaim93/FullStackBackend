import json
from xml.dom.minidom import CharacterData
from models.character_model import Character

class CharacterRepository:
    @staticmethod #return a character with a given name
    def readCharacterByName(name: str) -> Character|None:
        try:
            with open("./db/characters.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    raise Exception("Error decoding JSON.")
                for char in data["characters"]:
                    if char["name"] == name:
                        return Character(char["name"], char["gender"], 
                                         char["charClass"], char["ancestry"], char["background"])
        except FileNotFoundError:
            raise Exception("Character file not found")

        return None

    @staticmethod #return a character with a given number
    def readCharacterByNumber(number: int) -> Character|None:
        try:
            with open("./db/characters.json", "r") as file:
                    data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            #print(f"DEBUG: Error: cannot read characters.json- {e}")
            raise Exception(f"Error getting Character by number: {e}")
            
        print(f"DEBUG: Characters found in JSON file: {len(data["characters"])}")
        if number < 0 or number >= len(data["characters"]):
            #print(f"DEBUG: Requested characters index of {number} is out of bounds")
            return None

        charData = data["characters"][number]
        #print(f"DEBUG: Retrieved character data: {charData}")
        return Character(charData["name"], charData["gender"], charData["charClass"], charData["ancestry"], charData["background"])


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