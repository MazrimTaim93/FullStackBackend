from sqlalchemy import Column, Integer, String
from models.base_model import Base
from pydantic import BaseModel

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    gender = Column(String(50), nullable=False)
    charClass = Column(String(50), nullable=False)
    ancestry = Column(String(50), nullable=False)
    background = Column(String(50), nullable=False)
    might = Column(Integer, nullable=True)
    dexterity = Column(Integer, nullable=True)
    intellect = Column(Integer, nullable=True)
    charisma = Column(Integer, nullable=True)
    fortitude = Column(Integer, nullable=True)
    reflex = Column(Integer, nullable=True)
    will = Column(Integer, nullable=True)

    def __init__(self, name: str, gender: str, charClass: str, ancestry: str, background: str, might: int, dexterity: int, intellect: int, charisma: int):
        self.name = name
        self.gender = gender
        self.charClass = charClass
        self.ancestry = ancestry
        self.background = background
        self.might = might
        self.dexterity = dexterity
        self.intellect = intellect
        self.charisma = charisma
        match self.charClass.lower():
            case "fighter":
                self.fortitude = self.might + 3
                self.reflex = self.might + 3
                self.will = max(self.charisma, self.intellect) + 1
            case "rogue":
                self.fortitude = self.might + 1
                self.reflex = self.might + 5
                self.will = max(self.charisma, self.intellect) + 1
            case "cleric" | "wizard":
                self.fortitude = self.might + 1
                self.reflex = self.might + 1
                self.will = max(self.charisma, self.intellect) + 5
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ancestry": self.ancestry,
            "background": self.background,
            "charClass": self.charClass,
            "gender": self.gender,
            "might": self.might,
            "dexterity": self.dexterity,
            "intellect": self.intellect,
            "charisma": self.charisma,
            "fortitude": self.fortitude,
            "reflex": self.reflex,
            "will": self.will
        }
