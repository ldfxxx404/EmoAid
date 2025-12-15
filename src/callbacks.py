import aiogram
import aiogram.exceptions
import aiogram.filters

import constants
import data
import utils


class CallbacksRouter(aiogram.Router):
    def __init__(
            self,
            strings_provider: data.StringsProvider,
            config_manager: data.ConfigManager,
            logger_service: data.LoggerService,
            bot: aiogram.Bot,
    ) -> None:
        self._strings = strings_provider
        self._config = config_manager
        self._logger = logger_service
        self._bot = bot

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
    ) -> None:
        is_admin = call.from_user.id in self._config.settings.admins_list

        self._logger.log_user_interaction(
            user=call.from_user,
            interaction=f"{call.data} ({is_admin=})",
        )

        try:
            if is_admin:
                match call.data:
                    case "export_logs":
                        if self._config.settings.file_logging:
                            logs_file = self._logger.file

                            await self._bot.send_document(
                                chat_id=call.message.chat.id,
                                message_thread_id=utils.get_message_thread_id(call.message),
                                document=aiogram.types.BufferedInputFile(
                                    file=logs_file.read(),
                                    filename=logs_file.name,
                                ),
                            )

                            logs_file.close()
                        else:
                            await self._bot.answer_callback_query(
                                callback_query_id=call.id,
                                text=self._strings.alert.export_logs_unavailable,
                                show_alert=True,
                            )
                    case _:
                        await self._bot.answer_callback_query(
                            callback_query_id=call.id,
                            text=self._strings.alert.button_unavailable,
                            show_alert=True,
                        )
            else:
                await self._bot.answer_callback_query(
                    callback_query_id=call.id,
                    text=self._strings.alert.button_unavailable,
                    show_alert=True,
                )
        except Exception as e:
            if type(e) not in constants.IGNORED_EXCEPTIONS:
                self._logger.log_error(e)
        finally:
            await self._bot.answer_callback_query(
                callback_query_id=call.id,
            )

    # endregion
