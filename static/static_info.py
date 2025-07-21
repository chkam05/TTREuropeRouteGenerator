from static.language_keys import LanguageKeys


class StaticInfo:
    HEADER_TITLE_KEY = 'title'
    HEADER_SUBTITLE_KEY = 'subtitle'
    HEADER_GAME_SUBTITLE_KEY = 'subtitle_game'
    HEADER_MAP_SUBTITLE_KEY = 'subtitle_map'

    FOOTER_TITLE_KEY = 'title'
    FOOTER_VERSION_KEY = 'version'
    FOOTER_COPYRIGHT_KEY = 'copyright'
    FOOTER_LICENCE_KEY = 'licence'
    FOOTER_LEGAL_NOTICE_KEY = 'legal_notice'

    HEADER_DATA = {
        LanguageKeys.LANG_EN_US: {
            HEADER_TITLE_KEY: '🚂 Wsiąść do Pociągu Europa',
            HEADER_SUBTITLE_KEY: '🛤 Generator Tras',
            HEADER_GAME_SUBTITLE_KEY: 'Rozgrywka',
            HEADER_MAP_SUBTITLE_KEY: 'Mapa Trasy'
        }
    }

    FOOTER_DATA = {
        LanguageKeys.LANG_EN_US: {
            FOOTER_TITLE_KEY: 'Wsiąść do Pociągu Europa - Generator Tras',
            FOOTER_VERSION_KEY: 'Wersja: 2.0.0',
            FOOTER_COPYRIGHT_KEY: 'Copyright (c) Kamil Karpiński',
            FOOTER_LICENCE_KEY: 'Licence: Open Source',
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

    @staticmethod
    def get_header(lang_key: str):
        return StaticInfo.HEADER_DATA.get(lang_key, StaticInfo.HEADER_DATA[LanguageKeys.LANG_EN_US])

    @staticmethod
    def get_footer(lang_key: str):
        return StaticInfo.FOOTER_DATA.get(lang_key, StaticInfo.FOOTER_DATA[LanguageKeys.LANG_EN_US])
