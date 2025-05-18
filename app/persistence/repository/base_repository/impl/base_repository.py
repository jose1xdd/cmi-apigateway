from typing import Generic, TypeVar, Optional, List, Type
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository

T = TypeVar('T', bound=BaseModel)
M = TypeVar('M')  # Tipo para el modelo SQLAlchemy
ID = TypeVar('ID')

class BaseRepository(IBaseRepository[T, ID], Generic[T, M, ID]):
    def __init__(self, model: Type[M], db: Session):
        self.model = model
        self.db = db
    
    def get(self, id: ID) -> Optional[M]:
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[M]:
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self, obj_in: T) -> M:
        # Convertimos el modelo Pydantic a un diccionario
        # y filtramos solo los campos válidos para el modelo SQLAlchemy 
        obj_data = obj_in.dict()
        
        # Creamos la instancia del modelo SQLAlchemy
        db_obj = self.model(**obj_data)
        
        # La añadimos a la sesión
        self.db.add(db_obj)
        
        # Hacemos flush para obtener el ID pero no commit
        # El commit se hará automáticamente en get_db()
        self.db.flush()
        
        # Devolvemos el objeto creado
        return db_obj
    
    def update(self, id: ID, obj_in: T) -> Optional[M]:
        # Obtenemos el objeto existente
        db_obj = self.get(id)
        if db_obj is None:
            return None
            
        # Actualizamos los campos que vienen en obj_in
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            if hasattr(db_obj, key):
                setattr(db_obj, key, value)
        
        # La sesión detectará los cambios automáticamente
        self.db.flush()  # Para asegurarnos de que se apliquen los cambios
        
        return db_obj
    
    def delete(self, id: ID) -> bool:
        result = self.db.query(self.model).filter(self.model.id == id).delete()
        self.db.flush()  # Aplicamos los cambios sin hacer commit
        return result > 0