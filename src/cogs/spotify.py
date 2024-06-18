from discord.ext import commands
import discord
from utils import *
import PyFyLib

class Spotify():
    def __init__(self, bot):
        self.bot = bot
        pyfylib = PyFyLib()

    @commands.command(brief="!sp_enable to enable the spotify player.")
    async def sp_enable(self, ctx, arg): 
        if ctx.author.id == int(ALESS):
            SP_ENABLE = True 
            await ctx.send(f"Vive la muzik")
            return SP_ENABLE
        else:
            await ctx.send(f"Desoler {ctx.author.name}, Ta pa l'dwa.")

    @commands.command(brief="!sp_disable to disable the spotify player.")
    async def sp_disable(self, ctx, arg):
        if ctx.author.id == int(ALESS):
            SP_ENABLE = False
            await ctx.send(f"Feni la muzik")
            return SP_ENABLE
        else:
            await ctx.send(f"Desoler {ctx.author.name}, Ta pa l'dwa.")

    @commands.command(brief="!sp_play to play a spotify song.")
    async def sp_play(self, ctx, arg, pyfylib):
        if SP_ENABLE == True:
            pass
        else:
            pass

    @commands.command(brief="!sp_add to add a song in queue.")
    async def sp_add(self, ctx, arg, pyfylib):
        if SP_ENABLE == True:
            pass
        else:
            pass

    @commands.command(brief="!sp_next to play next song in queue.")
    async def sp_next(self, ctx, arg, pyfylib):
        if SP_ENABLE == True:
            pass
        else:
            pass


