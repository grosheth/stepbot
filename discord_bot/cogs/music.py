from discord.ext import commands
import spotipy

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!play play music from spotify (notdone)")
    async def play():
        
        return

def setup(bot):
    bot.add_cog(Music(bot))