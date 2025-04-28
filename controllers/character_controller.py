from fastapi import Depends
from sqlalchemy.orm import Session
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, HTTPException
from models.character_model import Character
from containers import Container
from schemas import character_schema
from services import character_service
from services.character_service import CharacterService
from repositories.character_repository import CharacterRepository
from schemas.character_schema import CountRequest, CountResponse, CreateRequest, CreateResponse, GetByNumberRequest, GetByNumberResponse, GetAllCharsRequest, GetAllCharsResponse

router = APIRouter(prefix="/api/character", tags=["Character"])

#Take a set of character variables and ask CharacterRepository to write that character to the database
@router.post("/create", response_model=CreateResponse)
@inject
async def createChar(character: CreateRequest,
                     character_service: CharacterService = Depends(Provide[Container.character_service])) -> CreateResponse:
    try:
        print("DEBUG: character_controller.py received request to create character.")
        newChar = Character(name=character.name, gender=character.gender, 
                        charClass=character.charClass, ancestry=character.ancestry, 
                        background=character.background, might=character.might, 
                        dexterity=character.dexterity, intellect=character.intellect, 
                        charisma=character.charisma)

        character_service.writeCharacter(newChar)
        return CreateResponse(success=True)

    except Exception as e:
        print(f"Character_controller.py/createChar error: {e}")
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/create: {e}")

#ask CharacterRepository to return the number of characters in the database
@router.post("/count", response_model=CountResponse)
@inject
async def countChar(request: CountRequest, 
                    character_service: CharacterService = Depends(Provide[Container.character_service])) -> CountResponse:
    try:
        count = character_service.getCharCount()
        return CountResponse(charCount=count, success=True)
    except Exception as e:
        print(f"Character_controller.py/countChar error: {e}")
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/count: {e}")

#return all characters in the database
@router.post("/getallchars", response_model=GetAllCharsResponse)
@inject
async def getAllChars(request: GetAllCharsRequest, 
                    character_service: CharacterService = Depends(Provide[Container.character_service])) -> GetByNumberResponse:
    try:
        allChars = character_service.getAllChars();
        return GetAllCharsResponse()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/getallchars: {e}")

#take int n and return the nth character in the database
@router.post("/getbynum", response_model=GetByNumberResponse)
@inject
async def getByNumber(request: GetByNumberRequest, 
                    character_service: CharacterService = Depends(Provide[Container.character_service])) -> GetByNumberResponse:
    try:
        #print(f"DEBUG: Received read request for character number {request.number}")
        newChar = character_service.getByNumber(request.number)
        if newChar is None:
            print(f"DEBUG: Character {request.number} not found")
            raise HTTPException(status_code=404, detail="character not found")

        #print(f"DEBUG: Found character {request.number}")
        return GetByNumberResponse(name=newChar.name, gender=newChar.gender, charClass=newChar.charClass, ancestry=newChar.ancestry, background=newChar.background, might=newChar.might, dexterity=newChar.dexterity, intellect=newChar.intellect, charisma=newChar.charisma, fortitude=newChar.fortitude, reflex=newChar.reflex, will=newChar.will, success=True)

    except Exception as e:
        print(f"Character_controller.py/getbynum error: {e}")
        raise HTTPException(status_code=500, detail=f"Error in character_controller.py/getbynum: {e}")