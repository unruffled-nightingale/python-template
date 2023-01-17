from language_wallpaper.wallpaper_controller.mac import MacWallpaperController

WALLPAPERS_CONTROLLERS = {"mac": MacWallpaperController()}


def get_wallpaper_controller(os: str):
    return WALLPAPERS_CONTROLLERS[os]
