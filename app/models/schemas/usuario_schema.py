from pydantic import BaseModel, ConfigDict, EmailStr

class UsuarioBase(BaseModel):
    email: EmailStr
    rol: str

class UsuarioCreate(UsuarioBase):
    password: str
    personaId: str
    rol: str

class Usuario(UsuarioBase):
    personaId: str
    
    class Config:
       model_config = ConfigDict(
        from_attributes=True,  # Reemplazo de orm_mode en Pydantic V2
        populate_by_name=True  # Permite usar alias y nombres de campo directamente
    )