from language_wallpaper.proverbs import get_proverb, get_quote


def test_proverbs():
    proverb = get_proverb()
    assert type(proverb) == str
    assert len(proverb) > 10


def test_quotes():
    quote = get_quote()
    assert type(quote) == str
    assert len(quote) > 10
