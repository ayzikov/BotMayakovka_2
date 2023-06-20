# файлы проекта
from keyboards.main_menu_keyboard import main_menu_keyboard

# импорты aiogram
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка команды /start
@router.message(Command(commands=['start']))
async def welcome_handler(message: Message):
    # получам клавиатуру
    markup = await main_menu_keyboard()

    await message.answer(text='В 1912 году девятнадцатилетний Владимир Маяковский впервые приехал в Санкт-Петербург. ',
                         reply_markup=markup)


# обработка команды /menu ,кнопок 'Главное меню' и 'Завершить прогулку'
@router.message(Command(commands=['menu']))
@router.message(Text(text='Главное меню'))
@router.message(Text(text='Завершить прогулку'))
async def main_menu_handler(message: Message):
    # получам клавиатуру
    markup = await main_menu_keyboard()

    await message.answer(text='Главное меню', reply_markup=markup)