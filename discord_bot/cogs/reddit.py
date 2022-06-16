from discord.ext import commands
import praw, random, discord, asyncio
from settings import REDDIT_ID, REDDIT_SECRET

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_ID and REDDIT_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_ID,client_secret=REDDIT_SECRET, user_agent="DISCORD_BOT:%s1.0" % REDDIT_ID)

    @commands.command(brief="!reddit then specify the subreddit")
    async def reddit(self, ctx, arg):
        channel = arg
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit(channel).hot()
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.title)
                await ctx.send(submission.url)

    @commands.command(brief="!fiftyfifty Send a reddit post from r/fiftyfifty")
    async def fiftyfifty(self, ctx):
        await ctx.send("fiftyfifty incoming")
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("fiftyfifty").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.title)
                await asyncio.sleep(5)
                await ctx.send(submission.url)

                
    @commands.command(brief="!feet Send a reddit post from r/feetishh")
    async def feet(self, ctx):
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("feetishh").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.title)
                await asyncio.sleep(5)
                await ctx.send(submission.url)


def setup(bot):
    bot.add_cog(Reddit(bot))