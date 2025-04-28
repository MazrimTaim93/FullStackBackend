from repositories.character_repository import CharacterRepository

class CharacterService:
    def __init__(self, character_repository: CharacterRepository):
        self.character_repository = character_repository

    def getCharCount(self) -> int:
        count = self.character_repository.getCharCount()
        return count

    def writeCharacter(self, newChar) -> bool:
        print("DEBUG: character_service.py received request to create character.")
        success = self.character_repository.writeCharacter(newChar)
        return success

    def getAllChars(self):
        characters = self.character_repository.getAllChars()
        return characters

    def getByNumber(self, id: int):
        character = self.character_repository.readCharacterByNumber(id)
        return character