import asyncio
import logging
import sys
import bot

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot

from utils.loader import dp
from config import TOKEN


async def main() -> None:
    bot_instance = Bot(
        token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot_instance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
