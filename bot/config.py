from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from aiogram.types import WebAppInfo

TOKEN = "7394950836:AAFgZ_0WE95jml8JogBRIcvR3GCGw999DTI"
CHANNEL_ID = "@gxdlikee"
MAIN_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="СИГНАЛ!",
                web_app=WebAppInfo(url="https://bebra.work.gd"),
            )
        ],
    ]
)
START_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подписаться", url="https://t.me/gxdlikee")],
        [InlineKeyboardButton(text="Проверить", callback_data="check_subscribe")],
    ]
)
