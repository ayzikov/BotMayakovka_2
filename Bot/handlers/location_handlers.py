# отдельные импорты


# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Подробное описание'
@router.message(Text(text='Подробное описание'))
async def detailed_desc_handler(message: Message, state: FSMContext):
    # получаем данные из состояния
    data = await state.get_data()

    # получаем изображения


    # получаем подробное описание локации
    text = data['detailed_description']

    await message.answer(text=text)


# обработка кнопки 'Аудиогид'
@router.message(Text(text='Аудиогид'))
async def audioguid_handler(message: Message):


    await message.answer(text='Аудиогид')


# обработка кнопки 'Дополнительно'
@router.message(F.text.in_({'Софья Шамардина'}))
async def additionally_handler(message: Message):


    await message.answer(text='Дополнительно')


