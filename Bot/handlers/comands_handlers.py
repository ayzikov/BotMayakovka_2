# файлы проекта
from keyboards.main_menu_keyboard import main_menu_keyboard
from crud.add_user import add_user

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

    await message.answer(text='В 1912 году девятнадцатилетний Владимир Маяковский впервые приехал в Санкт-Петербург. Чтобы пройтись вместе с поэтом по Петербургу, Петрограду и Ленинграду, нажмите на кнопку «Прогулка по городу». Не забудьте взять наушники, чтобы послушать аудиогид.\n\n'
                              'Хотите больше узнать о проекте и ближе познакомиться с библиотекой имени Маяковского — нажимайте на кнопку «О проекте»',
                         reply_markup=markup)

    # добавляем пользователя в БД
    user_tg_id = message.from_user.id
    try:
        full_name = message.from_user.full_name
    except:
        full_name = ''

    try:
        username = message.from_user.username
    except:
        username = ''


    await add_user(user_tg_id=user_tg_id,
                   full_name=full_name,
                   username=username)


# обработка команды /menu ,кнопок 'Главное меню' и 'Завершить прогулку'
@router.message(Command(commands=['menu']))
@router.message(Text(text='Главное меню'))
@router.message(Text(text='Завершить прогулку'))
async def main_menu_handler(message: Message):
    # получам клавиатуру
    markup = await main_menu_keyboard()

    await message.answer(text='Главное меню', reply_markup=markup)