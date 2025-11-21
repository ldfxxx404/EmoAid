from __future__ import annotations
import pyquoks, aiogram, aiogram.fsm.state


# region Providers

class StringsProvider(pyquoks.data.StringsProvider):
    class MenuStrings(pyquoks.data.StringsProvider.Strings):
        @property
        def start(self) -> str:
            return (
                "Привет, психолог скоро ответит\n"
                "Можешь описать свою проблему подробней?"
            )

        @property
        def psychologist(self) -> str:
            return (
                "Для обратной связи с пользователем\n"
                "ответьте на пересланное сообщение!"
            )

    _OBJECTS = {
        "menu": MenuStrings,
    }

    menu: MenuStrings


# endregion

# region Managers

class ConfigManager(pyquoks.data.ConfigManager):
    class SettingsConfig(pyquoks.data.ConfigManager.Config):
        _SECTION = "Settings"

        _VALUES = {
            "bot_token": str,
            "chat_id": int,
            "file_logging": bool,
            "psychologists_list": list,
            "skip_updates": bool,
        }

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
