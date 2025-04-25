from dependency_injector import containers, providers
from h11 import Data
from db.db import DatabaseFactory
from repositories import character_repository
from repositories.user_repository import UserRepository
from services.login_service import LoginService
from services.character_service import CharacterService
from repositories.character_repository import CharacterRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["controllers.login_controller", "controllers.character_controller"])
    db_factory = providers.Singleton(DatabaseFactory)
    character_repository = providers.Factory(CharacterRepository)

    user_repository = providers.Factory(
        UserRepository,
        db=db_factory
    )

    login_service = providers.Factory(
        LoginService,
        user_repository=user_repository
    )

    character_repository = providers.Factory(
        CharacterRepository,
        db=db_factory
    )

    character_service = providers.Factory(
        CharacterService,
        character_repository=character_repository
    )