from dotenv import load_dotenv
from utils.loader import dp
from os import getenv
from core import bot
import logging
import asyncio
import sys

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot

load_dotenv()

TOKEN = getenv("BOT_TOKEN")


async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
