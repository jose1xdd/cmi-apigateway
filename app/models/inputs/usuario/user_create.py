from pydantic import BaseModel, Field, EmailStr, field_validator
from enum import Enum

from app.utils.exceptions_handlers.models.error_response import AppException


class EnumRol(str, Enum):
    usuario = "usuario"
    admin = "admin"


class UsuarioCreate(BaseModel):
    email: str = Field(..., description="Correo del usuario")
    personaId: str = Field(..., description="UUID de la persona asociada")
    rol: EnumRol = Field(..., description="Rol del usuario")
