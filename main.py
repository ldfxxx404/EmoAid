import asyncio
import logging
from os import getenv
import sys
from loader import dp
from dotenv import load_dotenv
import bot

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv()

TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
