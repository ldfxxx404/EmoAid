from __future__ import annotations
import random
import pyquoks, aiogram


# region Managers

class StringsProvider(pyquoks.data.StringsProvider):
    class MenuStrings(pyquoks.data.StringsProvider.Strings):
        @property
        def _start_0(self) -> str:
            return "Я тут чтобы помочь тебе, расскажи о том, что тебя волнует"

        @property
        def _start_1(self) -> str:
            return "Что тебя волнует? Расскажи мне, и я постараюсь тебе помочь"

        @property
        def _start_2(self) -> str:
            return "Я готов тебя выслушать. Расскажи, что на душе?"

        @property
        def _start_3(self) -> str:
            return "Иногда просто хочется, чтобы кто-то выслушал, разве не так?"

        @property
        def _start_4(self) -> str:
            return "Расскажи, что тебя беспокоит? Я рядом и готов помочь"

        @property
        def start(self) -> str:
            available_strings = 5

            string_index = random.randint(0, available_strings - 1)

            match string_index:
                case 0:
                    return self._start_0
                case 1:
                    return self._start_1
                case 2:
                    return self._start_2
                case 3:
                    return self._start_3
                case 4:
                    return self._start_4
                case _:
                    raise ValueError()

        @property
        def _reply_0(self) -> str:
            return (
                "Психолога пока нет рядом, опиши свою проблему подробней ❤️\n"
                "Как только специалист освободится - он ответит тебе 🤗"
            )

        @property
        def _reply_1(self) -> str:
            return (
                "К сожалению, психолога пока нет на месте 🌸\n"
                "Оставь своё сообщение, мы скоро вернёмся к тебе 🫂"
            )

        @property
        def _reply_2(self) -> str:
            return (
                "Сейчас психолог занят другим разговором 👀\n"
                "Поделись своими мыслями, мы обязательно поможем ✨"
            )

        @property
        def _reply_3(self) -> str:
            return (
                "В данный момент психолог недоступен 😴\n"
                "Опиши ситуацию, постараемся помочь как можно скорее 🫶"
            )

        @property
        def _reply_4(self) -> str:
            return (
                "Можешь поделиться своими переживаниями, пока психолог отошёл 😌\n"
                "Он обязательно ответит, как только сможет ⏰"
            )

        @property
        def reply(self) -> str:
            available_strings = 5

            string_index = random.randint(0, available_strings - 1)

            match string_index:
                case 0:
                    return self._reply_0
                case 1:
                    return self._reply_1
                case 2:
                    return self._reply_2
                case 3:
                    return self._reply_3
                case 4:
                    return self._reply_4
                case _:
                    raise ValueError()

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
            "file_logging": bool,
            "skip_updates": bool,
        }

        bot_token: str
        file_logging: bool
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
