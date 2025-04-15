from dependency_injector import containers, providers
from repositories.user_repository import UserRepository
from services.login_service import LoginService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["controllers.login_controller", "controllers.character_controller"])

    # Import DatabaseFactory locally within the provider to avoid circular import
    db_factory = providers.Singleton(lambda: __import__('db.db').DatabaseFactory())

    user_repository = providers.Factory(
        UserRepository,
        db=db_factory
    )

    login_service = providers.Factory(
        LoginService,
        user_repository=user_repository
    )