
class MissingEnvVarError(Exception):
    """Excepción personalizada para variables de entorno faltantes."""
    def __init__(self, var_name):
        super().__init__(f"Falta la variable de entorno requerida: {var_name}")
        self.var_name = var_name