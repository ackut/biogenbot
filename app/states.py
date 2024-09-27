from aiogram.fsm.state import StatesGroup, State


class BioState(StatesGroup):
    name = State()
    age = State()
    city = State()
    current_job = State()
