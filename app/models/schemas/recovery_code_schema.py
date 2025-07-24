from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


class CodigoRecuperacionBase(BaseModel):
    codigo: str
    emailUsuario: EmailStr
    estado: bool


class CodigoRecuperacionCreate(CodigoRecuperacionBase):
    pass  # hereda todo lo necesario para crear


class CodigoRecuperacionRead(CodigoRecuperacionBase):
    id: int
    estado: bool

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )
