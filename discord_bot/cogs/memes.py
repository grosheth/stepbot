from discord.ext import commands
from random import randint


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!memes get fuckt")
    async def memes(self, ctx):
        memes = {
                1:"https://www.pornhub.com/categories/hentai",
                2:"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                3:"https://www.youtube.com/watch?v=jDwVkXVHIqg",
                4:"https://www.youtube.com/watch?v=N6hVmn9FM7o"
            }
        
        await ctx.send(memes[randint(1, len(memes))])

def setup(bot):
    bot.add_cog(Memes(bot))