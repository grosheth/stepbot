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
        print(member)
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

        if member.id == int(ALESS):
            print(f"get user {member} {ALESS} song")
            url = "https://www.youtube.com/watch?v=U06jlgpMtQs"

            if not before.channel:
                print(f'Bot {member.name} joined {after.channel.name}')

            voice_channel = member.voice.channel
            await voice_channel.connect()

            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format':"bestaudio"}
            vc = member.voice.channel

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,
                **FFMPEG_OPTIONS)
                vc.play(source)


def setup(bot):
    bot.add_cog(Activities(bot))