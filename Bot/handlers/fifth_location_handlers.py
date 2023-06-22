from crud.add_action import add_action

# импорты aiogram
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Text
from aiogram import Router
from aiogram import F



router = Router()

@router.message(F.text == 'Сходить на выставку')
async def go_to_the_exhibition(message: Message, state: FSMContext):
    # получаем данные из состояния
    data = await state.get_data()

    text = data['detailed_description']

    await message.answer(text=text)

    # добавляем действие в БД
    await add_action(user_tg_id=message.from_user.id,
                     msg_name='Сходить на выставку',
                     location_number=data['location_number'])


@router.message(F.text == 'НАТЕ!')
async def hate_button(message: Message, state: FSMContext):
    # получаем данные из состояния
    data = await state.get_data()

    text = data['additionally']

    await message.answer(text=text)

    # добавляем действие в БД
    await add_action(user_tg_id=message.from_user.id,
                     msg_name='НАТЕ!',
                     location_number=data['location_number'])

