# файлы проекта
from other.FSM_forms import AdminLogin
from keyboards.admin_keyboard import admin_keyboard
from crud.statistic import get_user_and_comands_statistic

# отдельные импорты
import os
from dotenv import load_dotenv

# импорты aiogram
from aiogram.fsm.context import FSMContext
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


@router.message(F.text=='Статистика')
async def get_statistic(message: Message, state: FSMContext):
    ''' показывает администратору статистику '''

    # получаем данные с БД
    data = await get_user_and_comands_statistic()

    # сортируем команды по количеству нажатий
    comands = sorted(data['clicks'], key=lambda elem: elem['count'], reverse=True)

    # делаем строку команд для вывода в чат
    comands_str = '\n'.join([f"{comand['msg_name']} - {comand['count']}" for comand in comands])

    # делаем строку количества пользователей для вывода в чат
    users_str = f"Всего пользователей - {data['quantity_users']}\n" \
                f"Пользователей за день - {data['quantity_users_day']}\n" \
                f"Пользователей за неделю - {data['quantity_users_week']}\n\n" \
                f"Прошли больше 25% - {data['quantity_users_25']}\n" \
                f"Прошли больше 50% - {data['quantity_users_50']}\n" \
                f"Прошли больше 75% - {data['quantity_users_75']}\n" \
                f"Прошли 100% - {data['quantity_users_100']}"

    text = f"{users_str}\n\n" \
           f"Статистика по командам:\n\n" \
           f"{comands_str}"

    await message.answer(text=text)