from language_wallpaper.translations.english import English
from language_wallpaper.translations.french import French

TRANSLATIONS = {"English": English(), "French": French()}


def get_text(language: str, text: str):
    try:
        return TRANSLATIONS[language].get_text(text)
    except Exception as e:
        raise TranslationException(f"Unable to translate proverb - {str(e)}")


class TranslationException(Exception):
    pass
