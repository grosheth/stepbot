from discord.ext import commands

class lottery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!lottery every samedi lottery winners")
    async def lottery(self, ctx):
        
        return
    

def setup(bot):
    bot.add_cog(lottery(bot))