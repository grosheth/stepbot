import asyncio
from sys import executable
from discord.ext import commands
from utils import *
from settings import *
import discord

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
        # voice_channel = member.voice.channel
        print(f"self: {self}")
        print(f"member: {member}")

        # retry with try catch on PI
        try:
            voice_channel = member.voice.channel
        except:
            print(f'{member.name} Quitted')
        
        try:
            bot_voice_channel = await voice_channel.connect()
        except:
            bot_voice_channel = discord.utils.get(self.bot.voice_clients)
            bot_voice_channel.stop()

        if member.bot:
            if not before.channel:
                print(f'Bot {member.name} joined {after.channel.name}')
        else:
            if not before.channel:
                print(f'{member.name} joined {after.channel.name}')

                if member.id == int(CORBIN):
                    intro = "src/intros/intro_corbin.mp3"

                elif member.id == int(ALESS):
                    intro = "src/intros/intro_aless.mp3"

                elif member.id == int(RURU):
                    intro = "src/intros/intro_ruel.mp3"

                elif member.id == int(FILOU):
                    intro = "src/intros/intro_filou.mp3"

                elif member.id == int(REN):
                    intro = "src/intros/intro_ren.mp3"

                elif member.id == int(MARTIN):
                    intro = "src/intros/rdoute.mp3"

                elif member.id == int(BRIDO):
                    intro = "src/intros/intro_brido.mp3"
                else:
                    intro = ""

                bot_voice_channel = discord.utils.get(self.bot.voice_clients)
                print(f"bot_voice_channel {bot_voice_channel}")
                if bot_voice_channel != None:
                    bot_voice_channel.play(await discord.FFmpegOpusAudio.from_probe(intro , executable="ffmpeg"))
                    await asyncio.sleep(5)
                    bot_voice_channel.stop()

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

async def setup(bot):
    await bot.add_cog(Activities(bot))
