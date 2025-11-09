from fastapi import APIRouter, Depends, Body, Query
from fastapi.responses import JSONResponse
from app.ioc.container import get_censo_manager
from app.models.inputs.censo.censo import CensoGenerateIn
from app.services.censo_manager import CensoManager

censo_router = APIRouter(tags=["Censo"])

@censo_router.post("/generar", summary="Generar censo anual")
def generar_censo(
    body: CensoGenerateIn = Body(...),
    manager: CensoManager= Depends(get_censo_manager)
):
    data, status_code = manager.generar_censo(body.model_dump())
    return JSONResponse(content=data, status_code=status_code)


@censo_router.get("/procesos", summary="Listar procesos de censos")
def listar_procesos(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    anio: int | None = Query(None),
    estado: str | None = Query(None),
    manager: CensoManager= Depends(get_censo_manager)
):
    params = {"page": page, "page_size": page_size, "anio": anio, "estado": estado}
    data, status_code = manager.listar_procesos(params)
    return JSONResponse(content=data, status_code=status_code)


@censo_router.get("/exportar/{censo_proceso_id}", summary="Exportar censo a Excel")
def exportar_censo(censo_proceso_id: int, manager: CensoManager= Depends(get_censo_manager)):
    return manager.exportar_censo(censo_proceso_id)
