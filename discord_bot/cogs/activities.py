from discord.ext import commands
from utils import *
from settings import *
import youtube_dl, discord
from pymongo import MongoClient

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('---------')
        print(f" Chu pra")
        print('---------')


    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        voice_channel = member.voice.channel
        vc = discord.utils.get(self.bot.voice_clients)
        await vc.disconnect()
        if member.bot:
            if not before.channel:
                print(f'Bot {member.name} joined {after.channel.name}')

        else:
            if not before.channel:
                print(f'{member.name} joined {after.channel.name}')

            if before.channel and after.channel:
                if before.channel.id != after.channel.id:
                    print("bot switched channel")
                else:
                    print("somethin else happened")
                    if member.voice.self_stream:
                        print(f"{member.name} started streaming")
                    if member.voice.self_deaf:
                        print("User deafened")

        if member.id == int(CORBIN):
            url = "https://www.youtube.com/watch?v=U06jlgpMtQs"

        elif member.id == int(ALESS):
            url = "https://www.youtube.com/watch?v=aT5JaB5agSE"
            
        elif member.id == int(RURU):
            url = "https://www.youtube.com/watch?v=wrdK57qgNqA"
        
        elif member.id == int(FILOU):
            url = "https://www.youtube.com/watch?v=9_o4_4fwbpU"

        elif member.id == int(PEPI):
            url = "https://www.youtube.com/watch?v=mtToc5EmSho"

        elif member.id == int(MARTIN):
            url = "https://www.youtube.com/watch?v=mtToc5EmSho"

        else:
            url = ""

        await voice_channel.connect()
        vc = discord.utils.get(self.bot.voice_clients)
        vc.stop()

        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}


        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,
            **FFMPEG_OPTIONS)
            vc.play(source)

def setup(bot):
    bot.add_cog(Activities(bot))