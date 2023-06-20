from aiogram.fsm.state import StatesGroup, State

class AdminLogin(StatesGroup):
    password = State()