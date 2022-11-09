from discord.ext import commands
import discord
from settings import FILOU
from utils import open_file

class Moderator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        
    @commands.command(brief="!ban @<member>")
    async def ban(self, ctx, member: discord.Member):
        current_count = get_amount(ctx.author.id, "Memes")
        add_to_db(ctx.author.id, current_count, 1, "Memes")
        if ctx.author.id == int(FILOU):
            message = await open_file("ban.json", "filou")
            
            await ctx.send(message)
        else:
            await ctx.send(f"Motherland says no to you {ctx.author.name}")


def setup(bot):
    bot.add_cog(Moderator(bot))
