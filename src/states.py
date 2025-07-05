from aiogram.fsm.state import StatesGroup, State

class States(StatesGroup):
    guitar_name = State()
    min_price = State()
    max_price = State()
    site = State()

