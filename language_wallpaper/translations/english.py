from language_wallpaper.translations.language import Language


class English(Language):
    """Subclass of translate, translating for French"""

    @property
    def iso6392(self):
        return "eng"

    @property
    def iso6391(self):
        return "en"

    @property
    def tenses(self):
        return ["present", "future", "imperfect"]

    def conjugate(self, verb):
        raise NotImplementedError("Cannot conjugate english verbs")
