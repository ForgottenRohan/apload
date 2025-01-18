from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from aiogram.types import WebAppInfo

TOKEN = "7771154906:AAGOZnoze9DPFS8ddGQ71r0dAkuBqqQzqdI"
CHANNEL_ID = "@gxdlikee"
MAIN_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Инструкция", callback_data="instruction")],
        [InlineKeyboardButton(text="Зарегистрироваться", callback_data="reg")],
        [
            InlineKeyboardButton(
                text="СИГНАЛ!",
                web_app=WebAppInfo(url="https://bebra.work.gd"),
            )
        ],
    ]
)
AFTER_INSTRUCTION_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="СИГНАЛ", web_app=WebAppInfo(url="https://bebra.work.gd")
            )
        ],
        [InlineKeyboardButton(text="Вернуться", callback_data="check_subscribe")],
    ]
)
START_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подписаться", url="https://t.me/gxdlikee")],
        [InlineKeyboardButton(text="Проверить", callback_data="check_subscribe")],
    ]
)
