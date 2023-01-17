import json
from random import choice

import requests
from verbecc import Conjugator


class Language:
    """Translations, conjugations and verb extraction for a specified language"""

    def __init__(self):
        if self.iso6391 != "en":
            self.conjugator = Conjugator(lang=self.iso6391)

    @property
    def iso6392(self):
        """Returns the the 3 digit iso code for language"""
        raise NotImplementedError()

    @property
    def iso6391(self):
        """Returns the the 2 digit iso code for language"""
        raise NotImplementedError()

    @property
    def tenses(self):
        """Returns the tenses for conjugation"""
        raise NotImplementedError()

    def get_text(self, text):
        translation = self.translate(text)
        verb = choice(self.get_verbs(translation))
        conjugations = self.conjugate(verb)
        return {
            "phrase": text,
            "translation": translation,
            "verb": verb,
            "conjugations": conjugations,
        }

    def translate(self, text):
        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={0}&tl={1}&dt=t&q={2}"
        url = url.format("auto", self.iso6391, text)
        response = requests.get(url)
        return json.loads(response.text)[0][0][0]

    def conjugate(self, verb):
        conjugations = []
        conjugated = self.conjugator.conjugate(verb)
        for tense in self.tenses:
            conjugations.append(
                {
                    "tense": tense.upper(),
                    "conjugations": "\n".join(conjugated["moods"]["indicatif"][tense]),
                }
            )
        return conjugations

    def get_verbs(self, text):
        speech = self._analyse_sentence(text)
        return [self._lemmatize_verb(e["word"]) for e in speech if e["tag"] == "VERB"]

    def _analyse_sentence(self, text):
        url = "https://api.textgain.com/1/tag?q={0}&lang={1}&key=629525c8944da56a68d56b30".format(
            text, self.iso6391
        )
        response = requests.get(url)
        return json.loads(response.text)["text"][0][0]

    def _lemmatize_verb(self, word):
        """
        Requests phrase structure from meaningcloud API.
        Returns lingustic breakdown of sentence
        """
        url = "http://api.meaningcloud.com/parser-2.0"
        payload = (
            "key=3ded5f1530cd52563ff2969719f72896&of=json&lang={0}&txt={1}".format(
                self.iso6391, word
            )
        )
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
        response = json.loads(response.text)
        return response["token_list"][0]["token_list"][0]["token_list"][0][
            "analysis_list"
        ][0]["lemma"]
