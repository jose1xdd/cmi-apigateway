from typing import Any, Dict, List
from databases import Database
from sqlalchemy import Table

from app.utils.config_loader.config_loader import ConfigLoader


class BaseRepository:
    def __init__(self, table: Table):
        self.db: Database = Database(ConfigLoader().get('DATABASE_URL'))
        self.table = table
        
    async def get_all(self) -> List[dict]:
        return await self.db.fetch_all(self.table.select())

    async def get_by_id(self, id: int) -> dict:
        query = self.table.select().where(self.table.c.id == id)
        return await self.db.fetch_one(query)

    async def delete(self, id: int) -> None:
        query = self.table.delete().where(self.table.c.id == id)
        await self.db.execute(query)

    async def save(self, data: Dict[str, Any]) -> int:

        query = self.table.insert().values(**data)
        return await self.db.execute(query)

    async def update(self, id: int, data: Dict[str, Any]) -> None:

        query = self.table.update().where(self.table.c.id == id).values(**data)
        await self.db.execute(query)
