# остальные импорты
import json

# импорты aiogram
from aiohttp import ClientSession
from aiogram.types import FSInputFile



async def get_location_info_by_number(location_number: int):
    '''
    Функция возвращает словарь с информацией о локации
    :param location_number: номер локации
    :return: dict
    '''

    data = {'location_number': location_number}
    json_data = json.dumps(data)
    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/locations/', data=json_data) as response:

            response = await response.json()

            return response


async def get_images_location_info_by_number(location_number: int):
    '''
    Функция возвращает информацию о фото
    :param location_number: номер локации
    :return: Список словарей с информацией о фотографиях локации
    '''

    data = {'location_number': location_number}
    json_data = json.dumps(data)
    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/images/', data=json_data) as response:

            response = await response.json()

            return response
