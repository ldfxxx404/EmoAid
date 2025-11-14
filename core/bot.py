from utils.loader import dp
from random import choice
import asyncio
from utils.templateMessages import (
    reply_to_ask_messages,
    reply_messages,
    start_messages,
    ask_messages,
)

from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, InputFile
from aiogram.enums import ChatAction


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(choice(start_messages))


@dp.message()
async def general_handler(message: Message) -> None:
    if message.text.lower() in [msg.lower() for msg in ask_messages]:
        await message.reply(choice(reply_to_ask_messages))
        return

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2.5)
    await message.reply(choice(reply_messages))

    await message.bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
    # photo = FSInputFile("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDrty1oP6IZ9xUx33QIlQOEvaI-aFk_2QMsQ&s")
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDrty1oP6IZ9xUx33QIlQOEvaI-aFk_2QMsQ&s', caption='Внимательно посмотри на кота, что ты чувствуешь?')
    return


# photo = FSInputFile("/home/lxmxr/Projects/EmoAid/1.jpg")
# await message.bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
# await message.bot.send_photo(message.chat.id, photo)
