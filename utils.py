from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="دوره های زنگ دانش 🎓")],
            [KeyboardButton(text="لینک های مفید 🔗")],
            [KeyboardButton(text="آموزش های کاربردی 📚")],
            [KeyboardButton(text="تماس با من 🗣")],
        ],
        resize_keyboard=True,
        input_field_placeholder="یکی از گزینه ها را انتخاب کنید",
    )

    return keyboard


def useful_links_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="آیدی تلگرام 💬", url="https://t.me/AmiirSaleh"
                )
            ],
            [
                InlineKeyboardButton(
                    text="اینستاگرام 📸", url="https://www.instagram.com/zangedanesh"
                )
            ],
            [
                InlineKeyboardButton(
                    text="کانال تلگرام 📢", url="https://t.me/zangedanesh"
                )
            ],
            [
                InlineKeyboardButton(
                    text="یوتوب ▶️", url="https://www.youtube.com/@zangedanesh"
                )
            ],
            [
                InlineKeyboardButton(
                    text="آپارات 🎬", url="https://www.aparat.com/zangedanesh/"
                )
            ],
            [
                InlineKeyboardButton(
                    text="وبسایت 🌐", url="https://www.zangedanesh.com/"
                )
            ],
        ]
    )

    return keyboard


USEFUL_LINKS_TEXT = """
سلام به تمام زنگ دانشی‌ها 👋🏻❤️
من امیر صالح هستم موسس و مدیر مجموعه آموزشی زنگ‌دانش.

در پایین میتونید تمام راه‌های ارتباطی با من رو ببینید 👇🏻
"""

# CONTACT_ME_TEXT = """
# سلام به تمام زنگ دانشی‌ها 👋🏻❤️من امیر صالح هستم موسس و مدیر مجموعه آموزشی زنگ‌دانش. در پایین تمام راه‌های ارتباطی با من رو میتونید پیدا کنید 👇🏻

# 🔗 آیدی تلگرام: @AmiirSaleh
# 🔗 اینستاگرام: https://www.instagram.com/zangedanesh
# 🔗 کانال تلگرام: https://t.me/zangedanesh
# 🔗 یوتوب: https://www.youtube.com/@zangedanesh
# 🔗 آپارات: https://www.aparat.com/zangedanesh/
# 🔗 وبسایت: https://www.zangedanesh.com/
# """
