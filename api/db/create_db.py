from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from ..settings import get_settings

settings = get_settings()
engine = create_async_engine(settings.DATABASE_URI, echo=False, future=True)  # noqa: WPS432, E501


async def create_db() -> None:
    """Create tables."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
