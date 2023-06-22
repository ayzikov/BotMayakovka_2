# остальные импорты
import json

# импорты aiogram
from aiohttp import ClientSession

async def get_user_and_comands_statistic():
    ''' Функция делает запрос в БД на получение статистики'''

    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/statistic/') as response:

            response = await response.json()
            return response