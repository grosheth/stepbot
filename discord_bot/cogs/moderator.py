from discord.ext import commands
import discord
from settings import FILOU
from utils import create_voice_channel, open_file

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief="!ban @<member>")
    async def ban(self, ctx, member: discord.Member):
        
        if ctx.author.id == int(FILOU):
            message = await open_file("ban.json", "filou")
            await ctx.send(message)
        else:
            await ctx.send(f"Motherland says no to you {ctx.author.name}")
def setup(bot):
    bot.add_cog(Moderator(bot))
