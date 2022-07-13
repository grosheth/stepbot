from discord.ext import commands
import discord, aiohttp
from pymongo import MongoClient
from settings import CONN_STRING
from utils import *

class Wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!wallet shows you ton nombre de Nanane")
    async def wallet(self, ctx):
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                current_cash = get_cash(member.id)
        await ctx.send(f"Ton wallet est à: {current_cash} Nanane")
        if current_cash < 25000:
            await sleep(1)
            await ctx.send(f"Sti d'pauvre")


    @commands.command(brief="!wallets shows you toute les Nanane")
    async def wallets(self, ctx):
        async with ctx.channel.typing():
            embed = discord.Embed(title="Vla les Nanane")
            for member in ctx.guild.members:
                if member.bot:
                    continue
                current_cash = get_cash(member.id)
                print(member.id, member.name, current_cash)
                embed.add_field(name=f'**{member.name}**', value=f'> **{current_cash}**',inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wallet(bot))