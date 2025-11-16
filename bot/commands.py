from utils.loader import dp
from aiogram.types import Message
from aiogram.filters import Command

@dp.message(Command("online"))
async def handle_online(message: Message) -> None:
    await message.reply("djfas")