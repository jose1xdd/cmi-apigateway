from pydantic import BaseModel, EmailStr, Field
from enum import Enum


class EnumRol(str, Enum):
    usuario = "usuario"
    admin = "admin"


class UsuarioCreate(BaseModel):
    email: EmailStr = Field(..., max_length=100,
                            description="Correo del usuario")
    password: str = Field(..., min_length=8,
                          max_length=64,
                          description="Contraseña con mínimo 8 caracteres")
    personaId: str = Field(..., description="UUID de la persona asociada")
    rol: EnumRol = Field(..., description="Rol del usuario")
