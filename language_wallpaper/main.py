import json
import logging
import time
from pathlib import Path
from random import choice
from typing import Dict, List

from language_wallpaper.image_editor import ImageEditor
from language_wallpaper.proverbs import get_proverb, get_proverbs, get_quotes
from language_wallpaper.translations.translations import TranslationException, get_text
from language_wallpaper.wallpaper_controller.wallpaper_controller import get_wallpaper_controller

logging.basicConfig(level=logging.INFO)


DATA_DIR = Path(__file__).parent / ".." / "resources" / "data"
IMAGE_DIR = Path(__file__).parent / ".." / "resources" / "images"
BASE_IMAGE = "default.jpeg"


def run(language: str, os: str = "mac", image_path: str = None):
    logging.info(f"Running {language} language wallpaper...")
    prebuilt_data = Path(__file__).parent / DATA_DIR / f"{language}.json"
    if prebuilt_data.is_file():
        logging.info("Collecting data from prebuilt file...")
        data = choice(json.loads(prebuilt_data.read_text()))
    else:
        logging.info("Building data from external APIs...")
        proverb = get_proverb()
        data = get_text(language, proverb)
    logging.info("Data collected")

    logging.info("Building wallpaper image...")
    if image_path is None:
        image_path = IMAGE_DIR / BASE_IMAGE
    image_editor = ImageEditor(image_path, data)
    image_editor.write_text_to_image()
    logging.info("Wallpaper image build")

    logging.info("Saving wallpaper image...")
    filename = Path(__file__).parent / IMAGE_DIR / f"wallpaper-{int(time.time())}.jpg"
    image_editor.save(filename)
    logging.info("Wallpaper image saved")

    logging.info("Setting wallpaper...")
    get_wallpaper_controller(os).set_desktop_background(str(filename))
    logging.info("Wallpaper set")


def build_language_data(language: str, max_calls: int = 10):
    logging.info(f"Loading existing {language} wallpaper data...")
    data_dir = Path(__file__).parent / DATA_DIR
    succeeded_file = data_dir / f"{language}.json"
    failed_file = data_dir / f"{language}-failed.json"

    existing_succeeded = read_file(succeeded_file)
    existing_failed = read_file(failed_file)

    seen_phrases = [e["phrase"] for e in existing_succeeded] + [
        e["phrase"] for e in existing_failed
    ]
    logging.info(f"Existing {language} wallpaper data loaded")

    logging.info("Retrieving proverbs data...")
    results = get_proverbs() + get_quotes()
    new_phrases = [e for e in results if e not in seen_phrases][0:max_calls]
    logging.info(f"Retrieved {len(new_phrases)} new proverbs")

    succeeded = []
    failed = []

    for p in new_phrases:
        logging.info(f"Retrieving language information for proverb - `{p}`...")
        try:
            logging.info("Successfully retrieved language data")
            succeeded.append(get_text(language, p))
        except TranslationException as e:
            logging.info(f"Failed to language data - {e}")
            failed.append({"phrase": p, "error": str(e)})

    logging.info("Writing data to file...")
    succeeded_file.write_text(json.dumps(succeeded + existing_succeeded))
    failed_file.write_text(json.dumps(failed + existing_failed))
    logging.info("Data written to file")


def read_file(file_path: Path) -> List[Dict]:
    if file_path.is_file():
        return json.loads(file_path.read_text())
    else:
        file_path.touch()
        return []


if __name__ == "__main__":
    run("French", "mac")
