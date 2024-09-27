from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine
)
import config as cfg


engine = create_async_engine(cfg.db_sqlite3.url)
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=cfg.db_sqlite3.expire_on_commit
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def create_base():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
