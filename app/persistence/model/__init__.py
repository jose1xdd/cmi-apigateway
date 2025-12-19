# Importar Base primero
from app.config.database import Base

# Importar modelos en orden de dependencia
from app.persistence.model.parcialidad import Parcialidad
from app.persistence.model.persona import Persona
from app.persistence.model.familia import Familia
from app.persistence.model.miembro_familia import MiembroFamilia
from app.persistence.model.usuario import Usuario

# Exportar todo
__all__ = ['Base', 'Parcialidad', 'Persona', 'Familia', 'MiembroFamilia', 'Usuario']
