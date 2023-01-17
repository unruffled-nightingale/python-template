from pathlib import Path
from urllib.request import urlopen

from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Resampling

DEFAULT_SCREEN_SIZE = (2880, 1800)


class ImageEditor:

    FONT_DIR = Path(__file__).parent / "fonts"

    def __init__(self, image_path: str, text: dict):
        self.font_dir = Path(__file__).parent / ".." / "resources" / "fonts"
        self.font_one = "https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Black.ttf?raw=true"
        self.font_two = "https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Black.ttf?raw=true"
        self.fill = (255, 255, 255, 255)
        self.image_path = image_path
        self.text = text
        self.image = Image.open(image_path)
        self.draw = ImageDraw.Draw(self.image)

    def write_text_to_image(self):
        """Writes text to image"""

        # Load image and resize to fit wallpaper
        self.resize()

        # Add phrase
        phrase_text = self.text["phrase"]
        phrase_font_size = 35
        phrase_font = ImageFont.truetype(urlopen(self.font_one), phrase_font_size)
        phrase_position = (200, 200)
        self._write_text(phrase_position, phrase_text, phrase_font)

        # Add translation
        translation_text = self.text["translation"]
        translation_font_size = 35
        translation_font = ImageFont.truetype(
            urlopen(self.font_one), translation_font_size
        )
        # Get translation position from phrase position
        translation_x = phrase_position[0]
        translation_y = (
            phrase_position[1] + self._font_pixel_size(phrase_text, phrase_font)[1] + 10
        )
        translation_position = (translation_x, translation_y)
        self._write_text(translation_position, translation_text, translation_font)

        # Add verb
        verb_text = self.text["verb"]
        verb_font_size = 28
        verb_font = ImageFont.truetype(urlopen(self.font_two), verb_font_size)
        verb_x = phrase_position[0]
        verb_y = (
            translation_position[1]
            + self._font_pixel_size(translation_text, translation_font)[1]
            + 25
        )
        verb_position = (verb_x, verb_y)
        self._write_text(verb_position, verb_text, verb_font)

        # Add conjugations
        next_conjugation_x = verb_position[0]
        for c in self.text["conjugations"]:
            # Add tense
            tense_text = c["tense"]
            tense_font_size = 26
            tense_font = ImageFont.truetype(urlopen(self.font_two), tense_font_size)
            tense_x = next_conjugation_x
            tense_y = (
                verb_position[1] + self._font_pixel_size(verb_text, verb_font)[1] + 35
            )
            tense_position = (tense_x, tense_y)
            self._write_text(tense_position, tense_text, tense_font)

            conjugation_text = c["conjugations"]
            conjugation_font_size = 26

            conjugation_font = ImageFont.truetype(
                urlopen(self.font_two), conjugation_font_size
            )
            # Get conjugation position from phrase position
            conjugation_x = next_conjugation_x
            conjugation_y = tense_y + 40
            conjugation_position = (conjugation_x, conjugation_y)
            # Set the x co-ordinate for next conjugation based on the position and size of this co-ordinate
            next_conjugation_x = (
                conjugation_position[0]
                + self._font_pixel_size(conjugation_text, conjugation_font)[1]
                + 35
            )

            self._write_text(conjugation_position, conjugation_text, conjugation_font)

    def save(self, filename: str):
        self.image.save(filename, quality=100)

    def resize(self):
        """
        Resizes the image to fit the resolution of the screen.
        This must be done prior to adding text, to avoid skewing
        """
        image_width, image_height = self.image.size
        image_ratio = image_width / image_height
        screen_width, screen_height = DEFAULT_SCREEN_SIZE
        screen_ratio = screen_width / screen_height

        # if the image is too skinny
        if image_ratio < screen_ratio:
            # set the image width to be equal to the screen width
            new_image_width = screen_width
            # set the image height proportionally
            new_image_height = int(image_height * (screen_width / image_width))
            # resize the image
            self.image = self.image.resize(
                (new_image_width, new_image_height), Image.ANTIALIAS
            )

            # crop the top and bottom of the picture to keep image and screen ration equal
            pixels_to_cut = int((new_image_height - screen_height) / 2)
            left = 0
            top = pixels_to_cut
            right = new_image_width
            bottom = new_image_height - pixels_to_cut
            # crop the image
            self.image = self.image.crop((left, top, right, bottom))

        # if the image is too fat
        elif image_ratio > screen_ratio:
            # set the image width to be equal to the screen width
            new_image_height = int(screen_height)
            # set the image height proportionally
            new_image_width = int(image_width * (screen_height / screen_height))
            # resize the image.
            self.image = self.image.resize(
                (new_image_width, new_image_height), Resampling.LANCZOS
            )

            # crop the left and right of the picture to keep image and screen ration equal
            pixels_to_cut = int((new_image_width - screen_width) / 2)
            left = pixels_to_cut
            top = 0
            right = new_image_width - pixels_to_cut
            bottom = new_image_height
            # Crop the image
            self.image = self.image.crop((left, top, right, bottom))

        # if image rations are the same
        else:
            # transform the image to ensure it is the same size as our screen
            self.image = self.image.resize(
                (screen_width, screen_height), Image.ANTIALIAS
            )

        # reset draw as the image has mutated
        self.draw = ImageDraw.Draw(self.image)

    def _write_text(self, position, text, font):
        self.draw.text(position, text=text, fill=self.fill, font=font)

    def _font_pixel_size(self, text, font):
        return self.draw.textsize(text, font)
