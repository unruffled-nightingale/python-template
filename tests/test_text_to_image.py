from pathlib import Path

import pytest

from language_wallpaper.image_editor import DEFAULT_SCREEN_SIZE, ImageEditor


@pytest.fixture()
def text():
    conjugations = (
        "I speak\nyou speak\nhe/she/it speaks\nwe speak\nyou speak\nthey speak\n"
    )
    return {
        "phrase": "Hello World",
        "translation": "Bonjour le monde",
        "verb": "Hello   Bonjour",
        "conjugations": [
            {"tense": "PRESENT", "conjugations": conjugations},
            {"tense": "PAST", "conjugations": conjugations},
            {"tense": "FUTURE", "conjugations": conjugations},
        ],
    }


@pytest.fixture()
def img_path():
    return str(Path(__file__).parent / "resources" / "default.jpeg")


@pytest.fixture()
def image_editor(text, img_path):
    return ImageEditor(img_path, text)


def test_resize(image_editor):
    image_editor.resize()
    assert image_editor.image.size == DEFAULT_SCREEN_SIZE


def test_make_image_editor(image_editor):
    try:
        image_editor.write_text_to_image()
    except Exception:
        pytest.fail("Failed to write text to image")
