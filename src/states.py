from aiogram.filters.state import StatesGroup, State


class UserData(StatesGroup):
    date_ = State()
    time_ = State()
    city = State()
    country = State()