# отдельные импорты


# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup



async def location_keyboard(additionally_button: str):
    '''
    Клавиатура локации
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Подробное описание'),
            KeyboardButton(text='Аудиогид')],

            [KeyboardButton(text=additionally_button),
             KeyboardButton(text='Дальше')],

            [KeyboardButton(text='Завершить прогулку')]
        ],
        resize_keyboard=True)

    return markup


async def location_keyboard_without_next_button(additionally_button: str):
    '''
    Клавиатура для последней локации
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Подробное описание'),
            KeyboardButton(text='Аудиогид')],

            [KeyboardButton(text=additionally_button)],

            [KeyboardButton(text='Завершить прогулку')]
        ],
        resize_keyboard=True)

    return markup