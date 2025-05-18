from sqlalchemy import select, update, delete
from typing import TypeVar, Optional, List

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository

T = TypeVar('T', bound=BaseModel)
ID = TypeVar('ID')

class BaseRepository(IBaseRepository[T, ID]):
    def __init__(self, model):
        self.model = model
    
    async def get(self, db: AsyncSession, id: ID) -> Optional[T]:
        result = await db.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalars().first()
    
    async def get_all(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[T]:
        result = await db.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()
    
    async def create(self, db: AsyncSession, obj_in: T) -> T:
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        await db.flush()
        return db_obj
    
    async def update(self, db: AsyncSession, id: ID, obj_in: T) -> Optional[T]:
        await db.execute(
            update(self.model)
            .where(self.model.id == id)
            .values(**obj_in.dict(exclude_unset=True))
        )
        return await self.get(db, id)
    
    async def delete(self, db: AsyncSession, id: ID) -> bool:
        result = await db.execute(
            delete(self.model).where(self.model.id == id)
        )
        return result.rowcount > 0