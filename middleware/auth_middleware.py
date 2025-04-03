from fastapi import FastAPI

app = FastAPI()

class AuthMiddleware(BaseHTTPMiddleware):
	def __init__(self, app:FastAPI):
		super().__init(app)

	#async def dispatch(self, request: Request, call_next):