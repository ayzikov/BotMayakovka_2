# файлы проекта
from other.FSM_forms import AdminLogin
from keyboards.admin_keyboard import admin_keyboard

# отдельные импорты
import os
from dotenv import load_dotenv

# импорты aiogram
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router
from aiogram import F



#загрузка виртуального окружения
load_dotenv()

router = Router()

@router.message(F.text=='Админка')
async def login_to_the_admin_panel(message: Message, state: FSMContext):
    ''' При вводе от пользователя "Админка" устанавливается состояние при котором бот ждет от него пароля '''
    await state.set_state(AdminLogin.password)


@router.message(AdminLogin.password)
async def check_password(message: Message, state: FSMContext):
    ''' при вводе правильного пароля пользователь попадает в админ панель '''
    if message.text == os.getenv('ADMIN_PASSWORD'):
        markup = await admin_keyboard()
        await message.answer(text='Админ панель', reply_markup=markup)

    # убираем пользователя из состояния ввода пароля
    await state.clear()
