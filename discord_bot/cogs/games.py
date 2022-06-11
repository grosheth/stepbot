import asyncio
from discord.ext import commands
from random import randint
from utils import get_channel_by_name, open_file, create_voice_channel

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!online <game>")
    async def online(self, ctx, arg):
        games = {
            1:"https://garticphone.com/lobby",
            2:"https://songtrivia2.io/",
            3:"https://world-geography-games.com/en/flags_world.html",
            4:"https://www.geoguessr.com/"
        }
        if arg == "gartic":
            await ctx.send(games[1])
        if arg == "songtrivia":
            await ctx.send(games[2])
        if arg == "flags":
            await ctx.send(games[3])
        if arg == "geo":
            await ctx.send(games[4])
        if arg == "random game":
            await ctx.send(games[randint(1, len(games))])


    @commands.command(brief="!coinflip <pile> <face>")
    async def coinflip(self, ctx, arg):
        arg = arg.lower()
        if arg != "pile" and arg != "face":
            await ctx.send(f"{arg} n'est pas un choix à Pile ou face. Bravo")
            return
        
        guesses = {
            1:"pile",
            2:"face"
        }
        guess = randint(1,2)
        await ctx.send("...")
        await asyncio.sleep(1)
        await ctx.send("...La tension monte...")
        if ctx.author.id == 388902413358071819:
            await ctx.send("...")
            await asyncio.sleep(1)
            await ctx.send("...pas comme la molle a Filou...")
        await asyncio.sleep(1)
        await ctx.send(guesses[guess])
        if guesses[guess] == arg:
            await asyncio.sleep(1)
            await ctx.send("Bravo, Pussi Conqueror")
        else:
            await asyncio.sleep(1)
            await ctx.send("Hélas, la maison l'emporte")


    @commands.command(brief="!russianroulette")
    async def rr(self, ctx):

        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Tu decide po.")
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        await ctx.send("Roulette Russe")
        await asyncio.sleep(1)
        for member in voice_channel.members:
            opening = await open_file("russianroulette.json","opening")
            dead = await open_file("russianroulette.json","dead")
            alive = await open_file("russianroulette.json","alive")
            shot = randint(1,6)
            if member.bot:
                shot = 0

            await ctx.send(f"{member.name} {opening}")
            await asyncio.sleep(1)
            await ctx.send(f"...")
            await asyncio.sleep(1)
            await ctx.send(f"...")
            await asyncio.sleep(2)
            if shot == 1:
                await ctx.send(f'{member.name} {dead}')
                #await create_voice_channel(member.guild, f"{member.name}-sti-dpardant")
                await asyncio.sleep(1)
                await member.move_to(None)
                return
            else:
                await ctx.send(f"click...")
                await asyncio.sleep(1)
                await ctx.send(f'{alive}')
                await asyncio.sleep(1)
                await ctx.send(f"...")

        await asyncio.sleep(1)
        await ctx.send(f"Parsonne est mort")                
        return

def setup(bot):
    bot.add_cog(Games(bot))