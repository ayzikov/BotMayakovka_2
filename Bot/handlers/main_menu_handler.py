# файлы проекта
from BotMayakovka_2.Bot.keyboards.second_lvl_keyboards import walk_keyboard, about_project_keyboard

# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Прогуляться по городу'
@router.message(Text(text='Прогуляться по городу'))
async def walk_handler(message: Message):
    # получам клавиатуру
    markup = await walk_keyboard()

    await message.answer(text='Прогуляться по городу', reply_markup=markup)


# обработка кнопки 'О проекте'
@router.message(Text(text='О проекте'))
async def about_project_handler(message: Message):
    # получам клавиатуру
    markup = await about_project_keyboard()

    await message.answer(text='О проекте', reply_markup=markup)