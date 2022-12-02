from discord.ext import commands
import discord, aiohttp
from utils import *
from random import randint
import os

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!insult @<user>")
    async def insult(self, ctx, member: discord.Member = None):
        current_count = get_amount(ctx.author.id, "Memes")
        add_to_db(ctx.author.id, current_count, 1, "Memes")
        insult = await get_mom_joke()
        await ctx.send(f"{member.display_name} {insult}")


    @commands.command(brief="!quote sends a beer quote with image")
    async def quote(self, ctx):
        current_count = get_amount(ctx.author.id, "Memes")
        add_to_db(ctx.author.id, current_count, 1, "Memes")
        quote = await open_file("beer.json", "beer")
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://picsum.photos/1000/1000") as r:
                    embed = discord.Embed(title=quote)
                    embed.set_image(url=r._real_url)
                    await ctx.send(embed=embed)


    @commands.command(brief="!ban @<member>")
    async def ban(self, ctx, member: discord.Member):
        current_count = get_amount(ctx.author.id, "Memes")
        add_to_db(ctx.author.id, current_count, 1, "Memes")
        if ctx.author.id == int(FILOU):
            message = await open_file("ban.json", "filou")
            await ctx.send(message)
        else:
            await ctx.send(f"Motherland says no to you {ctx.author.name}")


    @commands.command(brief="!creme Envoie un extrait de creme dans le voice channel")
    async def creme(self, ctx):

        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Ta pas de creme.")

        cremes = os.listdir("src/creme/")
        print(cremes)
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client
        intro = f"src/creme/{cremes[randint(1,len(cremes))]}"
        print(intro)

        try:
            await voice_channel.connect()
        except:
            await ctx.voice_client.move_to(voice_channel)

        vc = discord.utils.get(self.bot.voice_clients)
        await vc.play(await discord.FFmpegOpusAudio.from_probe(intro , executable="ffmpeg"))
        await asyncio.sleep(10)
        await vc.stop()


    # @commands.command(brief="!sucela SUCELA")
    # async def sucela(self, ctx):

    #     if ctx.author.voice is None:
    #         await ctx.send("T po dans l'channel, Toé sucela.")

    #     cremes = os.listdir("src/sucela/")
    #     print(cremes)
    #     voice_channel = ctx.author.voice.channel
    #     voice_client = ctx.voice_client
    #     intro = f"src/sucela/{cremes[randint(1,len(cremes))]}"
    #     print(intro)

    #     try:
    #         await voice_channel.connect()
    #     except:
    #         await ctx.voice_client.move_to(voice_channel)

    #     vc = discord.utils.get(self.bot.voice_clients)
    #     await vc.play(await discord.FFmpegOpusAudio.from_probe(intro , executable="ffmpeg"))
    #     await asyncio.sleep(10)
    #     await vc.stop()

    @commands.command(brief="!whoyou Stepbot se présente")
    async def whoyou(self, ctx):
        await ctx.send(embed=discord.Embed(title="What are you doing stepbot?? UwU",
                                                    description=
                                                    "Feet adorer, womanizer, Short longsword, can do the drapeau, gets stuck in washing machine and windows(I use Arch btw). Nemesis: Nick Gingras.",
                                                    color=0xeeafe6))

def setup(bot):
    bot.add_cog(Memes(bot))
