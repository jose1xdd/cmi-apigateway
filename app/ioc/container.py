import logging
from dependency_injector import containers, providers
from app.config.database import get_db
from app.persistence.repository.repository_factory import RepositoryFactory
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.manager import Manager


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.routers.main_router"])

    db_session = providers.Resource(get_db)

    repository_factory = providers.Factory(
        RepositoryFactory,
        db=db_session,
    )

    usuario_repository = providers.Factory(
        lambda factory: factory.get_repository(IUsuarioRepository),
        factory=repository_factory
    )

    logger = providers.Singleton(logging.getLogger, __name__)

    manager = providers.Factory(
        Manager,
        logger=logger,
        usuario_repository=usuario_repository
    )