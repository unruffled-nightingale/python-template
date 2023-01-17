import pytest

from language_wallpaper.translations.french import French


@pytest.fixture(scope="module")
def fr():
    return French()


def test_iso6391(fr):
    assert fr.iso6392 == "fra"


def test_iso6392(fr):
    assert fr.iso6391 == "fr"


def test_tenses(fr):
    assert fr.tenses == ["présent", "futur-simple", "imparfait"]


def test_conjugate(fr):
    assert fr.conjugate("manger") == [
        {
            "conjugations": "je mange\ntu manges\nil mange\nnous mangeons\nvous mangez\nils mangent",
            "tense": "PRÉSENT",
        },
        {
            "conjugations": "je mangerai\ntu mangeras\nil mangera\nnous mangerons\nvous mangerez\nils mangeront",
            "tense": "FUTUR-SIMPLE",
        },
        {
            "conjugations": "je mangeais\ntu mangeais\nil mangeait\nnous mangions\nvous mangiez\nils mangeaient",
            "tense": "IMPARFAIT",
        },
    ]


def test_translate(fr):
    assert fr.translate("I am made of memories.") == "Je suis fait de souvenirs."


def test_get_verbs(fr):
    assert fr.get_verbs("Je suis fait de souvenirs.") == ["être", "faire"]


def test_get_text(fr):
    assert fr.get_text("I eat") == {
        "conjugations": [
            {
                "conjugations": "je mange\ntu manges\nil mange\nnous mangeons\nvous mangez\nils mangent",
                "tense": "PRÉSENT",
            },
            {
                "conjugations": "je mangerai\ntu mangeras\nil mangera\nnous mangerons\nvous mangerez\nils mangeront",
                "tense": "FUTUR-SIMPLE",
            },
            {
                "conjugations": "je mangeais\ntu mangeais\nil mangeait\nnous mangions\nvous mangiez\nils mangeaient",
                "tense": "IMPARFAIT",
            },
        ],
        "phrase": "I eat",
        "translation": "je mange",
        "verb": "manger",
    }
