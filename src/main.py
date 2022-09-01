import os, discord, dotenv
from discord.ext import commands
from settings import *
from mongoengine import *
from pymongo import MongoClient

dotenv.load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# load files in cogs folder
try:
	for filename in os.listdir("./cogs"):
		if filename.endswith(".py") and filename != "__init__.py":
			bot.load_extension(f'cogs.{filename[:-3]}')
except:
        for filename in os.listdir("./discord_bot/cogs"):
                if filename.endswith(".py") and filename != "__init__.py":
                        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
