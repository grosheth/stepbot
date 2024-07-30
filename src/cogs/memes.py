from asyncio.tasks import sleep
from discord.ext import commands
import discord, aiohttp, asyncio
import datetime
from utils import *
from random import randint
import os

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!insult @<user>")
    async def insult(self, ctx, member: discord.Member = None):
        # current_count = get_amount(ctx.author.id, "Memes")
        # add_to_db(ctx.author.id, current_count, 1, "Memes")
        insult = await get_mom_joke()
        await ctx.send(f"{member.display_name} {insult}")

    @commands.command(brief="!quote sends a beer quote with image")
    async def quote(self, ctx):
        # current_count = get_amount(ctx.author.id, "Memes")
        # add_to_db(ctx.author.id, current_count, 1, "Memes")
        quote = await open_file("beer.json", "beer")
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://picsum.photos/1000/1000") as r:
                    embed = discord.Embed(title=quote)
                    embed.set_image(url=r._real_url)
                    await ctx.send(embed=embed)

    @commands.command(brief="!ban @<member>")
    async def ban(self, ctx, member: discord.Member):
        # current_count = get_amount(ctx.author.id, "Memes")
        # add_to_db(ctx.author.id, current_count, 1, "Memes")
        if ctx.author.id == int(FILOU):
            message = await open_file("ban.json", "filou")
            await ctx.send(message)
        else:
            await ctx.send(f"Motherland says no to you {ctx.author.name}")

    @commands.command(brief="!filou filou is... something")
    async def filou(self, ctx):
        message = "Filou may be causing harm or disruption to the community on the discord server.They may be spreading negativity, causing drama, or breaking rules. This can create a toxic environment and make it difficult for other members to enjoy the server. Additionally, Filou's presence may be discouraging other users from joining or participating in the server. In order to maintain a positive and inclusive community, it may be best for Filou to leave the discord server. It is important to have a healthy and peaceful environment for all members to participate and enjoy."
        if ctx.author.id == int(FILOU):
            message = await open_file("ban.json", "filou")
            await ctx.send(message)
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="ChatGPT says:", description=message, color=0xEEAFE6
                )
            )

    @commands.command(brief="!whoyou Stepbot se présente")
    async def whoyou(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="What are you doing stepbot?? UwU",
                description="Feet adorer, womanizer, Short longsword, can do the drapeau, gets stuck in washing machine and windows(I use Arch btw). Nemesis: Nick Gingras.",
                color=0xEEAFE6,
            )
        )

    @commands.command(brief="!vachier va chier")
    async def vachier(self, ctx):
        await ctx.send(
            embed=discord.Embed(
                title="va chier", description="va chier.", color=0xEEAFE6
            )
        )

    @commands.command(brief="!barbade RURU Senvo")
    async def barbade(self, ctx):
        now = datetime.datetime.now()
        byebye = datetime.datetime(2024, 7, 30, 12)
        time_left = datetime.datetime(2024, 7, 30, 12) - now
        if now < byebye:
            await ctx.send(f"Ruru bebye dans: {time_left}")
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="La Barbada", description="Ruru already byebye :(", color=0xEEAFE6
                )
            )

    @commands.command(brief="!tokebecicitte")
    async def ciao_le_barbadais(self, ctx, bot):
        if ctx.author.id == int(MARTIN):
            await ctx.send("T pas Papa tu peut pas bannir un Barbadais.")
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="It's the final countdown", description="Tanana nanana nanana nananana", color=0xEEAFE6
                )
            )
            await ctx.send(f"Tanana nanana nanana nanananan")
            await ctx.send(f"5")
            await asyncio.sleep(2)
            await ctx.send(f"4")
            await asyncio.sleep(2)
            await ctx.send(f"3")
            await asyncio.sleep(2)
            await ctx.send(f"2")
            await asyncio.sleep(2)
            await ctx.send(f"1")
            await asyncio.sleep(2)
            await ctx.send(f":)")
            await asyncio.sleep(2)
            await bot.kick(RURU)



async def setup(bot):
    await bot.add_cog(Memes(bot))
