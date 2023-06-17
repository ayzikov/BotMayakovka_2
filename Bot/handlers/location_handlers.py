# отдельные импорты
import pathlib
from urllib.parse import unquote

# файлы проекта
from BotMayakovka_2.Bot.other.additional_functions import parsing_images


# импорты aiogram
from aiogram.filters import Text
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile



# роутер (сын диспетчера)
router = Router()

# обработка кнопки 'Подробное описание'
@router.message(Text(text='Подробное описание'))
async def detailed_desc_handler(message: Message, state: FSMContext):
    # получаем данные из состояния
    data = await state.get_data()

    # получаем изображения
    images_info = data['images_info']

    # изображения для вывода в чат
    # список с кортежами путей изображений и их описанием
    images_tuple = await parsing_images(images_info, 'Подробное описание')

    # перебираем циклом инфо о изображениях, делаем из них FSInputFile-объекты и выводим в чат
    for image_tuple in images_tuple:
        # получаем полный путь к изображению
        current_path = str(pathlib.Path(__file__).resolve().parents[2])
        image_path = pathlib.Path(current_path, 'Django', *image_tuple[0].split('/'))
        image = FSInputFile(image_path)

        # получаем описание изображения
        image_description = image_tuple[1]

        await message.answer_photo(photo=image, caption=image_description)


    # получаем подробное описание локации
    text = data['detailed_description']

    await message.answer(text=text)


# обработка кнопки 'Аудиогид'
@router.message(Text(text='Аудиогид'))
async def audioguid_handler(message: Message, state: FSMContext):

    # получаем данные из состояния
    data = await state.get_data()

    # путь к файлу с аудиогидом
    current_path = str(pathlib.Path(__file__).resolve().parents[2])
    audio_path = pathlib.Path(current_path, 'Django', *unquote(data['audio_guide']).split('/'))
    audio = FSInputFile(audio_path)

    await message.answer_voice(audio)



# обработка кнопки 'Дополнительно'
@router.message(F.text.in_({'Софья Шамардина'}))
async def additionally_handler(message: Message, state: FSMContext):
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

        await message.answer_photo(photo=image, caption=image_description)

        # получаем подробное описание локации
        text = data['additionally']

    await message.answer(text=text)


