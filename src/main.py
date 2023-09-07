import os, discord, dotenv, asyncio
from discord.ext import commands
from settings import *
from mongoengine import *
from pymongo import MongoClient

dotenv.load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# load files in cogs folder
async def setup():
    try:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await bot.load_extension(f'cogs.{filename[:-3]}')
    except:
        for filename in os.listdir("./src/cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await bot.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(setup())

bot.run(TOKEN)
