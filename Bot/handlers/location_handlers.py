# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Подробное описание'
@router.message(Text(text='Подробное описание'))
async def detailed_desc_handler(message: Message):


    await message.answer(text='Подробное описание')


# обработка кнопки 'Аудиогид'
@router.message(Text(text='Аудиогид'))
async def audioguid_handler(message: Message):


    await message.answer(text='Аудиогид')


# обработка кнопки 'Дополнительно'
@router.message(Text(text='Дополнительно'))
async def additionally_handler(message: Message):


    await message.answer(text='Дополнительно')


