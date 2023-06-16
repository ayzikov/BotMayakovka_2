# отдельные импорты


# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup



async def location_keyboard():
    '''
    Клавиатура локации
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Подробное описание'),
            KeyboardButton(text='Аудиогид')],

            [KeyboardButton(text='Дополнительно'),
             KeyboardButton(text='Дальше')],

            [KeyboardButton(text='Назад')],
            [KeyboardButton(text='Завершить прогулку')]
        ],
        resize_keyboard=True)

    return markup
