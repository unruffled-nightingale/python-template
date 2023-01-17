from pathlib import Path

import pytest

from language_wallpaper.wallpaper_controller.mac import MacWallpaperController
from language_wallpaper.wallpaper_controller.wallpaper import WallpaperController
from language_wallpaper.wallpaper_controller.wallpaper_controller import (WALLPAPERS_CONTROLLERS,
                                                                          get_wallpaper_controller)


@pytest.fixture
def controller() -> WallpaperController:
    return WALLPAPERS_CONTROLLERS["mac"]


@pytest.fixture
def img_path():
    return str(Path(__file__).parent / "resources" / "default.jpeg")


@pytest.mark.skip("This test changes the desktop background so should be run manually")
def test_set_as_wallpaper_for_mac(img_path, controller):
    controller.set_desktop_background(img_path)


def test_get_wallpaper_controllers():
    assert type(get_wallpaper_controller("mac")) == MacWallpaperController
