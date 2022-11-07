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
    async def feet_stats(self, ctx):
        for member in ctx.guild.members:
            if member.id == ctx.author.id:
                current_amount = get_amount(member.id, "Feet")
        await ctx.send(f"Toi appeller les pieds: {current_amount} fois")

def setup(bot):
    bot.add_cog(Stats(bot))
