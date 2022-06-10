import json, os, random
from unicodedata import category
from settings import *




async def get_mom_joke():
    with open(os.path.join(WORDBANK_DIR, "mama.json")) as f:
        jokes = json.load(f)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult

async def get_quote():
    with open(os.path.join(WORDBANK_DIR, "beer.json")) as f:
        quotes = json.load(f)
    quote = random.choice(list(quotes["beer"]))
    return quote