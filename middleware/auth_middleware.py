from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from config import settings
from services.login_service import LoginService

app = FastAPI()

class AuthMiddleware(BaseHTTPMiddleware):
	def __init__(self, app:FastAPI):
		super().__init__(app)

	async def dispatch(self, request: Request, call_next):
		#print(f"DEBUG: authMiddleWare running")
		PUBLIC_PATHS = {"/api/login", "/health", "/openapi.json", "/api/character/count"}
		if request.url.path in PUBLIC_PATHS:
			return await call_next(request)

		#print(f"DEBUG: request headers: {dict(request.headers)}")
		auth_header = request.headers.get("Authorization")
		#print(f"DEBUG: raw auth header: {auth_header}")
		if not auth_header or not auth_header.startswith("Bearer "):
			return JSONResponse(status_code=401, content={"detail": "invalid authorization token"})
		
		token = auth_header.split("Bearer ")[1]
		#print(f"DEBUG: token: ", token)
		try:
			LoginService.verify_token(token)
		except Exception as e:
			return JSONResponse(status_code=401, content={"detail": str(e)})

		return await call_next(request)