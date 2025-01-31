import logging
from aiogram import Bot, Dispatcher, types
import aiohttp
import asyncio
from random import randint
# Настройки
API_TOKEN = '6258953549:AAGaWJRFn7DLtOCL92-MWqPfxR5vKPW3dPQ'  # Замени на свой токен
CHANNEL_ID = '@millonerrrrrrr'    # Например, '@my_test_channel'
API_KEY = 'uklA7HZ6JyIwKlDj29ePcclstdLtylRwah94DjkNr3Zp90kCmfAoAbbBBswf'

# Инициализация
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def send_http_request(link):
    """Отправляет GET-запрос на указанный URL."""
    try:
        async with aiohttp.ClientSession() as session:
            count = randint(1800, 2000)
            async with session.get(f'https://vexboost.ru/api/v2?action=add&service=1555&link={link}&quantity={count}&key={API_KEY}') as response:
                logging.info(f"Запрос отправлен. Номер: {response.json()['order']}")
    except Exception as e:
        logging.error(f"Ошибка при отправке запроса: {e}")

@dp.channel_post()
async def handle_new_post(post: types.Message):
    """Обрабатывает новые посты в канале."""
    # Если пост не пустой (текст, фото, документ и т.д.)
    if post.content_type != 'text' or post.text.strip() != '':
        logging.info(f"Новый пост в канале")
        post_id = post.message_id
        channel_id = post.chat.username or post.chat.id
        post_link = f"https://t.me/{channel_id}/{post_id}"
        logging.info(post_link)
        await send_http_request(link=post_link)  

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))