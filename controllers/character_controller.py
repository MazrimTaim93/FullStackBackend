from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException
from models.character_model import Character
from repositories.character_repository import CharacterRepository
from schemas.character_schema import CountRequest, CountResponse, CreateRequest, CreateResponse, GetByNumberRequest, GetByNumberResponse

router = APIRouter(prefix="/api/character", tags=["Creation"])

#Take a set of character variables and ask CharacterRepository to write that character to the database
@router.post("/create", response_model=CreateResponse)
async def createChar(character: CreateRequest) -> CreateResponse:
    try:
        newChar = Character(name=character.name, gender=character.gender, 
                        charClass=character.charClass, ancestry=character.ancestry, 
                        background=character.background)

        CharacterRepository.writeCharacter(newChar)
        return CreateResponse(success=True)

    except Exception as e:
        #print(f"Character_controller.py/createChar error: {e}")
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/create: {e}")

#ask CharacterRepository to return the number of characters in the database
@router.post("/count", response_model=CountResponse)
async def countChar(request: CountRequest) -> CountResponse:
    try:
        count = CharacterRepository.getCharCount()
        return CountResponse(charCount=count, success=True)
    except Exception as e:
        print(f"Character_controller.py/countChar error: {e}")
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/count: {e}")

#take int n and return the nth character in the database
@router.post("/getbynum", response_model=GetByNumberResponse)
async def getByNumber(request: GetByNumberRequest) -> GetByNumberResponse:
    try:
        #print(f"DEBUG: Received read request for character number {request.number}")
        newChar = CharacterRepository.readCharacterByNumber(request.number)
        if newChar is None:
            print(f"DEBUG: Character {request.number} not found")
            raise HTTPException(status_code=404, detail="character not found")

        #print(f"DEBUG: Found character {request.number}")
        return GetByNumberResponse(name=newChar.name, gender=newChar.gender, charClass=newChar.charClass, ancestry=newChar.ancestry, background=newChar.background, success=True)

    except Exception as e:
        #print(f"Character_controller.py/getbynum error: {e}")
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/getbynum: {e}")