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
                await ctx.sendembed=discord.Embed(title="Voila coco tes stats de pedo? UwU",
                                                    description=
                                                    f"You have called the reddits: {current_amount_reddit} fois, You have been a foot pervert: {current_amount_feet} fois, You called the meme {current_amount_memes} fois",
                                                    color=0xeeafe6)


def setup(bot):
    bot.add_cog(Stats(bot))
