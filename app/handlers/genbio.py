from aiogram.dispatcher.router import Router
from aiogram.types.message import Message
from aiogram.fsm.context import FSMContext
from aiogram import F
from app.states import BioState
from database.models.user import User
from yandexgpt import generate_bio


router = Router()


@router.message(F.text == 'Генерация биографии')
async def _(msg: Message, state: FSMContext):
    user = await User.get(msg.from_user.id)

    if user.attempts < 1:
        await msg.answer('У вас закончились бесплатные попыточки.')
        return

    user.attempts -= 1
    await user.update()
    await state.set_state(BioState.name)
    await msg.answer('(1/4) Укажите имя персонажа.')


@router.message(BioState.name)
async def _(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(BioState.age)
    await msg.answer('(2/4) Укажите возраст персонажа.')


@router.message(BioState.age)
async def _(msg: Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await state.set_state(BioState.city)
    await msg.answer('(3/4) Укажите город в котором проживает персонаж.')


@router.message(BioState.city)
async def _(msg: Message, state: FSMContext):
    await state.update_data(city=msg.text)
    await state.set_state(BioState.current_job)
    await msg.answer('(4/4) Укажите текущую работу персонажа.')


@router.message(BioState.current_job)
async def _(msg: Message, state: FSMContext):
    await state.update_data(current_job=msg.text)
    await msg.answer('Биография генерируется, ожидайте.')
    bio = await generate_bio(await state.get_data())
    await msg.answer(bio)
