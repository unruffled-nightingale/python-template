import os

from language_wallpaper.wallpaper_controller.wallpaper import WallpaperController


class MacWallpaperController(WallpaperController):
    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "{filepath}"
    end tell
    END"""

    def set_desktop_background(self, filepath: str):
        os.system(self.SCRIPT.format(filepath=filepath))
