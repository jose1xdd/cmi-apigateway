from typing import Dict, Optional


class IClientCenso:
    def generar_censo(self, payload: dict, headers: Optional[Dict[str, str]] = None):
        
        raise NotImplementedError

    def listar_procesos(self, params: dict, headers: Optional[Dict[str, str]] = None):
        raise NotImplementedError

    def exportar_censo(self, censo_proceso_id: int, headers: Optional[Dict[str, str]] = None):
        raise NotImplementedError