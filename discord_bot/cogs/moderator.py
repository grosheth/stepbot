from discord.ext import commands
import discord
from settings import FILOU

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def ban(self, ctx, member: discord.Member):
        if ctx.author.id == FILOU:
            ctx.send("haha ben oui Filou")
        return

def setup(bot):
    bot.add_cog(Moderator(bot))