import hashlib
import datetime
import jwt
from repositories.user_repository import UserRepository

#key and algorithm
SECRET_KEY = "This is my secret key, please don't steal it."
ALGORITHM = "HS256"

class LoginService:
    @staticmethod
    def get_login_token(username: str, password: str) -> str:
        try:
            #get user account by username from loginrepo
            user = UserRepository.getUser(username)
            if not user:
                raise Exception("User not  found")

            #check that credentials match
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print(hashed_password)
            print(user.password_hash)

            if user.password_hash != hashed_password:
                raise Exception("Invalid credentials")

            #create jwt with secret key
            user_payload = {
                "username": user.username,
                "name": user.name
            }

            expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours = 1)
            token_payload = {
                "sub": user.username,
                "exp": expiration_time,
                "user": user_payload
            }
            token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)
            return token
        except Exception as e:
            print(e)
            raise