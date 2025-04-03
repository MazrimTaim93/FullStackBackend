import json
from models.user_model import User

class UserRepository:
    @staticmethod
    def getUser(username: str) -> User|None:
        try:
            with open("./db/users.json", "r") as file:
                data = json.load(file)
                for user in data["users"]:
                    if user["username"] == username:
                        return User(user["username"], user["name"], user["password_hash"])
        except FileNotFoundError:
            raise Exception("User file not found")

        return None