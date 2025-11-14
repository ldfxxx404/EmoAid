# bot.py
import asyncio
from aiogram.types import Message, FSInputFile
from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from loader import dp
from data.templateMessages import (
    get_random_start,
    get_random_reply_to_ask,
    get_random_general_reply
)

from logic.logic import find_matching_phrase
from config import PHOTO_PATH

PHOTO_PATH = PHOTO_PATH


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(get_random_start())


@dp.message()
async def general_handler(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2.5)

    if not message.text:
        return

    if find_matching_phrase(message.text):
        await message.reply(get_random_reply_to_ask())

        await message.bot.send_chat_action(message.chat.id,
                                           ChatAction.UPLOAD_PHOTO)
        photo = FSInputFile(PHOTO_PATH)
        await message.answer_photo(photo=photo, caption="фото")
        return

    await message.reply(get_random_general_reply())
