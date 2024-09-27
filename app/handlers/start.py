from aiogram.dispatcher.router import Router
from aiogram.filters.command import CommandStart
from aiogram.types.message import Message
from database.models.user import User
from app import keyboard as kb


router = Router()


@router.message(CommandStart())
async def _(msg: Message):
    user = await User.get(msg.from_user.id) or await User.create(msg.from_user.id)
    await msg.answer(
        text=f'Оставшиеся попытки: {user.attempts}',
        reply_markup=kb.main
    )
