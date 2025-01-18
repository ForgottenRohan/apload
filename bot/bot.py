from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
import asyncio
from config import (
    TOKEN,
    MAIN_KEYBOARD,
    START_KEYBOARD,
    CHANNEL_ID,
    AFTER_INSTRUCTION_KEYBOARD,
)

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    user_status = await bot.get_chat_member(
        chat_id=CHANNEL_ID, user_id=message.from_user.id
    )
    if user_status.status != "left":
        await bot.send_message(
            chat_id=message.from_user.id,
            text="thx for subscribe, use bot",
            reply_markup=MAIN_KEYBOARD,
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Subscribe to channel, for use bot",
            reply_markup=START_KEYBOARD,
        )


@dp.callback_query(F.data == "reg")
async def reg(callback: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="Registration text",
        reply_markup=AFTER_INSTRUCTION_KEYBOARD,
    )


@dp.callback_query(F.data == "instruction")
async def instr(callback: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback.from_user.id,
        text="[Instruction text](https://t.me/woeofficial)",
        reply_markup=AFTER_INSTRUCTION_KEYBOARD,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.callback_query(F.data == "check_subscribe")
async def calback(callback: types.CallbackQuery):
    user_status = await bot.get_chat_member(
        chat_id=CHANNEL_ID, user_id=callback.from_user.id
    )
    if user_status.status != "left":
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="thx for subscribe, use bot",
            reply_markup=MAIN_KEYBOARD,
        )
    else:
        await bot.send_message(
            chat_id=callback.from_user.id,
            text="Subscribe to channel, for use bot",
            reply_markup=START_KEYBOARD,
        )


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
