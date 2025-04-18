from math import log
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from controllers import character_controller, login_controller
import json

app = FastAPI()

#app.add_middleware(AuthMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(login_controller.router)
app.include_router(character_controller.router)

@app.get("/")
def read_root():
    return {"message": "hello world"}

def verify_login(username: str, password: str) -> bool:
    try:
        with open("./db/users.json") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    return True
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="User file not found")
    return False