from tg_bot.handlers import router
import aiogram
import os
import dotenv
import logging
import asyncio
from aiogram import Bot, Dispatcher, html
from tg_bot import handlers
from dotenv import load_dotenv
from pathlib import Path
load_dotenv('/home/max/Documents/sr_parser/.env')
TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()
bot = Bot(TOKEN)


async def main():
    # подключаем руты из app/handlers.py
    dp.include_router(router)
    # функция запуска бота в работу
    await dp.start_polling(bot)


if __name__ == '__main__':
    # включение логирования для отслежки логов при работе бота
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
