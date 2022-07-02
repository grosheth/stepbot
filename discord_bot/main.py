import os, discord, dotenv
from sqlite3 import connect
from discord.ext import commands
from settings import *


dotenv.load_dotenv()

# connect('discord', host='192.168.2.101', port=30011, username='admin', password='admin', authentication_source='admin')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# load files in cogs folder
for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)