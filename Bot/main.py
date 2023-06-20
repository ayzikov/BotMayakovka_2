# файлы проекта
from handlers import comands_handlers, main_menu_handlers, navigation_handlers, location_handlers, admin_handlers, fifth_location_handlers

# отдельные импорты
import logging
import asyncio
import os
from dotenv import load_dotenv

# импорты aiogram
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage



#загрузка виртуального окружения
load_dotenv()

# токен бота
token = os.getenv('BOTTOKEN')

# объект памяти для ФСМ состояний
storage = MemoryStorage()

# бот с диспетчером
bot = Bot(token)
dp = Dispatcher(storage=storage)

# регестрируем роутеры в боте
dp.include_router(comands_handlers.router)
dp.include_router(main_menu_handlers.router)
dp.include_router(navigation_handlers.router)
dp.include_router(location_handlers.router)
dp.include_router(admin_handlers.router)
dp.include_router(fifth_location_handlers.router)

# вывод логов в консоль
logging.basicConfig(level=logging.INFO)



# запускаем пулинг бота
async def main() -> None:
    await dp.start_polling(bot)

# запускаем функцию main() при активации главного файла
if __name__ == "__main__":
    asyncio.run(main())