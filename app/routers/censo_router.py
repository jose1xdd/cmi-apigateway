from fastapi import APIRouter, Depends, Body, Query, status
from fastapi.responses import JSONResponse
from app.ioc.container import get_censo_manager
from app.models.inputs.censo.censo import CensoGenerateIn
from app.services.censo_manager import CensoManager
from app.utils.constans import BEARER_SCHEME
from app.utils.decorators.role_check_decorator import require_roles

censo_router = APIRouter(tags=["Censo"])


@censo_router.post("/generar",
                   summary="Generar censo anual",
                   status_code=status.HTTP_200_OK,
                   dependencies=[Depends(BEARER_SCHEME)],)
def generar_censo(
    body: CensoGenerateIn = Body(...),
    _: dict = Depends(require_roles([])),
    manager: CensoManager = Depends(get_censo_manager)

):
    data, status_code = manager.generar_censo(body.model_dump())
    return JSONResponse(content=data, status_code=status_code)


@censo_router.get("/procesos",
                  summary="Listar procesos de censos",
                  status_code=status.HTTP_200_OK,
                  dependencies=[Depends(BEARER_SCHEME)],)
def listar_procesos(
    _: dict = Depends(require_roles([])),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    anio: int | None = Query(None),
    estado: str | None = Query(None),
    manager: CensoManager = Depends(get_censo_manager)
):
    params = {"page": page, "page_size": page_size,
              "anio": anio, "estado": estado}
    data, status_code = manager.listar_procesos(params)
    return JSONResponse(content=data, status_code=status_code)


@censo_router.get("/exportar/{censo_proceso_id}", summary="Exportar censo a Excel")
def exportar_censo(censo_proceso_id: int, manager: CensoManager = Depends(get_censo_manager)):
    return manager.exportar_censo(censo_proceso_id)
