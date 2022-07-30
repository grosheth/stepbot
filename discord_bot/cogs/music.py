from discord.ext import commands
import youtube_dl
import discord, aiohttp
from pymongo import MongoClient
from settings import CONN_STRING
from utils import *

url_list = []

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!track")
    async def spotify_track(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        print(spotify_result)
        if spotify_result is None:
            await ctx.send(f"{user.name} is not listening to spotify.")
            return
        await ctx.send(f"https://open.spotify.com/track/{spotify_result.track_id}")
    
    
    @commands.command(brief="!disconnect")
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()


    @commands.command(brief="!play <url> pour jouser de la music")
    async def play(self, ctx, url):

        url_list.append(url)
        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Tu decide po.")
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client


        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(x, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,
            **FFMPEG_OPTIONS)
            await vc.play(source)



def setup(bot):
    bot.add_cog(Music(bot))