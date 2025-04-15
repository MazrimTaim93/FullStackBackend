from dependency_injector import containers, providers
from h11 import Data
from db.db import DatabaseFactory
from repositories.user_repository import UserRepository
from services.login_service import LoginService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["controllers.login_controller", "controllers.character_controller"])
    db_factory = providers.Singleton(DatabaseFactory)

    user_repository = providers.Factory(
        UserRepository,
        db=db_factory
    )

    login_service = providers.Factory(
        LoginService,
        user_repository=user_repository
    )