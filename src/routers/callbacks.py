from __future__ import annotations

import aiogram
import aiogram.exceptions
import aiogram.filters

import data
import dispatcher as dp
import utils


class CallbacksRouter(aiogram.Router):
    def __init__(self, logger: data.LoggerService) -> None:
        self._logger = logger

        super().__init__(
            name=self.__class__.__name__,
        )

        self.callback_query.register(
            self.callback_handler,
        )

        self._logger.info(f"{self.name} initialized!")

    # region Handlers

    async def callback_handler(
            self,
            call: aiogram.types.CallbackQuery,
            dispatcher: dp.AiogramDispatcher,
    ) -> None:
        is_admin = call.from_user.id in dispatcher._config.settings.admins_list

        self._logger.log_user_interaction(
            user=call.from_user,
            interaction=f"{call.data} ({is_admin=})",
        )

        try:
            match call.data:
                case _:
                    if is_admin:
                        match call.data:
                            case "export_logs":
                                if dispatcher._config.settings.file_logging:
                                    logs_file = self._logger.file

                                    await dispatcher._bot.send_document(
                                        chat_id=call.message.chat.id,
                                        message_thread_id=utils.get_message_thread_id(call.message),
                                        document=aiogram.types.BufferedInputFile(
                                            file=logs_file.read(),
                                            filename=logs_file.name,
                                        ),
                                    )

                                    logs_file.close()
                                else:
                                    await dispatcher._bot.answer_callback_query(
                                        callback_query_id=call.id,
                                        text=dispatcher._strings.alert.export_logs_unavailable,
                                        show_alert=True,
                                    )
                            case _:
                                await dispatcher._bot.answer_callback_query(
                                    callback_query_id=call.id,
                                    text=dispatcher._strings.alert.button_unavailable,
                                    show_alert=True,
                                )
                    else:
                        await dispatcher._bot.answer_callback_query(
                            callback_query_id=call.id,
                            text=dispatcher._strings.alert.button_unavailable,
                            show_alert=True,
                        )
        except Exception as exception:
            if exception is not aiogram.exceptions.TelegramBadRequest:
                self._logger.log_error(
                    exception=exception,
                )
        finally:
            await dispatcher._bot.answer_callback_query(
                callback_query_id=call.id,
            )

    # endregion
