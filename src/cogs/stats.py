import asyncio
from sys import executable
from discord.ext import commands
from utils import *
from settings import *
import discord

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!specs_on_seggs")
    async def specs_on_seggs(self, ctx):
        messages = await ctx.history(limit=1).flatten()
        print(messages)
        
        pass

def setup(bot):
    bot.add_cog(Stats(bot))
