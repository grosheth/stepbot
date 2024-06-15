from discord.ext import commands
import discord
from utils import *
import PyFyLib

class Spotify():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!sp_enable to enable the spotify player")
    async def sp_enable(self, ctx, arg):
        await check_enabled()

    @commands.command(brief="!sp_disable to disable the spotify player ")
    async def sp_disable(self, ctx, arg):
        await check_enabled()

    @commands.command(brief="!sp_play to play a spotify song")
    async def sp_play(self, ctx, arg):
        await check_enabled()

    @commands.command(brief="!sp to play spotify music")
    async def sp_add(self, ctx, arg):
        await check_enabled()

    @commands.command(brief="!sp to play spotify music")
    async def sp_(self, ctx, arg):
        await check_enabled()

