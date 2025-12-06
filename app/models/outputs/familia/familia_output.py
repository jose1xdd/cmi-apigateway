from pydantic import BaseModel
from typing import Optional
from app.models.inputs.familia.familia_create import EnumEstadoFamilia
from app.models.outputs.persona.persona_output import PersonaOut


from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.outputs.persona.persona_output import PersonaOut


class FamiliaOut(BaseModel):
    id: int
    representanteId: Optional[str]
    fechaCreacion: Optional[datetime]   # ← Nuevo campo
    representante: Optional[PersonaOut] = None

    class Config:
        from_attributes = True
        exclude_none = True


class FamiliaDataLeader(BaseModel):
    id: int
    lider_nombre: str
    lider_apellido: str
    cedula: str
    parcialidad: Optional[str]
    miembros: int
    fechaCreacion: Optional[datetime]   # ← Nuevo campo

    class Config:
        from_attributes = True
        exclude_none = True


class FamiliaResumenOut(BaseModel):
    id: int
    lider_familia: Optional[str]
    parcialidad: Optional[str]
    total_miembros: int
    miembros_activos: int
    defunciones: int
    fechaCreacion: Optional[datetime]   # ← Nuevo campo

    class Config:
        from_attributes = True


class ReunionesPorEstado(BaseModel):
    programadas: int
    en_curso: int
    cerradas: int
