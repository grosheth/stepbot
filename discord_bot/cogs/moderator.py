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
            await create_voice_channel(ctx.author.guild, f"{ctx.author.name}-PARDANT", user_limit=1)
            await ctx.send(message)
        else:
            # await create_voice_channel(ctx.author.guild, f"{member.name}-PARDANT", user_limit=1)
            await ctx.send(f"Motherland says no to you {ctx.author.name}")
def setup(bot):
    bot.add_cog(Moderator(bot))
