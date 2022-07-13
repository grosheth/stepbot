import asyncio
from discord.ext import commands
from random import randint
from pymongo import MongoClient
from settings import CONN_STRING
from utils import *

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!coinflip <pile> <face>")
    async def coinflip(self, ctx, arg):
        arg = arg.lower()
        if arg != "pile" and arg != "face":
            await ctx.send(f"{arg} n'est pas un choix à Pile ou face. Monsieur soleil")
            return
        
        guesses = {
            1:"pile",
            2:"face"
        }
        guess = randint(1,2)
        await asyncio.sleep(1)
        await ctx.send("...La tension monte...")
        await asyncio.sleep(2)
        
        if ctx.author.id == int(FILOU):
            await ctx.send("...pas comme la molle a Filou...")
        await ctx.send(guesses[guess])

        if guesses[guess] == arg:
            await asyncio.sleep(1)
            await ctx.send("Bravo, Pussi Conqueror")
        else:
            await asyncio.sleep(1)
            await ctx.send("CACHING MUFAKA")


    @commands.command(brief="!rr Russian roulette")
    async def rr(self, ctx):       
        await ctx.send("Tu gagne 1000 Nanane si tu meur pas. Tu perd 5000 Nanane si tu tfa shot.")
        
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

            current_cash = get_cash(member.id)
            shot = randint(1,6)

            await ctx.send(f'{member.name} {await open_file("russianroulette.json","opening")}')
            await asyncio.sleep(1)
            if shot == 1:
                lose_money(member.id, current_cash, 5000)
                await ctx.send(f'{member.name} {await open_file("russianroulette.json","dead")}')
                await ctx.send(f'{member.name} Ta pardu tes Nanane sti de laid')
                await asyncio.sleep(1)
                await member.move_to(None)
                return
            else:
                if member.id == int(FILOU):
                    lose_money(member.id, current_cash, 500)            
                else:
                    win_money(member.id, current_cash, 1000)
                await ctx.send(f"click...")
                await asyncio.sleep(1)
                await ctx.send(f'{await open_file("russianroulette.json","alive")}')

        await asyncio.sleep(1)
        await ctx.send(f"Parsonne est mort")
        return


def setup(bot):
    bot.add_cog(Games(bot))