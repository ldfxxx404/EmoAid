from __future__ import annotations

import datetime

import aiogram
import aiogram.fsm.state
import aiogram.utils.keyboard
import pyquoks


# region Providers

class StringsProvider(pyquoks.data.StringsProvider):
    class AlertStrings(pyquoks.data.StringsProvider.Strings):
        @property
        def export_logs_unavailable(self) -> str:
            return "Логирование отключено!"

        @property
        def button_unavailable(self) -> str:
            return "Эта кнопка недоступна!"

    class ButtonStrings(pyquoks.data.StringsProvider.Strings):
        @property
        def export_logs(self) -> str:
            return "Экспортировать логи"

    class MenuStrings(pyquoks.data.StringsProvider.Strings):
        @property
        def start(self) -> str:
            return (
                "Привет, специалист скоро ответит.\n"
                "Если хочешь, можешь описать свою проблему подробнее."
            )

        @staticmethod
        def info(bot_full_name: str, time_started: datetime.datetime) -> str:
            return (
                f"Информация о {bot_full_name}:\n"
                f"\n"
                f"Запущен: {time_started.strftime("%d.%m.%y %H:%M:%S")} UTC\n"
                f"\n"
                f"Исходный код на GitHub:\n"
                f"https://github.com/ldfxxx404/EmoAid\n"
            )

        @property
        def no_sender_data(self) -> str:
            return (
                "Данные о пользователе отсутствуют!\n"
                "Свяжитесь с отправителем самостоятельно."
            )

    _OBJECTS = {
        "alert": AlertStrings,
        "button": ButtonStrings,
        "menu": MenuStrings,
    }

    alert: AlertStrings
    button: ButtonStrings
    menu: MenuStrings


class ButtonsProvider:
    def __init__(self) -> None:
        self._strings = StringsProvider()

    @property
    def export_logs(self) -> aiogram.types.InlineKeyboardButton:
        return aiogram.types.InlineKeyboardButton(
            text=self._strings.button.export_logs,
            callback_data="export_logs",
        )


class KeyboardProvider:
    def __init__(self) -> None:
        self._buttons = ButtonsProvider()

    @property
    def info(self) -> aiogram.types.InlineKeyboardMarkup:
        markup_builder = aiogram.utils.keyboard.InlineKeyboardBuilder()
        markup_builder.row(self._buttons.export_logs)

        return markup_builder.as_markup()


# endregion

# region Managers

class ConfigManager(pyquoks.data.ConfigManager):
    class SettingsConfig(pyquoks.data.ConfigManager.Config):
        _SECTION = "Settings"

        _VALUES = {
            "admins_list": list,
            "bot_token": str,
            "chat_id": int,
            "file_logging": bool,
            "psychologists_list": list,
            "skip_updates": bool,
        }

        admins_list: list
        bot_token: str
        chat_id: int
        file_logging: bool
        psychologists_list: list
        skip_updates: bool

    _OBJECTS = {
        "settings": SettingsConfig,
    }

    settings: SettingsConfig


# endregion

# region Services

class LoggerService(pyquoks.data.LoggerService):
    def log_user_interaction(self, user: aiogram.types.User, interaction: str) -> None:
        user_info = f"@{user.username} ({user.id})" if user.username else user.id
        self.info(f"{user_info} - \"{interaction}\"")

# endregion
