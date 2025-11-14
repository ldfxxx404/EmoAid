from utils.loader import dp
from random import choice
import asyncio
from templateMessages import (
    replyMessages,
    startMessages,
    askMessages,
    replyToAskMessage,
)

from aiogram.filters import CommandStart
from aiogram.types import Message # , FSInputFile
from aiogram.enums import ChatAction


@dp.message(CommandStart())
async def startHandler(message: Message) -> None:
    await message.answer(choice(startMessages))


@dp.message()
async def generalHandler(message: Message) -> None:
    if message.text.lower() in [x.lower() for x in askMessages]:
        await message.reply(choice(replyToAskMessage))
        return

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2.5)
    await message.reply(choice(replyMessages))
    return


# photo = FSInputFile("/home/lxmxr/Projects/EmoAid/1.jpg")
# await message.bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
# await message.bot.send_photo(message.chat.id, photo)
