FILE="$(cd "$(dirname "$0")" && pwd)/run-mac.sh"
(crontab -l 2>/dev/null; echo "* * * * * $FILE >/tmp/language-wallpaper-stdout.log 2>/tmp/language-wallpaper-stderr.log") | crontab -