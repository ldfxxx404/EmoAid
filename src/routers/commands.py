from __future__ import annotations

import datetime

import aiogram
import aiogram.filters
import pyquoks

import data
import dispatcher as dp
import utils


class CommandsRouter(aiogram.Router):
    def __init__(self, logger: data.LoggerService) -> None:
        self._logger = logger

        super().__init__(
            name=self.__class__.__name__,
        )

        self.message.register(
            self.start_handler,
            aiogram.filters.CommandStart(),
        )
        self.message.register(
            self.info_handler,
            aiogram.filters.Command(
                "info",
            ),
        )

        self._logger.info(f"{self.name} initialized!")

    # region Handlers

    async def start_handler(
            self,
            message: aiogram.types.Message,
            command: aiogram.filters.CommandObject,
            dispatcher: dp.AiogramDispatcher,
    ) -> None:
        self._logger.log_user_interaction(message.from_user, command.text)

        await dispatcher._bot.send_message(
            chat_id=message.chat.id,
            message_thread_id=utils.get_message_thread_id(message),
            text=dispatcher._strings.menu.start,
            reply_to_message_id=message.message_id,
        )

    async def info_handler(
            self,
            message: aiogram.types.Message,
            command: aiogram.filters.CommandObject,
            dispatcher: dp.AiogramDispatcher,
    ) -> None:
        is_admin = message.from_user.id in dispatcher._config.settings.admins_list

        self._logger.log_user_interaction(
            user=message.from_user,
            interaction=f"{command.text} ({is_admin=})",
        )

        if is_admin:
            await dispatcher._bot.send_message(
                chat_id=message.chat.id,
                message_thread_id=utils.get_message_thread_id(message),
                text=dispatcher._strings.menu.info(
                    bot_full_name=(await dispatcher._bot.me()).full_name,
                    time_started=pyquoks.utils.get_process_created_datetime().astimezone(
                        tz=datetime.UTC,
                    ),
                ),
                reply_markup=dispatcher._keyboards.info,
            )

    # endregion
