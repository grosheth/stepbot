import asyncio
from sys import executable
from discord.ext import commands
from utils import *
from settings import *
import discord

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!Number of time you called !feet")
    async def feet_stats(self, ctx):
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                current_amount = get_amount(member.id, "Feet")
        await ctx.send(f"Toi appeller les pieds: {current_amount} fois")


    @commands.command(brief="Number of time you called !memes")
    async def memes_stats(self, ctx):
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                current_amount = get_amount(member.id, "Memes")
        await ctx.send(f"Toi appeller les memes: {current_amount} fois")


    @commands.command(brief="Number of time you called !reddit")
    async def reddit_stats(self, ctx):
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                current_amount = get_amount(member.id, "Reddit")
        await ctx.send(f"Toi appeller les reddits: {current_amount} fois")


    @commands.command(brief="Number of time you called !reddit")
    async def stats(self, ctx):
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                current_amount_reddit = get_amount(member.id, "Reddit")
                current_amount_feet = get_amount(member.id, "Feet")
                current_amount_memes = get_amount(member.id, "Memes")
                current_amount_shemale = get_amount(member.id, "Shemale")
                current_amount_hentai = get_amount(member.id, "Hentai")
                await ctx.send(embed=discord.Embed(title="Voila coco tes stats de pedo UwU",
                                                    description=
                                                    f"You called the reddits: {current_amount_reddit} fois,\n You have been a foot pervert: {current_amount_feet} fois,\n You called the memes {current_amount_memes} fois,\n You called the penis madame {current_amount_shemale} fois,\n You called the anime seggs {current_amount_hentai} fois",
                                                    color=0xeeafe6))


    @commands.command(brief="Erribody stets !stats_all")
    async def stats_all(self, ctx):
        async with ctx.channel.typing():
            embed = discord.Embed(title="Vla les Stats du Reddirty")
            for member in ctx.guild.members:
                if member.bot:
                    continue
                current_amount_reddit = get_amount(member.id, "Reddit")
                print(member.id, member.name, current_amount_reddit)
                embed.add_field(name=f'**{member.name} :**', value=f'> **{current_amount_reddit}**',inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Stats(bot))
