from aiogram.fsm.state import State, StatesGroup


class BotForm(StatesGroup):
    location = State()
    budget = State()
