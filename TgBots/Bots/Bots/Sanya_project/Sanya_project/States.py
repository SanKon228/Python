from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    food_state = State()
    size_state = State()
    geo = State()
