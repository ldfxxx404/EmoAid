from utils.images import choice_rand_picture
from aiogram.filters import CommandStart
from aiogram.enums import ChatAction
from aiogram.types import Message

from utils.loader import dp
import asyncio
from utils.template_messages import ask_messages, start, reply, answer


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(start())


@dp.message()
async def general_handler(message: Message) -> None:
    if message.text.lower() in [msg.lower() for msg in ask_messages]:
        await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        await asyncio.sleep(2.5)
        await message.reply(answer())
        return

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2.5)
    await message.reply(reply())

    await message.bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(1.5)
    await message.answer_photo(photo=choice_rand_picture())
    return
