from discord.ext import commands
import discord, aiohttp, asyncio
from utils import *
from random import randint
import os

class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!creme Envoie un extrait de creme dans le voice channel")
    async def creme(self, ctx):

        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Ta pas de creme.")

        cremes = os.listdir("src/creme/")
        voice_channel = ctx.author.voice.channel
        audio = f"src/creme/{cremes[randint(1,len(cremes))]}"

        try:
            await voice_channel.connect()
        except:
            await ctx.voice_client.move_to(voice_channel)

        vc = discord.utils.get(self.bot.voice_clients)
        await get_mp3(vc, audio)
 

    @commands.command(brief="!sb CYKA BLYET")
    async def sb(self, ctx, sound = None):
        try:
            # Searching path for volume inside container files
            path = "/mnt/sb/"
            random = os.listdir(f"{path}")
        except:
            # Searching for local files
            path = "src/soundboard/"
            random = os.listdir(f"{path}")

        if sound == 'list':
            random = '\n'.join(random)
            await ctx.send(embed=discord.Embed(title="Soundboard List", description=f"{random}", color=0xeeafe6, type='rich', url='https://www.youtube.com/watch?v=xm3YgoEiEDc'))
        else:
            if ctx.author.voice is None:
                await ctx.send("T po dans l'channel, Ta pas de soundboard")

            if sound is None:
                audio = f"{path}{random[randint(1,len(random))]}"
                print(f"Trying to play {audio}")
            else:
                audio = f"{path}{sound}.mp3"
                print(f"Trying to play {audio}")

            # Connect to voice channels
            voice_channel = ctx.author.voice.channel

            try:
                await voice_channel.connect()
            except:
                await ctx.voice_client.move_to(voice_channel)

            # Playing Audio
            vc = discord.utils.get(self.bot.voice_clients)
            await get_mp3(vc, audio)


    @commands.command(brief="!sucela SUCELA")
    async def sucela(self, ctx):

        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Toé sucela.")

        path = os.listdir("src/sucela/")
        voice_channel = ctx.author.voice.channel
        audio = f"src/sucela/{path[randint(1,len(path))]}"
        print(f"Now playing : {audio}")

        try:
            await voice_channel.connect()
        except:
            await ctx.voice_client.move_to(voice_channel)

        vc = discord.utils.get(self.bot.voice_clients)
        await get_mp3(vc, audio, 10)


    @commands.command(brief="!tibizou Bonne nuit")
    async def tibizou(self, ctx):

        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Pas de bonne nuit.")

        voice_channel = ctx.author.voice.channel
        audio = f"src/intros/tibizou.mp3"
        print(f"Now playing : {audio}")

        try:
            await voice_channel.connect()
        except:
            await ctx.voice_client.move_to(voice_channel)

        vc = discord.utils.get(self.bot.voice_clients)
        await get_mp3(vc, audio, 10)


async def setup(bot):
    await bot.add_cog(Audio(bot))
