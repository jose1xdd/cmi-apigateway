from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T', bound=BaseModel)  # Tipo del modelo Pydantic
ID = TypeVar('ID')                 # Tipo del ID (puede ser str, int, etc.)

class IBaseRepository(ABC, Generic[T, ID]):
    @abstractmethod
    async def get(self, db: AsyncSession, id: ID) -> Optional[T]:
        pass
    
    @abstractmethod
    async def get_all(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[T]:
        pass
    
    @abstractmethod
    async def create(self, db: AsyncSession, obj_in: T) -> T:
        pass
    
    @abstractmethod
    async def update(self, db: AsyncSession, id: ID, obj_in: T) -> Optional[T]:
        pass
    
    @abstractmethod
    async def delete(self, db: AsyncSession, id: ID) -> bool:
        pass