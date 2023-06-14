# файлы проекта

# отдельные импорты
import logging
import asyncio
import os
from dotenv import load_dotenv

# импорты aiogram
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.filters import Command, Text
from aiogram.types import Message
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

# вывод логов в консоль
logging.basicConfig(level=logging.INFO)


# тестовый хендлер
@dp.message(Command(commands=['start']))
async def hello(message: Message):
    await message.answer(text='Приветствие')


# запускаем пулинг бота
async def main() -> None:
    await dp.start_polling(bot)

# запускаем функцию main() при активации главного файла
if __name__ == "__main__":
    asyncio.run(main())