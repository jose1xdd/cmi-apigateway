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

    def _commit_with_handling(self):
        try:
            self.db.flush()
            self.db.commit()
        except:
            self.db.rollback()
            raise

    def _commit_and_refresh(self, db_obj: M):
        try:
            self.db.flush()
            self.db.commit()
            self.db.refresh(db_obj)
        except:
            self.db.rollback()
            raise

    def get(self, id: ID) -> Optional[M]:
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[M]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, obj_in: T) -> M:
        obj_data = obj_in.dict()
        db_obj = self.model(**obj_data)
        self.db.add(db_obj)
        self._commit_and_refresh(db_obj)
        return db_obj

    def update(self, id: ID, obj_in: T) -> Optional[M]:
        db_obj = self.get(id)
        if db_obj is None:
            return None
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            if hasattr(db_obj, key):
                setattr(db_obj, key, value)
        self._commit_and_refresh(db_obj)
        return db_obj

    def delete(self, id: ID) -> bool:
        db_obj = self.get(id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self._commit_with_handling()
        return True
