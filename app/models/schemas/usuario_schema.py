from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str
    personaId: str

class Usuario(UsuarioBase):
    personaId: str
    
    class Config:
        orm_mode = True