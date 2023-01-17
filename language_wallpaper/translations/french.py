from language_wallpaper.translations.language import Language


class French(Language):
    """Subclass of translate, translating for French"""

    @property
    def iso6392(self):
        return "fra"

    @property
    def iso6391(self):
        return "fr"

    @property
    def tenses(self):
        return ["présent", "futur-simple", "imparfait"]
