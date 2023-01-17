from abc import ABC, abstractmethod


class WallpaperController(ABC):
    @abstractmethod
    def set_desktop_background(self, filepath: str):
        raise NotImplementedError
