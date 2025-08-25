from pydantic import BaseModel, EmailStr
from typing import Optional
from app.persistence.model.enum import EnumRol

class UsuarioOut(BaseModel):
    email: EmailStr
    personaId: Optional[str]
    rol: EnumRol

    class Config:
        from_attributes = True  # Para mapear desde SQLAlchemy