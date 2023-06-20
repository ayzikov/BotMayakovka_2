# файлы проекта
from keyboards.second_lvl_keyboards import walk_keyboard, about_project_keyboard

# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Прогуляться по городу'
@router.message(Text(text='Прогуляться по городу'))
async def walk_handler(message: Message, state: FSMContext):

    # записываем в ФСМ состояние что пользователь сейчас находится на нулевой локации
    await state.update_data(location_number=0)

    # получам клавиатуру
    markup = await walk_keyboard()

    text = "Отлично! Давайте прогуляемся по маршруту «Маяковский в Петрограде».\
    Мы посмотрим на места, в которых поэт бывал в 1912—1919 годах: артистические кафе, выставочные залы, \
гостиницы, квартиры друзей и соратников.\
    \n\nПолный маршрут: \
    \n-13 объектов \
    \n-7 километров \
    \n-3 часа.\
    \n\nНачало маршрута: улица Пушкинская, дом 20"

    await message.answer(text=text, reply_markup=markup)
    await message.answer_location(latitude=59.937607, longitude=30.348447)


# обработка кнопки 'О проекте'
@router.message(Text(text='О проекте'))
async def about_project_handler(message: Message):
    # получам клавиатуру
    markup = await about_project_keyboard()

    await message.answer(text='О проекте', reply_markup=markup)