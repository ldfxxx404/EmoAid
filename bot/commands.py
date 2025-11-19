from aiogram.types import BotCommand
from aiogram.methods import SetMyCommands
from aiogram import Bot

COMMANDS = [
    BotCommand(command="online", description="online"),
    BotCommand(command="offline", description="offline"),
]

async def bot_commands(bot: Bot) -> None:
    await bot(
        SetMyCommands(
            commands=COMMANDS, language_code="en"
        )
    )
