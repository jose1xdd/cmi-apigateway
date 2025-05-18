from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    password: str
    personaId: str

class Usuario(UsuarioBase):
    personaId: str
    
    class Config:
        orm_mode = True