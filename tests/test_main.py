from pathlib import Path

import pytest

from language_wallpaper.main import build_language_data, run


@pytest.fixture
def img_path():
    return str(Path(__file__).parent / "resources" / "default.jpeg")


def test_run_with(img_path):
    run("French", "mac", img_path)


def test_run_without_image_path(img_path):
    run("French", "mac")


def test_build_language_data():
    build_language_data("French")
