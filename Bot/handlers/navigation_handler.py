# файлы проекта
from BotMayakovka_2.Bot.keyboards.menu_for_location_keyboard import location_keyboard

# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Я на месте'
@router.message(Text(text='Я на месте'))
async def walk_handler(message: Message):
    # получам клавиатуру
    markup = await location_keyboard()

    await message.answer(text='Я на месте', reply_markup=markup)