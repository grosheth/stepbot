import os, discord, dotenv
from discord.ext import commands


dotenv.load_dotenv()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# load files in cogs folder
for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and filename != "__init__.py":
		bot.load_extension(f'cogs.{filename[:-3]}')

async def on_ready(self):
    print('Logged in as')
    print(bot.user.name)
    print('------')
    print(f"Chu pra")

async def on_message(self, message):
    if message.author.bot:
        return

    if message.content[0] != os.getenv("PREFIX"):
        return

    if message.content == os.getenv("PREFIX"):
        await message.channel.send(embed=discord.Embed(title="Hello I am, P0u55i5l4y3r. Summon me using '!'", description="Feet adorer, womanizer, Short longsword, can do the drapeau. Arch Ennemy: Nick Gingras. Pioussi is the quest, pioussi is the Graal.", color=0xeeafe6))
    


bot.run(os.getenv("TOKEN"))