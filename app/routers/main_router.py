from datetime import date
from fastapi import APIRouter

import logging

from pydantic import EmailStr

from app.config.database import get_db_session
from app.models.schemas.persona_schema import PersonaCreate
from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.model.enum import EnumDocumento, EnumEscolaridad, EnumParentesco, EnumSexo
from app.persistence.repository.repository_factory import RepositoryFactory
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger_printer = logging.getLogger(__name__)

main_router = APIRouter()

@main_router.get("/login")
async def login():
    usuario = UsuarioCreate(
    email=EmailStr("juan.perez@example.com"),
    password="secreto123",
    personaId="1144123456")
    logger_printer.info("manfredo godofredo")
    usuario_repo = RepositoryFactory.get_repository(IUsuarioRepository)
    usuario_repo.create(get_db_session(),usuario)
    return {}