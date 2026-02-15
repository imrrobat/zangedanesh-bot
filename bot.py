import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from dotenv import load_dotenv
from db import init_db, get_user_by_telegram_id, add_user
from utils import main_menu_keyboard, useful_links_keyboard, USEFUL_LINKS_TEXT

load_dotenv()
init_db()

API_TOKEN = os.getenv("API_TOKEN")


class RegisterState(StatesGroup):
    waiting_for_fullname = State()


async def start_handler(pm: Message, state: FSMContext):
    telegram_id = pm.from_user.id

    user = get_user_by_telegram_id(telegram_id)

    if user:
        await pm.answer("خوش اومدی دوباره 🌱", reply_markup=main_menu_keyboard())
    else:
        await pm.answer("سلام 👋\nلطفا نام و نام خانوادگی خود را ارسال کنید:")
        await state.set_state(RegisterState.waiting_for_fullname)


async def fullname_handler(pm: Message, state: FSMContext):
    if not pm.text:
        await pm.answer("لطفا فقط نام و نام خانوادگی را به صورت متن ارسال کنید.")
        return

    fullname = pm.text.strip()
    telegram_id = pm.from_user.id
    username = pm.from_user.username

    add_user(telegram_id, username, fullname)

    await pm.answer(
        "ثبت نام شما با موفقیت انجام شد ✅", reply_markup=main_menu_keyboard()
    )
    await state.clear()


async def help_handler(pm: Message):
    await pm.answer(
        "به دلایل مشکوکی نمیتونم کمکت کنم", reply_markup=main_menu_keyboard()
    )


async def contact_handler(pm: Message):
    await pm.answer(
        USEFUL_LINKS_TEXT,
        reply_markup=useful_links_keyboard(),
        disable_web_page_preview=True,
    )


async def courses_handler(pm: Message):
    await pm.answer(
        "لیست دوره ها به زودی اینجا نمایش داده میشه 🎓",
        reply_markup=main_menu_keyboard(),
    )


async def links_handler(pm: Message):
    await pm.answer(
        "اینجا لینک های مفید قرار میگیرن 🔗", reply_markup=main_menu_keyboard()
    )


async def tutorials_handler(pm: Message):
    await pm.answer(
        "آموزش های کاربردی اینجا قرار میگیرن 📚", reply_markup=main_menu_keyboard()
    )


async def main():
    bot = Bot(API_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())
    dp.message.register(help_handler, Command("help"))
    dp.message.register(fullname_handler, RegisterState.waiting_for_fullname)

    dp.message.register(contact_handler, F.text == "تماس با من 🗣")
    dp.message.register(courses_handler, F.text == "دوره های زنگ دانش 🎓")
    dp.message.register(links_handler, F.text == "لینک های مفید 🔗")
    dp.message.register(tutorials_handler, F.text == "آموزش های کاربردی 📚")

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
