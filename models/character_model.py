from sqlalchemy import Column, Integer, String
from models.base_model import Base

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    gender = Column(String(50), nullable=False)
    charClass = Column(String(50), nullable=False)
    ancestry = Column(String(50), nullable=False)
    background = Column(String(50), nullable=False)

    def __init__(self, name: str, gender: str, charClass: str, ancestry: str, background: str):
        self.name = name
        self.gender = gender
        self.charClass = charClass
        self.ancestry = ancestry
        self.background = background