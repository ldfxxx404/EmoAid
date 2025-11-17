from __future__ import annotations
import aiogram, aiogram.filters
import data, utils


class CommandsRouter(aiogram.Router):
    def __init__(self, logger: data.LoggerService) -> None:
        self._strings = data.StringsProvider()
        self._logger = logger

        super().__init__(
            name=self.__class__.__name__,
        )

        self.message.register(
            self.start_handler,
            aiogram.filters.CommandStart(),
        )

        self._logger.info(f"{self.name} initialized!")

    # region Handlers

    async def start_handler(
            self,
            message: aiogram.types.Message,
            command: aiogram.filters.CommandObject,
            bot: aiogram.Bot,
    ) -> None:
        self._logger.log_user_interaction(message.from_user, command.text)

        await bot.send_message(
            chat_id=message.chat.id,
            message_thread_id=utils.get_message_thread_id(message),
            text=self._strings.menu.start,
            reply_to_message_id=message.message_id,
        )

    # endregion
