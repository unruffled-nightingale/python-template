import pytest

from language_wallpaper.translations.english import English


@pytest.fixture(scope="module")
def en():
    return English()


def test_iso6391(en):
    assert en.iso6392 == "eng"


def test_iso6392(en):
    assert en.iso6391 == "en"


def test_tenses(en):
    assert en.tenses == ["present", "future", "imperfect"]


def test_conjugate(en):
    with pytest.raises(NotImplementedError):
        en.conjugate("eat")


def test_translate(en):
    assert en.translate("Je suis fait de souvenirs.") == "I am made of memories."


def test_get_verbs(en):
    assert en.get_verbs("I am made of memories.") == ["be", "make"]
