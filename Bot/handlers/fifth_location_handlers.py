# отдельные импорты
import pathlib

# файлы проекта
from other.additional_functions import parsing_images
from crud.add_action import add_action

# импорты aiogram
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.filters import Text
from aiogram import Router
from aiogram import F



router = Router()

@router.message(F.text == 'Осмотреть двор')
async def go_to_the_exhibition(message: Message, state: FSMContext):
    # получаем данные из состояния
    data = await state.get_data()

    text = data['detailed_description']

    # геолокация двора
    await message.answer_location(latitude=59.932114, longitude=30.343957)

    # сообщение
    await message.answer(text=text)

    # добавляем действие в БД
    await add_action(user_tg_id=message.from_user.id,
                     msg_name='Осмотреть двор',
                     location_number=data['location_number'])


@router.message(F.text == 'Юбилеить')
async def hate_button(message: Message, state: FSMContext):
    # получаем данные из состояния
    data = await state.get_data()

    # получаем изображения
    images_info = data['images_info']

    # изображения для вывода в чат
    # список с кортежами путей изображений и их описанием
    images_tuple = await parsing_images(images_info, 'Дополнительно')

    # перебираем циклом инфо о изображениях, делаем из них FSInputFile-объекты и выводим в чат
    for image_tuple in images_tuple:
        # получаем полный путь к изображению
        current_path = str(pathlib.Path(__file__).resolve().parents[2])
        image_path = pathlib.Path(current_path, 'Django', *image_tuple[0].split('/'))
        image = FSInputFile(image_path)

        # получаем описание изображения
        image_description = image_tuple[1]

        try:
            await message.answer_photo(photo=image, caption=image_description)
        except:
            pass

    text = data['additionally']

    await message.answer(text=text)

    # добавляем действие в БД
    await add_action(user_tg_id=message.from_user.id,
                     msg_name='Юбилеить',
                     location_number=data['location_number'])

