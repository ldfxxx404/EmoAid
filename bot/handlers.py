import asyncio

from aiogram.enums import ChatAction
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.images import choice_rand_picture
from utils.loader import dp
from data.template_messages import (
    ask_messages,
    get_random_general_reply,
    get_random_start,
    get_random_reply_to_ask_messages
)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(get_random_start())


@dp.message()
async def general_handler(message: Message) -> None:
    if message.text.lower() in [msg.lower() for msg in ask_messages]:
        await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        await asyncio.sleep(2.5)
        await message.reply(get_random_reply_to_ask_messages())
        return

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2.5)
    await message.reply(get_random_general_reply())

    await message.bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1.5)
    await message.answer_photo(photo=choice_rand_picture())
    return
