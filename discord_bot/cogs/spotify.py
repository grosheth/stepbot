from discord.ext import commands
import discord, aiohttp
from pymongo import MongoClient
from settings import CONN_STRING
from utils import *

class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!track")
    async def track(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        print(spotify_result)
        if spotify_result is None:
            await ctx.send(f"{user.name} is not listening to spotify.")
            return
        await ctx.send(f"https://open.spotify.com/track/{spotify_result.track_id}")



def setup(bot):
    bot.add_cog(Spotify(bot))