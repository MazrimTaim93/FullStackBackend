from pydantic import BaseModel

from models.character_model import Character

class CreateRequest(BaseModel):
    name: str
    gender: str
    charClass: str
    ancestry: str
    background: str

class CreateResponse(BaseModel):
    success: bool

class GetByNameRequest(BaseModel):
    name: str

class GetByNameResponse(BaseModel):
    name: str
    gender: str
    charClass: str
    ancestry: str
    background: str
    success: bool

class GetByNumberRequest(BaseModel):
    number: int

class GetByNumberResponse(BaseModel):
    name: str
    gender: str
    charClass: str
    ancestry: str
    background: str
    success: bool

class CountRequest(BaseModel):
    filler: str

class CountResponse(BaseModel):
    charCount: int
    success: bool