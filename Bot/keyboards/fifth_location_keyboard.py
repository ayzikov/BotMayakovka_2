# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


async def fifth_location_keyboard():
    '''
    Клавиатура 5-ой локации
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Осмотреть двор'),
            KeyboardButton(text='Юбилеить')],

            [KeyboardButton(text='Дальше')],

            [KeyboardButton(text='Завершить прогулку')]
        ],
        resize_keyboard=True)

    return markup