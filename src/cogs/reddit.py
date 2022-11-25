from discord.ext import commands
import praw, random, discord, asyncio
from settings import REDDIT_ID, REDDIT_SECRET, NSFW_CHANNEL
from utils import *

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_ID and REDDIT_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_ID,client_secret=REDDIT_SECRET, user_agent="DISCORD_BOT:%s1.0" % REDDIT_ID)


    @commands.command(brief="!reddit then specify the subreddit")
    async def reddit(self, ctx, arg):
        current_count = get_amount(ctx.author.id, "Reddit")
        add_to_db(ctx.author.id, current_count, 1, "Reddit")
        channel = arg
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit(channel).hot()
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                if submission.over_18 == True and ctx.channel.id != int(NSFW_CHANNEL):
                    await ctx.send("Oh mon vilain, pas très gentil pour les amis au travail ça. (ou dans l'autobus)")
                else:
                    await ctx.send(submission.title)
                    await ctx.send(submission.url)


    @commands.command(brief="!fiftyfifty Send a reddit post from r/fiftyfifty")
    async def fiftyfifty(self, ctx):
        current_count = get_amount(ctx.author.id, "Reddit")
        add_to_db(ctx.author.id, current_count, 1, "Reddit")
        await ctx.send("fiftyfifty incoming")
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("fiftyfifty").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                if submission.over_18 == True and ctx.channel.id != int(NSFW_CHANNEL):
                    print(ctx.channel.id)
                    await ctx.send("C'est pas très approprié comme message ça.")
                else:
                    await ctx.send(submission.title)
                    await asyncio.sleep(5)
                    await ctx.send(submission.url)

    @commands.command(brief="!feet Send a reddit post from r/feetishh")
    async def feet(self, ctx):
        current_count_feet = get_amount(ctx.author.id, "Feet")
        current_count_reddit = get_amount(ctx.author.id, "Reddit")
        add_to_db(ctx.author.id, current_count_feet, 1, "Feet")
        add_to_db(ctx.author.id, current_count_reddit, 1, "Reddit")
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("feetishh").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                if submission.over_18 == True and ctx.channel.id != int(NSFW_CHANNEL):
                    print(ctx.channel.id)
                    await ctx.send("Pu de vilainerie sur ce channel mon coco")
                else:
                    await ctx.send(submission.title)
                    await asyncio.sleep(2)
                    await ctx.send(submission.url)

    @commands.command(brief="!hentai Send a reddit post from r/hentai")
    async def hentai(self, ctx):
        current_count_hentai = get_amount(ctx.author.id, "Hentai")
        current_count_reddit = get_amount(ctx.author.id, "Reddit")
        add_to_db(ctx.author.id, current_count_hentai, 1, "Hentai")
        add_to_db(ctx.author.id, current_count_reddit, 1, "Reddit")
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("hentai").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                if submission.over_18 == True and ctx.channel.id != int(NSFW_CHANNEL):
                    print(ctx.channel.id)
                    await ctx.send("Oh mon dieu, ces images sont plutôt perturbante.")
                else:
                    await ctx.send(submission.title)
                    await asyncio.sleep(2)
                    await ctx.send(submission.url)

    @commands.command(brief="!shemale Send a reddit post from r/shemalesparadise")
    async def shemale(self, ctx):
        current_count_shemale = get_amount(ctx.author.id, "Shemale")
        current_count_reddit = get_amount(ctx.author.id, "Reddit")
        add_to_db(ctx.author.id, current_count_shemale, 1, "Shemale")
        add_to_db(ctx.author.id, current_count_reddit, 1, "Reddit")
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("shemalesparadise").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                if submission.over_18 == True and ctx.channel.id != int(NSFW_CHANNEL):
                    print(ctx.channel.id)
                    await ctx.send("Désolé, les penis madame sont pas admise dans ce channel.")
                else:
                    await ctx.send(submission.title)
                    await asyncio.sleep(2)
                    await ctx.send(submission.url)

    @commands.command(brief="!roast Send a reddit post from r/roastme and some comments")
    async def roastme(self, ctx):
        current_count = get_amount(ctx.author.id, "Reddit")
        add_to_db(ctx.author.id, current_count, 1, "Reddit")
        async with ctx.channel.typing():
            if self.reddit:
                submissions = self.reddit.subreddit("roastme").hot(limit=100)
                rnd = random.randint(1,99)
                for i in range(0, rnd):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.title)
                await asyncio.sleep(2)
                await ctx.send(submission.url)
                submission.comment_sort = 'best'
                x = 0
                for top_level_comment in submission.comments:
                    x += 1
                    if x > 10:
                        return
                    await ctx.send(f"{x}: {top_level_comment.body}")

def setup(bot):
    bot.add_cog(Reddit(bot))