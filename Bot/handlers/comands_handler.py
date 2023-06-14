# импорты aiogram
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

# роутер (сын диспетчера)
router = Router()

# обработка команды /start
@router.message(Command(commands=['start']))
async def hello(message: Message):
    await message.answer(text='Приветствие')