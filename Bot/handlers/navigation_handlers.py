# файлы проекта
from BotMayakovka_2.Bot.keyboards.menu_for_location_keyboard import location_keyboard
from BotMayakovka_2.Bot.keyboards.second_lvl_keyboards import walk_keyboard

# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Я на месте'
@router.message(Text(text='Я на месте'))
async def in_place_handler(message: Message):
    # получам клавиатуру
    markup = await location_keyboard()

    await message.answer(text='Я на месте', reply_markup=markup)


# обработка кнопки 'Дальше'
@router.message(Text(text='Дальше'))
async def next_location_handler(message: Message):
    # получам клавиатуру
    markup = await walk_keyboard()

    await message.answer(text='Дальше', reply_markup=markup)