from discord.ext import commands

class Wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!wallet to see how much you have on your wallet")
    async def wallet(self, ctx, arg):
        
        
        return

def setup(bot):
    bot.add_cog(Wallet(bot))