import json
from math import log
from h11 import Data
from containers import Container
from config import settings
from pydantic import BaseModel
from containers import Container
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from controllers import character_controller, login_controller
from middleware.api_gateway_middleware import ApiGatewayAuthMiddleware
from middleware.auth_middleware import AuthMiddleware
from fastapi.openapi.utils import get_openapi
from schemas.message_schema import MessageResponse

app = FastAPI()
container = Container()
app.container = container
container.wire(modules=["controllers.login_controller", "controllers.character_controller"])

app.add_middleware(AuthMiddleware)
if settings.app_env == "local":
    app.add_middleware(
        CORSMiddleware,
        allow_origins = settings.allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
if settings.app_env == "prod":
    app.add_middleware(ApiGatewayAuthMiddleware)

app.include_router(login_controller.router)
app.include_router(character_controller.router)

#print(f"DEBUG: Main.py is running.")

@app.get("/", response_model=MessageResponse)
def read_root():
    return {"message": "hello world"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description="CS3660 Backend Project",
        routes=app.routes
    )

    openapi_schema["openapi"] = "3.0.1"

    openapi_schema["paths"] = {
        path.rstrip("/") if path != "/" else path: data
        for path, data in openapi_schema["paths"].items() if path != ""
    }

    for schema_name, schema in openapi_schema["components"]["schemas"].items():
        if "properties" in schema:
            for field_name, field in schema["properties"].items():
                if "anyOf" in field:
                    field["type"] = "string"
                    field["nullable"] = True
                    del field["anyOf"]

    for path, methods in openapi_schema["paths"].items():
        for method, data in methods.items():
            if "operationId" in data:
                data["operationId"] = "".join(
                    word.capitalize() for word in data["operationId"].split("_")
                )

        """"
    "openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
    }

    for path, methods in openapi_schema["paths"].items():
        if path != "/api/login":  # Skip authentication for login endpoint
            for method in methods:
                methods[method]["security"] = [{"BearerAuth": []}]"
    """

    for schema_name, schema in openapi_schema["components"]["schemas"].items():
        if "type" not in schema:
            schema["type"] = "object"

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


