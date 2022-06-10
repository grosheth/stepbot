from discord.ext import commands

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('---------')
        print(f" Chu pra")
        print('---------')


    @commands.Cog.listener()
    async def on_voice_channel_update(self,member,before,after):
        if member.bot:
            return

def setup(bot):
    bot.add_cog(Activities(bot))