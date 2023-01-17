DIR="$(cd "$(dirname "$0")" && pwd)/"
source $DIR../venv/bin/activate
python3 $DIR../language_wallpaper/main.py
deactivate
