# отдельные импорты


# импорты aiogram
from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardMarkup



async def main_menu_keyboard():
    '''
    Клавиатура главного меню
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Прогуляться по городу'),
            KeyboardButton(text='О проекте')],

            [KeyboardButton(text='Главное меню')]
        ],
        resize_keyboard=True)

    return markup