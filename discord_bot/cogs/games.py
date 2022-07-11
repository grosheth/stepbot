import asyncio
from discord.ext import commands
from random import randint
from pymongo import MongoClient
from settings import CONN_STRING
from utils import open_file, FILOU

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


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
        if ctx.author.id == int(FILOU):
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


    @commands.command(brief="!rr Russian roulette")
    async def rr(self, ctx):

        connect = MongoClient(CONN_STRING)
        db = connect.discord
        collection = db.wallet
        await ctx.send("Tu gagne 1 Nanane si tu meur pas. Tu perd 5 Nanane si tu tfa shot.")
        
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

            current_cash = collection.find_one({'_id': member.id})['Nanane']
            shot = randint(1,4)
            if member.bot:
                shot = 1

            await ctx.send(f"{member.name} {opening}")
            await asyncio.sleep(1)
            await ctx.send(f"...")
            await asyncio.sleep(2)
            if shot == 1:
                collection.update_one({'_id': member.id},{'$set': {'Nanane': current_cash - 50}}, upsert=False)
                await ctx.send(f'{member.name} {dead}')
                await asyncio.sleep(1)
                await member.move_to(None)
                return
            else:
                if member.id != int(FILOU):
                    collection.update_one({'_id': member.id},{'$set': {'Nanane': current_cash + 10}}, upsert=False)
                else:
                    collection.update_one({'_id': member.id},{'$set': {'Nanane': current_cash - 1}}, upsert=False)
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