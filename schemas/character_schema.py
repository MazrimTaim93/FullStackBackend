from pydantic import BaseModel
from typing import List
from models.character_model import Character

class CreateRequest(BaseModel):
    name: str
    gender: str
    charClass: str
    ancestry: str
    background: str
    might: int
    dexterity: int
    intellect: int
    charisma: int

class CreateResponse(BaseModel):
    success: bool

class GetByNumberRequest(BaseModel):
    number: int

class GetByNumberResponse(BaseModel):
    name: str
    number: int
    gender: str
    charClass: str
    ancestry: str
    background: str
    might: int
    dexterity: int
    intellect: int
    charisma: int
    fortitude: int
    reflex: int
    will: int
    success: bool

class CountRequest(BaseModel):
    filler: str

class CountResponse(BaseModel):
    charCount: int
    success: bool

class DeleteRequest(BaseModel):
    number: int

class DeleteResponse(BaseModel):
    success: bool

class GetAllResponse(BaseModel):
    ids: List[int]
