import logging
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from sqlalchemy.orm import Session
from app.client.ms_gestion_reuniones.asistencia.impl.client_asistencia import ClientAsistencia
from app.client.ms_gestion_reuniones.reunion.impl.gestion_reuniones import ClientReunion
from app.client.ms_gestion_usuarios.familia.impl.client_familia import ClientFamilia
from app.client.ms_gestion_usuarios.parcialidad.impl.client_parcialidad import ClientParcialidad
from app.client.ms_gestion_usuarios.personas.impl.client_personas import ClientPersonas
from app.client.ms_index.impl.client_index import ClientIndex
from app.client.ms_reportes.censo.impl.client_censo import ClientCenso
from app.client.ms_reportes.reportes.impl.client_reportes import ClientReportes
from app.config.database import get_db
from app.middlewares.middleware_auth import MiddlewarAuth
from app.persistence.repository.persona_repository.interface.interface_persona_repository import IPersonaRepository
from app.persistence.repository.recovery_code_repository.interface.interface_recovery_code_repository import IRecoveryCodeRepository
from app.persistence.repository.repository_factory import RepositoryFactory
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.asistencia_manager import AsistenciaManager
from app.services.censo_manager import CensoManager
from app.services.email_service.impl.email_service import EmailService
from app.services.familia_manager import FamiliaManager
from app.services.hashing_service.impl.hashing_service import HashingService
from app.services.index_manager import IndexManager
from app.services.jwt_service.impl.jwt_service import JwtService
from app.services.parcialidad_manager import ParcialidadManager
from app.services.persona_manager import PersonaManager
from app.services.reporte_manager import ReporteManager
from app.services.reunion_manager import ReunionManager
from app.services.user_manager import UserManager
from app.utils.enviroment import settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.ioc.container",
                 "app.utils.decorators.role_check_decorator"])

    logger = providers.Singleton(logging.getLogger, __name__)

    hashing_service = providers.Factory(
        HashingService
    )

    jwt_service = providers.Factory(
        JwtService,
        access_expires_minutes=settings.access_expires_minutes,
        refresh_expires_days=settings.refresh_expires_days,
        algorithm=settings.algorithm,
        secret_key=settings.secret_key
    )

    email_service = providers.Factory(
        EmailService,
        logger=logger,
        smtp_server=settings.smtp_server,
        smtp_port=settings.smtp_port,
        smtp_password=settings.smtp_password,
        smtp_email=settings.smtp_email
    )

    client_personas = providers.Factory(
        ClientPersonas,
        url=settings.ms_gestion_usuarios_url
    )

    client_familia = providers.Factory(
        ClientFamilia,
        url=settings.ms_gestion_usuarios_url
    )

    client_parcialidad = providers.Factory(
        ClientParcialidad,
        url=settings.ms_gestion_usuarios_url
    )
    client_index = providers.Factory(
        ClientIndex,
        url=settings.ms_index_url
    )

    client_reportes = providers.Factory(
        ClientReportes,
        url=settings.ms_reportes_url
    )

    client_censo = providers.Factory(
        ClientCenso,
        url=settings.ms_reportes_url
    )

    client_reunion = providers.Factory(
        ClientReunion,
        url=settings.ms_gestion_reuniones
    )
    client_asistencia = providers.Factory(
        ClientAsistencia,
        url=settings.ms_gestion_reuniones  # asegúrate de tener esta var en settings
    )

    middleware_auth = providers.Factory(
        MiddlewarAuth,
        jwt_service=jwt_service,
        hashing_service=hashing_service,
        logger=logger
    )


@inject
def get_user_manager(
    db: Session = Depends(get_db),
    logger: logging.Logger = Depends(Provide[Container.logger]),
    jwt_service=Depends(Provide[Container.jwt_service]),
    hashing_service=Depends(Provide[Container.hashing_service]),
    email_service=Depends(Provide[Container.email_service]),
) -> UserManager:
    factory = RepositoryFactory(db=db)

    return UserManager(
        logger=logger,
        usuario_repository=factory.get_repository(IUsuarioRepository),
        code_repository=factory.get_repository(IRecoveryCodeRepository),
        persona_repository=factory.get_repository(IPersonaRepository),
        jwt_service=jwt_service,
        hashing_service=hashing_service,
        email_service=email_service,
    )


@inject
def get_persona_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_personas=Depends(Provide[Container.client_personas]),
) -> PersonaManager:
    return PersonaManager(client_personas, logger)


@inject
def get_familia_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_familia=Depends(Provide[Container.client_familia]),
) -> FamiliaManager:
    return FamiliaManager(client_familia, logger)


@inject
def get_parcialidad_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_parcialidad=Depends(Provide[Container.client_parcialidad])
) -> ParcialidadManager:
    return ParcialidadManager(client_parcialidad, logger)


@inject
def get_index_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_index=Depends(Provide[Container.client_index])
) -> IndexManager:
    return IndexManager(client_index, logger)


@inject
def get_reportes_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_reportes=Depends(Provide[Container.client_reportes])
) -> ReporteManager:
    return ReporteManager(client_reportes, logger)


@inject
def get_reunion_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_reunion=Depends(Provide[Container.client_reunion])
) -> ReunionManager:
    return ReunionManager(client_reunion, logger)


@inject
def get_asistencia_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_asistencia=Depends(Provide[Container.client_asistencia]),
) -> AsistenciaManager:
    return AsistenciaManager(client_asistencia, logger)


@inject
def get_censo_manager(
    logger: logging.Logger = Depends(Provide[Container.logger]),
    client_censo=Depends(Provide[Container.client_censo])
) -> CensoManager:
    return CensoManager(client_censo=client_censo, logger=logger)
