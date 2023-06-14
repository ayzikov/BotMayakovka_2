# отдельные импорты


# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup



async def walk_keyboard():
    '''
    Клавиатура прогулки по городу
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Я на месте')],
            [KeyboardButton(text='Завершить прогулку')]
        ],
        resize_keyboard=True)

    return markup


async def about_project_keyboard():
    '''
    Клавиатура о проекте
    :return: markup
    '''
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Главное меню')]
        ],
        resize_keyboard=True)

    return markup