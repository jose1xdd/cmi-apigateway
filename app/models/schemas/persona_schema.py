from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional
from app.persistence.model.enum import EnumDocumento, EnumSexo, EnumParentesco, EnumEscolaridad

class PersonaBase(BaseModel):
    tipoDocumento: EnumDocumento
    nombre: str
    apellido: str
    fechaNacimiento: date
    parentesco: EnumParentesco
    sexo: EnumSexo
    profesion: Optional[str] = None
    escolaridad: EnumEscolaridad
    integrantes: int
    direccion: str
    telefono: str
    idFamilia: int
    idParcialidad: int

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: str
    model_config = ConfigDict(
        from_attributes=True,  # Reemplazo de orm_mode en Pydantic V2
        populate_by_name=True  # Permite usar alias y nombres de campo directamente
    )