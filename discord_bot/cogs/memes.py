from discord.ext import commands
from random import randint
import discord, aiohttp
from utils import get_mom_joke, open_file

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!memes get fuckt")
    async def memes(self, ctx):
        memes = {
                1:"https://www.pornhub.com/categories/hentai",
                2:"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                3:"https://www.youtube.com/watch?v=jDwVkXVHIqg",
                4:"https://www.youtube.com/watch?v=N6hVmn9FM7o",
                5: "https://www.youtube.com/watch?v=zNtr0RahRqM"
            }
        
        await ctx.send(memes[randint(1, len(memes))])

    @commands.command(brief="!insult @<user>")
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_mom_joke()
        await ctx.send(f"{member.display_name} {insult}")

    @commands.command(brief="!quote sends a beer quote with image")
    async def quote(self, ctx):
        quote = await open_file("beer.json", "beer")
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://picsum.photos/1000/1000") as r:
                    embed = discord.Embed(title=quote)
                    embed.set_image(url=r._real_url)
                    await ctx.send(embed=embed)
                    
    @commands.command(brief="!whoyou PoussySlayer se présente")
    async def whoyou(self, ctx):
        await ctx.send(embed=discord.Embed(title="Hello I am, P0u55i5l4y3r. Summon me using '!'",
                                                    description=
                                                    "Feet adorer, womanizer, Short longsword, can do the drapeau. Arch Ennemy: Nick Gingras. Pioussi is the quest, pioussi is the Graal.",
                                                    color=0xeeafe6))

    @commands.command(brief="!feet PoussySlayer se présente")
    async def feet(self, ctx):
        



def setup(bot):
    bot.add_cog(Memes(bot))