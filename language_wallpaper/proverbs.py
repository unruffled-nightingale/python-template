import re
from random import choice, randint

import requests
from bs4 import BeautifulSoup


def get_quote():
    return choice(get_quotes())


def get_proverb():
    return choice(get_proverbs())


def get_quotes():
    page = randint(1, 100)
    url = "https://www.goodreads.com/quotes?page={0}".format(page)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    # Scrape quotes from the website
    quotes = [
        re.findall("(?<=“).*(?=”)", e.text)[0]
        for e in soup.find_all("div", {"class": "quoteText"})
    ]
    # Remove any quotes that are None, or are longer than 100 characters
    quotes = [quote for quote in quotes if quote is not None and len(quote) < 100]
    return quotes


def get_proverbs():
    url = "https://en.wikiquote.org/wiki/english_proverbs"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    soup = soup.find_all("div", {"class": "mw-parser-output"})[0]
    proverbs = []
    for soup in soup.find_all("ul", recursive=False):
        soup = soup.find_all("li", recursive=False)
        for element in soup:
            [s.extract() for s in element("ul")]
        proverbs = proverbs + [e.text for e in soup]
    # Small hack - last 11 are rubbish that we do not want.
    proverbs = [clean_proverb(e) for e in proverbs[0:-11] if len(e) < 100]
    return proverbs


def clean_proverb(proverb):
    # Remove any brackets and any text contained within them.
    return re.sub("\\s?\\(.*\\)", "", proverb).strip()
