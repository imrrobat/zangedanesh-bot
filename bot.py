import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")


async def start_handler(pm: Message):
    await pm.answer("سلام اینجا بات زنگ دانشه")


async def help_handler(pm: Message):
    await pm.answer("به دلایل مشکوکی نمیتونم کمکت کنم")


async def main():
    bot = Bot(API_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())
    dp.message.register(help_handler, Command("help"))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
