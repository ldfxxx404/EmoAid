from __future__ import annotations
import aiogram, aiogram.filters, aiogram.fsm.storage.base, aiogram.fsm.context
import dispatcher as dp, data, utils


class MessagesRouter(aiogram.Router):
    def __init__(self, logger: data.LoggerService) -> None:
        self._logger = logger

        super().__init__(
            name=self.__class__.__name__,
        )

        self.message.register(
            self.message_handler,
        )

        self._logger.info(f"{self.name} initialized!")

    # region Handlers

    async def message_handler(
            self,
            message: aiogram.types.Message,
            state: aiogram.fsm.context.FSMContext,
            dispatcher: dp.AiogramDispatcher,
    ) -> None:
        is_psychologist = message.from_user.id == dispatcher._config.settings.psychologist_id

        self._logger.log_user_interaction(message.from_user, f"{message.text} ({is_psychologist=})")

        if is_psychologist:
            try:
                if not message.reply_to_message:
                    raise Exception()

                state_data = await state.get_data()

                await dispatcher._bot.send_message(
                    chat_id=state_data[str(message.reply_to_message.message_id)],
                    text=message.text,
                    reply_to_message_id=message.reply_to_message.forward_from_message_id,
                )
            except:
                await dispatcher._bot.send_message(
                    chat_id=message.chat.id,
                    message_thread_id=utils.get_message_thread_id(message),
                    text=dispatcher._strings.menu.psychologist,
                    reply_to_message_id=message.message_id,
                )
        else:
            forwarded_message = await dispatcher._bot.forward_message(
                chat_id=dispatcher._config.settings.psychologist_id,
                message_thread_id=utils.get_message_thread_id(message),
                from_chat_id=message.chat.id,
                message_id=message.message_id,
            )

            psychologist_state = aiogram.fsm.context.FSMContext(
                storage=dispatcher.storage,
                key=aiogram.fsm.storage.base.StorageKey(
                    chat_id=dispatcher._config.settings.psychologist_id,
                    user_id=dispatcher._config.settings.psychologist_id,
                    bot_id=(await dispatcher._bot.me()).id,
                )
            )

            await psychologist_state.update_data(
                data={
                    str(forwarded_message.message_id): message.from_user.id,
                }
            )

    # endregion
