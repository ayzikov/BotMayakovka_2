# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup



async def admin_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='Статистика')],
            [KeyboardButton(text='Главное меню')]
        ],
        resize_keyboard=True
    )

    return markup