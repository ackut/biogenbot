import time
from sqlalchemy import select, update
from sqlalchemy.types import String, BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import Base, async_session
from config import nid


class UserModel(Base):
    __tablename__ = 'users'

    nid: Mapped[str] = mapped_column(primary_key=True, default=nid)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    attempts: Mapped[int] = mapped_column(default=3)
    created_at: Mapped[float] = mapped_column(default=time.time)


class User:
    def __init__(self, model: UserModel) -> None:
        self.nid = model.nid
        self.telegram_id = model.telegram_id
        self.attempts = model.attempts
        self.created_at = model.created_at

    @classmethod
    async def get(cls, telegram_id: BigInteger) -> "User":
        async with async_session() as session:
            model = await session.scalar(
                select(UserModel).where(UserModel.telegram_id == telegram_id)
            )

            return cls(model) if model else None

    @classmethod
    async def create(cls, telegram_id: BigInteger) -> "User":
        async with async_session() as session:
            model = UserModel(telegram_id=telegram_id)
            session.add(model)
            await session.commit()

            return cls(model)

    async def update(self) -> "User":
        async with async_session() as session:
            model = await session.get(UserModel, self.nid)
            model.attempts = self.attempts
            await session.commit()

            return self