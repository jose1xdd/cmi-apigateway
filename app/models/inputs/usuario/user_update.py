from pydantic import BaseModel, EmailStr
from typing import Optional
from app.persistence.model.enum import EnumRol


class UsuarioUpdate(BaseModel):
    email: Optional[EmailStr] = None