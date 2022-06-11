import json, os, random
from settings import *


async def create_text_channel(guild, channel_name):
    await guild.create_text_channel(channel_name)
    channel = get_channel_by_name(guild, channel_name)
    return channel


async def create_voice_channel(guild, channel_name, user_limit=1):
    await guild.create_voice_channel(channel_name, user_limit=user_limit)
    channel = get_channel_by_name(guild, channel_name)
    return channel


async def get_channel_by_name(guild, channel_name):
    channel = None
    for c in guild.channels:
        if c.name == channel_name.lower():
            channel = c
            break
        return channel


async def open_file(file, category):
    print(file, type(file), category, type(category), WORDBANK_DIR, type(WORDBANK_DIR))
    with open(os.path.join(WORDBANK_DIR, file)) as f:
        jokes = json.load(f)
    opening = random.choice(list(jokes[category]))
    return opening


async def get_mom_joke():
    with open(os.path.join(WORDBANK_DIR, "mama.json")) as f:
        jokes = json.load(f)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult
