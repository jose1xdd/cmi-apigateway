from typing import List
from pydantic import BaseModel

from app.models.outputs.asistencia.asistencia_out import PersonaAsistenciaOut
from app.models.outputs.familia.familia_output import FamiliaDataLeader, FamiliaOut
from app.models.outputs.parcialidad.parcialidad_output import ParcialidadOut
from app.models.outputs.persona.persona_output import PersonaFamiliaOut, PersonaOut
from app.models.outputs.publicacion.publicacion_out import PublicacionOut
from app.models.outputs.reunion.reunion_out import ReunionOut
from app.models.outputs.usuario.usuario_output import UsuarioOut


class PaginatedPersonas(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[PersonaOut]


class PaginatedFamilias(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[FamiliaOut]


class PaginatedParcialidad(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[ParcialidadOut]


class PaginatedUsuario(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[UsuarioOut]

class PaginatedPublicacion(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[PublicacionOut]

class PaginatedReunion(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[ReunionOut]

class PaginatedReunion(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[ReunionOut]

class PaginatedDataLeader(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[FamiliaDataLeader]

class PaginatedParcialidad(BaseModel):
    total_items: int
    current_page: int
    total_pages: int
    items: List[ParcialidadOut]

class PaginatedPersonasFamilia(BaseModel):
    total_items: int
    total_pages: int
    current_page: int
    items: List[PersonaFamiliaOut]

    class Config:
        from_attributes = True