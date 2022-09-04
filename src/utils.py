import json, os, random
from pymongo import MongoClient
from settings import *


def db_connection():
    connect = MongoClient(CONN_STRING)
    collection = connect.discord.wallet
    return collection


def get_cash(member_id):
    collection = db_connection()
    current_cash = collection.find_one({'_id': member_id})['Nanane']
    return current_cash


def lose_money(member_id, current_cash, win):
    collection = db_connection()
    collection.update_one({'_id': member_id},{'$set': {'Nanane': current_cash - win}}, upsert=False)


def win_money(member_id, current_cash, loss):
    collection = db_connection()
    collection.update_one({'_id': member_id},{'$set': {'Nanane': current_cash + loss}}, upsert=False)

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
