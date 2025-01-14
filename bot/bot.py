from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
import asyncio
from config import TOKEN, MAIN_KEYBOARD, START_KEYBOARD, CHANNEL_ID

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    global start_message_id

    user_status = await bot.get_chat_member(
        chat_id=CHANNEL_ID, user_id=message.from_user.id
    )
    if user_status.status != "left":
        start_message_id = await bot.send_message(
            chat_id=message.from_user.id,
            text="thx for subscribe, use bot",
            reply_markup=MAIN_KEYBOARD,
        )
    else:
        start_message_id = await bot.send_message(
            chat_id=message.from_user.id,
            text="Subscribe to channel, for use bot",
            reply_markup=START_KEYBOARD,
        )


@dp.callback_query(F.data == "check_subscribe")
async def calback(callback: types.CallbackQuery):
    user_status = await bot.get_chat_member(
        chat_id=CHANNEL_ID, user_id=callback.from_user.id
    )
    if user_status.status != "left":
        await bot.edit_message_text(
            chat_id=callback.from_user.id,
            text="thx for subscribe, use bot",
            reply_markup=MAIN_KEYBOARD,
            message_id=start_message_id.message_id,
        )
    else:
        await bot.edit_message_text(
            chat_id=callback.from_user.id,
            text="Subscribe to channel, for use bot",
            reply_markup=START_KEYBOARD,
            message_id=start_message_id.message_id,
        )


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
