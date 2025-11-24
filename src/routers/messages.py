from __future__ import annotations

import aiogram
import aiogram.filters
import aiogram.fsm.context
import aiogram.fsm.storage.base

import data
import dispatcher as dp
import utils


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
        is_psychologist_chat = message.chat.id == dispatcher._config.settings.chat_id
        has_reply_to_forwarded = bool(message.reply_to_message and message.reply_to_message.forward_origin)

        self._logger.log_user_interaction(
            user=message.from_user,
            interaction=f"{message.text} ({is_psychologist_chat=}, {has_reply_to_forwarded=})",
        )

        if is_psychologist_chat:
            if has_reply_to_forwarded:
                try:
                    state_data = await state.get_data()
                    original_chat_id = state_data[str(message.reply_to_message.message_id)]

                    await dispatcher._bot.send_message(
                        chat_id=original_chat_id,
                        text=message.text,
                        reply_to_message_id=message.reply_to_message.forward_from_message_id,
                    )
                except:
                    await dispatcher._bot.send_message(
                        chat_id=message.chat.id,
                        message_thread_id=utils.get_message_thread_id(message),
                        text=dispatcher._strings.menu.no_sender_data,
                        reply_to_message_id=message.message_id,
                    )
        elif message.text:
            forwarded_message = await dispatcher._bot.forward_message(
                chat_id=dispatcher._config.settings.chat_id,
                from_chat_id=message.chat.id,
                message_id=message.message_id,
            )

            for psychologist_id in dispatcher._config.settings.psychologists_list:
                psychologist_state = aiogram.fsm.context.FSMContext(
                    storage=dispatcher.storage,
                    key=aiogram.fsm.storage.base.StorageKey(
                        chat_id=dispatcher._config.settings.chat_id,
                        user_id=psychologist_id,
                        bot_id=(await dispatcher._bot.me()).id,
                    ),
                )

                await psychologist_state.update_data(
                    data={
                        str(forwarded_message.message_id): message.from_user.id,
                    },
                )

    # endregion
