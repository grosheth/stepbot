from discord.ext import commands
import discord, aiohttp
from pymongo import MongoClient
from settings import CONN_STRING

class Wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!wallet shows you ton nombre de Nanane")
    async def wallet(self, ctx):
        connect = MongoClient(CONN_STRING)
        db = connect.discord
        collection = db.wallet
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                print(member.id)
                current_cash = collection.find_one({'_id': member.id})['Nanane']
        await ctx.send(f"Ton wallet est à: {current_cash} Nanane")
        if current_cash < 25000:
            await sleep(1)
            await ctx.send(f"Sti d'pauvre")

    @commands.command(brief="!wallets shows you toute les Nanane")
    async def wallets(self, ctx):

        connect = MongoClient(CONN_STRING)
        embed = discord.Embed(title="Vla les Nanane")
        db = connect.discord
        collection = db.wallet
        
        for member in ctx.guild.members:
            if member.bot:
                continue

            current_cash = collection.find_one({'_id': member.id})['Nanane']
            print(member.id, member.name, current_cash)
            embed.add_field(name=f'**{member.name}**', value=f'> **{current_cash}**',inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wallet(bot))