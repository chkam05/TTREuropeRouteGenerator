from static.language_keys import LanguageKeys


class StaticInfo:
    HEADER_TITLE_KEY = 'title'
    HEADER_SUBTITLE_KEY = 'subtitle'

    HOME_BUTTON_CREATE_GAME_KEY = 'create_game'
    HOME_BUTTON_JOIN_GAME_KEY = 'join_game'
    HOME_INPUT_GAME_NAME_KEY = 'game_name'
    HOME_INPUT_NICKNAME_KEY = 'nickname'

    GAME_GAME_NAME_KEY = 'game_name'
    GAME_NICKNAME_KEY = 'nickname'

    FOOTER_TITLE_KEY = 'title'
    FOOTER_VERSION_KEY = 'version'
    FOOTER_COPYRIGHT_KEY = 'copyright'
    FOOTER_LICENCE_KEY = 'licence'
    FOOTER_LEGAL_NOTICE_KEY = 'legal_notice'

    LABELS_DATA_HOME = {
        LanguageKeys.LANG_EN_US: {
            HEADER_TITLE_KEY: '🚂 Ticket to Ride Europe',
            HEADER_SUBTITLE_KEY: '🛤 Routes Generator',
            HOME_BUTTON_CREATE_GAME_KEY: 'Create Game',
            HOME_BUTTON_JOIN_GAME_KEY: 'Join Game',
            HOME_INPUT_GAME_NAME_KEY: 'Game name',
            HOME_INPUT_NICKNAME_KEY: 'Nickname'
        },
        LanguageKeys.LANG_PL: {
            HEADER_TITLE_KEY: '🚂 Wsiąść do Pociągu Europa',
            HEADER_SUBTITLE_KEY: '🛤 Generator Tras',
            HOME_BUTTON_CREATE_GAME_KEY: 'Stwórz grę',
            HOME_BUTTON_JOIN_GAME_KEY: 'Dołącz do gry',
            HOME_INPUT_GAME_NAME_KEY: 'Nazwa gry',
            HOME_INPUT_NICKNAME_KEY: 'Nazwa gracza'
        }
    }

    LABELS_DATA_GAME = {
        LanguageKeys.LANG_EN_US: {
            HEADER_TITLE_KEY: '🚂 Ticket to Ride Europe',
            HEADER_SUBTITLE_KEY: 'Game',
            GAME_GAME_NAME_KEY: 'Game name:',
            GAME_NICKNAME_KEY: 'Nickname:',
        },
        LanguageKeys.LANG_PL: {
            HEADER_TITLE_KEY: '🚂 Wsiąść do Pociągu Europa',
            HEADER_SUBTITLE_KEY: 'Rozgrywka',
            GAME_GAME_NAME_KEY: 'Nazwa gry:',
            GAME_NICKNAME_KEY: 'Nazwa gracza:',
        }
    }

    FOOTER_DATA = {
        LanguageKeys.LANG_EN_US: {
            FOOTER_TITLE_KEY: 'Ticket to Ride Europe - Routes Generator',
            FOOTER_VERSION_KEY: 'Version: 2.0.0',
            FOOTER_COPYRIGHT_KEY: 'Copyright (c) Kamil Karpiński',
            FOOTER_LICENCE_KEY: 'Licence: Open Source',
            FOOTER_LEGAL_NOTICE_KEY: """
            This project is for personal, non-commercial use only.
            It is inspired by the game "Ticket to Ride" by Alan R. Moon, published by Days of Wonder.
            The project is not affiliated with, sponsored, or endorsed by the authors or the brand owners.
            The source code is available under an open source license.
            """
        },
        LanguageKeys.LANG_PL: {
            FOOTER_TITLE_KEY: 'Wsiąść do Pociągu Europa - Generator Tras',
            FOOTER_VERSION_KEY: 'Wersja: 2.0.0',
            FOOTER_COPYRIGHT_KEY: 'Copyright (c) Kamil Karpiński',
            FOOTER_LICENCE_KEY: 'Licencja: Open Source',
            FOOTER_LEGAL_NOTICE_KEY: """
                Ten projekt powstał wyłącznie na użytek prywatny i niekomercyjny. 
                Jest inspirowany grą „Wsiąść do Pociągu” (oryg. „Ticket to Ride”) autorstwa Alana R. Moona, wydaną przez Days of Wonder. 
                Projekt nie jest powiązany, sponsorowany ani wspierany przez autorów ani właścicieli marki. 
                Kod źródłowy dostępny jest na licencji Open Source.
                """
        }
    }

    def __new__(cls, *args, **kwargs):
        raise TypeError(f"{cls.__name__} is a static class and cannot be instantiated.")

    @classmethod
    def get_home_labels(cls, lang_key: str):
        return cls.LABELS_DATA_HOME.get(lang_key, cls.LABELS_DATA_HOME[LanguageKeys.LANG_EN_US])

    @classmethod
    def get_game_labels(cls, lang_key: str):
        return cls.LABELS_DATA_GAME.get(lang_key, cls.LABELS_DATA_GAME[LanguageKeys.LANG_EN_US])

    @classmethod
    def get_footer(cls, lang_key: str):
        return cls.FOOTER_DATA.get(lang_key, cls.FOOTER_DATA[LanguageKeys.LANG_EN_US])
