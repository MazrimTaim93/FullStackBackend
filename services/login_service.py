import hashlib
import datetime
import jwt
from config import settings
from repositories.user_repository import UserRepository


class LoginService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    @staticmethod # Decode token
    def verify_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")

    def get_login_token(self, username: str, password: str) -> str:
        try:
            #get user account by username from loginrepo
            user = self.user_repository.get_user_by_username(username)
            if not user:
                raise Exception("User not  found")

            #check that credentials match
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

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
            raise Exception(f"Login failed: {str(e)}")