import asyncio
from sys import executable
from discord.ext import commands
from utils import *
from settings import *
import youtube_dl, discord

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

        try:
            await voice_channel.connect()
        except:
            vc = discord.utils.get(self.bot.voice_clients)
            vc.stop()
        
        if member.bot:
            if not before.channel:
                print(f'Bot {member.name} joined {after.channel.name}')

        else:
            if not before.channel:
                print(f'{member.name} joined {after.channel.name}')

                if member.id == int(CORBIN):
                    intro = "intros/intro_corbin.mp3"

                elif member.id == int(ALESS):
                    intro = "intros/intro_corbin.mp3"
                    
                elif member.id == int(RURU):
                    intro = "intros/intro_ruel.mp3"

                elif member.id == int(FILOU):
                    intro = "intros/intro_filou.mp3"

                elif member.id == int(PEPI):
                    url = "https://www.youtube.com/watch?v=Y4kNfv7cUA8"
                    time = 10

                elif member.id == int(MARTIN):
                    url = "https://www.youtube.com/watch?v=mtToc5EmSho"
                    time = 10

                elif member.id == int(BRIDO):
                    url = "https://www.youtube.com/watch?v=aT5JaB5agSE"
                    time = 10
                else:
                    intro = ""

                vc = discord.utils.get(self.bot.voice_clients)
                vc.play(await discord.FFmpegOpusAudio.from_probe(intro , executable="ffmpeg"))
                await asyncio.sleep(5)
                vc.stop()

            if before.channel and after.channel:
                if before.channel.id != after.channel.id:
                    print("switched channel")
                    return
                else:
                    print("somethin else happened")
                    if member.voice.self_stream:
                        print(f"{member.name} started streaming")
                        return
                    if member.voice.self_deaf:
                        print("User deafened")
                        return

def setup(bot):
    bot.add_cog(Activities(bot))
