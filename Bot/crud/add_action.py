# остальные импорты
import json

# импорты aiogram
from aiohttp import ClientSession

async def add_action(user_tg_id, msg_name, location_number):
    ''' Функция делает запрос в БД на добавление нажатия на кнопку'''

    data = {'user_tg_id': user_tg_id,
            'msg_name': msg_name,
            'location_number': location_number}

    json_data = json.dumps(data)
    async with ClientSession() as session:
        async with session.post('http://127.0.0.1:8080/action_add/', data=json_data) as response:

            response = await response.json()
            print(response)