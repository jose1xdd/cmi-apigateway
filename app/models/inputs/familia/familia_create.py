from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class EnumEstadoFamilia(str, Enum):
    ACTIVA = "ACTIVA"
    INACTIVA = "INACTIVA"
    
class FamiliaCreate(BaseModel):
    """
    Modelo de entrada para crear una Familia.
    """
    idFamilia: Optional[int] = Field(default=None, description="ID de la familia (opcional, se puede asignar manualmente)")
    representanteId: Optional[str] = Field(default=None, description="ID de la persona líder o representante de la familia")
    estado: Optional[EnumEstadoFamilia] = Field(default=EnumEstadoFamilia.ACTIVA, description="Estado de la familia (ACTIVA/INACTIVA)")

    class Config:
        from_attributes = True
        exclude_none = True