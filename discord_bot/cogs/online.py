from discord.ext import commands

class Online(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="!online goal is to start an online game lobby via APi's")
    async def online(self, ctx, arg):
        games = {
            1:"https://garticphone.com/lobby",
            2:"https://songtrivia2.io/",
            3:"https://world-geography-games.com/en/flags_world.html",
            4:"https://www.geoguessr.com/"
        }
        if arg == "gartic":
            await ctx.send(games[1])
        if arg == "songtrivia":
            await ctx.send(games[2])
        if arg == "flags":
            await ctx.send(games[3])
        if arg == "geo":
            await ctx.send(games[4])
        if arg == "random game":
            await ctx.send(games[randint(1, len(games))])

def setup(bot):
    bot.add_cog(Online(bot))