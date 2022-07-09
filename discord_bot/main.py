import os, discord, dotenv
from discord.ext import commands
from settings import *
from mongoengine import *
from pymongo import MongoClient

dotenv.load_dotenv()

# connect = MongoClient(host="192.168.2.101", port=30011, username="admin", password="admin")

#connect(DB, host=HOST, port=int(PORT), username=DBUSER, password=DBPASS)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# load files in cogs folder
for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)