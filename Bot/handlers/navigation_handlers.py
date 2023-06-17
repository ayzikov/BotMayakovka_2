# отдельные иморты
import pathlib

# файлы проекта
from BotMayakovka_2.Bot.keyboards.menu_for_location_keyboard import location_keyboard
from BotMayakovka_2.Bot.keyboards.second_lvl_keyboards import walk_keyboard
from BotMayakovka_2.Bot.crud.all_location_info import get_location_info_by_number, get_images_location_info_by_number
from BotMayakovka_2.Bot.other.additional_functions import parsing_images

# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Я на месте'
@router.message(Text(text='Я на месте'))
async def in_place_handler(message: Message, state: FSMContext):
    # при каждом нажатии этой кнопки номер локации пользователя в ФСМ состоянии увеличивается на 1

    # получаем номер локации из состояния
    data = await state.get_data()
    location_number = data['location_number']

    # увеличиваем его на 1
    location_number += 1

    # записываем в состояние новый номер локации
    await state.update_data(location_number=location_number)

    # получаем информацию о локации и информацию о каждой фотографии локации
    location_info = await get_location_info_by_number(location_number)
    images_info = await get_images_location_info_by_number(location_number)

    # парсим и записываем информацию о локации в ФСМ состояние
    await state.update_data(
        location_name=location_info['location_name'],
        location_latitude=location_info['location_latitude'],
        location_longitude=location_info['location_longitude'],
        main_text=location_info['main_text'],
        detailed_description=location_info['detailed_description'],
        audio_guide_text=location_info['audio_guide_text'],
        audio_guide=location_info['audio_guide'],
        additionally=location_info['additionally'],
        additionally_button=location_info['additionally_button']
    )

    # записываем в состояние список словарей с информацией о фотографиях
    await state.update_data(
        images_info=images_info
    )


    # изображения для вывода в чат
    # список с кортежами путей изображений и их описанием
    images_tuple = await parsing_images(images_info, 'Я на месте')

    # перебираем циклом инфо о изображениях, делаем из них FSInputFile-объекты и выводим в чат
    for image_tuple in images_tuple:

        # получаем полный путь к изображению
        current_path = str(pathlib.Path(__file__).resolve().parents[2])
        image_path = pathlib.Path(current_path, 'Django', *image_tuple[0].split('/'))
        image = FSInputFile(image_path)

        # получаем описание изображения
        image_description = image_tuple[1]

        await message.answer_photo(photo=image, caption=image_description)


    # получам клавиатуру
    markup = await location_keyboard(location_info['additionally_button'])

    # текст для вывода в чат
    text = location_info['main_text']

    await message.answer(text=text, reply_markup=markup)


# обработка кнопки 'Дальше'
@router.message(Text(text='Дальше'))
async def next_location_handler(message: Message):


    # получам клавиатуру
    markup = await walk_keyboard()

    await message.answer(text='Дальше', reply_markup=markup)