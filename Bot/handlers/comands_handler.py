# файлы проекта
from BotMayakovka_2.Bot.keyboards.main_menu_keyboard import main_menu_keyboard

# импорты aiogram
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка команды /start
@router.message(Command(commands=['start']))
async def hello(message: Message):
    # получам клавиатуру
    markup = await main_menu_keyboard()

    await message.answer(text='Приветствие', reply_markup=markup)