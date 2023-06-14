# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Прогуляться по городу'
@router.message(Text(text='Подробное описание'))
async def walk_handler(message: Message):


    await message.answer(text='Подробное описание')


# обработка кнопки 'Прогуляться по городу'
@router.message(Text(text='Аудиогид'))
async def walk_handler(message: Message):


    await message.answer(text='Аудиогид')


# обработка кнопки 'Прогуляться по городу'
@router.message(Text(text='Дополнительно'))
async def walk_handler(message: Message):


    await message.answer(text='Дополнительно')


