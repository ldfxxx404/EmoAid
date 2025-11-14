from random import choice
import asyncio
import re
from loader import dp
from templateMessages import (
    replyMessages,
    startMessages,
    askMessages,
    replyToAskMessage,
)

from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
# , InputFile
from aiogram.enums import ChatAction

@dp.message(CommandStart())
async def startHandler(message: Message):
    await message.answer(choice(startMessages))


@dp.message()
async def generalHandler(message: Message):

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2.5)

    if not message.text:
        return
    text = message.text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    for phrase in askMessages:
        phrase_clean = phrase.lower()
        phrase_clean = re.sub(r"[^\w\s]", "", phrase_clean)
        if phrase_clean in text:
            await message.reply(choice(replyToAskMessage))
            return
        photo = FSInputFile('/home/lxmxr/Projects/EmoAid/1.jpg')
        await message.bot.send_chat_action(message.chat.id, photo)
        return

    await message.reply(choice(replyMessages))
