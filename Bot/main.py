# файлы проекта
from handlers import comands_handler, main_menu_handler

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
dp.include_router(comands_handler.router)
dp.include_router(main_menu_handler.router)

# вывод логов в консоль
logging.basicConfig(level=logging.INFO)



# запускаем пулинг бота
async def main() -> None:
    await dp.start_polling(bot)

# запускаем функцию main() при активации главного файла
if __name__ == "__main__":
    asyncio.run(main())