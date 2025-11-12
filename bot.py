from random import choice
import re
from loader import dp
from templateMessages import replyMessages, startMessages, dangerWords, askMessages, replyToAskMessage

from aiogram.filters import CommandStart
from aiogram.types import Message


@dp.message(CommandStart())
async def startHandler(message: Message):
    await message.answer(choice(startMessages))

@dp.message()
async def generalHandler(message: Message):
    if not message.text:
        return

    text = message.text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    for word in dangerWords:
        if word in text:
            await message.reply(choice(replyMessages))
            return

    for phrase in askMessages:
        phrase_clean = phrase.lower()
        phrase_clean = re.sub(r'[^\w\s]', '', phrase_clean)
        if phrase_clean in text:
            await message.reply(choice(replyToAskMessage))
            return

    await message.reply(choice(replyMessages))


# @dp.message(CommandStart())
# async def startHandler(message: Message) -> None:
#     # Hello message
#     await message.answer(choice(startMessages))


# @dp.message()
# async def dangerWordHandler(message: Message) -> None:
#     textInMessage = message.text.lower()
#     for word in dangerWords:
#         if word in textInMessage:
#             await message.reply(choice(replyMessages))
#             return
        

# @dp.message()
# async def questionReplyHandler(message: Message) -> None:
#     textInMessage = message.text.lower()
#     for word in askMessages:
#         if word in textInMessage:
#             await message.reply(choice(replyToAskMessage))
#             return

# @dp.message()
# async def replyHandler(message: Message) -> None:
#     # Reply messages
#     await message.reply(choice(replyMessages))

