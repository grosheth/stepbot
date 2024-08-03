import asyncio
from discord.ext import commands
from random import randint
from utils import *
from settings import *


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!coinflip <pile> <face>")
    async def coinflip(self, ctx, arg):
        arg = arg.lower()
        if arg != "pile" and arg != "face":
            await ctx.send(f"{arg} n'est pas un choix à Pile ou face. Monsieur soleil")
            return

        guesses = {1: "pile", 2: "face"}
        guess = randint(1, 2)
        await asyncio.sleep(1)
        await ctx.send("...La tension monte...")
        await asyncio.sleep(2)

        if ctx.author.id == int(FILOU):
            await ctx.send("...pas comme la molle a Filou...")
        await ctx.send(guesses[guess])

        if guesses[guess] == arg:
            await asyncio.sleep(1)
            await ctx.send("Bravo, Pussi Conqueror")
        else:
            await asyncio.sleep(1)
            await ctx.send("CACHING MUFAKA")

    @commands.command(brief="!rr Russian roulette")
    async def rr(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("T po dans l'channel, Tu decide po.")
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        await ctx.send("Roulette Russe")
        await asyncio.sleep(1)
        for member in voice_channel.members:
            shot = randint(1, 6)

            await ctx.send(
                f'{member.name} {await open_file("russianroulette.json","opening")}'
            )
            await asyncio.sleep(1)
            if shot == 1:
                await ctx.send(
                    f'{member.name} {await open_file("russianroulette.json","dead")}'
                )
                await ctx.send(f"{member.name} Ta pardu tes Nanane sti de laid")
                await asyncio.sleep(1)
                await member.move_to(None)
                return
            else:
                await ctx.send(f"click...")
                await asyncio.sleep(1)
                await ctx.send(f'{await open_file("russianroulette.json","alive")}')

        await asyncio.sleep(1)
        await ctx.send(f"Parsonne est mort")
        return


# Create a Text channel for each person who wants to play blackjack
# Give player input options
# Delete text channel afterwards


#     @commands.command(brief="!bleckjeck")
#     async def bj(self, ctx):

#         points = 0
#         dealer_points = 0
#         hand = []
#         dealer_hand = []
#         cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#         x = 0
#         for value in cards:
#             if x < 39:
#                 cards.append(value)
#             else:
#                 break
#             x += 1

#         await create_text_channel(ctx.author.guild, f"{ctx.author.name}-blackjack")
#         await asyncio.sleep(2)
#         new_channel = get_channel_by_name(ctx.author.guild, f"{ctx.author.name}-blackjack")

#         await new_channel.send("Here is the dealer's first card:")
#         get_card_dealer(cards, dealer_hand)
#         await new_channel.send("-------------------------------------")
#         await new_channel.send("Here is your hand:")
#         get_card(cards, hand)
#         points = convert(hand, points)
#         dealer_points = convert(dealer_hand, dealer_points)
#         while True:
#             await new_channel.send(f"you currently have {points}")
#             await new_channel.send(f"The dealer has {dealer_points}")
#             await new_channel.send("1. Call.")
#             await new_channel.send("2. Stay.")

#             msg = await client.wait_for("message", check=check)

#             if answer == "1":
#                 await new_channel.send("Here is your hand:")
#                 get_card(cards, hand)
#                 points = convert(hand, points)
#                 if points > 21:
#                     await new_channel.send("you have more than 21!")
#                     await new_channel.send("YOU LOST")
#                     await asyncio.sleep(10)
#                     await delete_text_channel(ctx.author.guild, f"{ctx.author.name}-blackjack")

#             elif answer == "2":
#                     get_card_dealer(cards, dealer_hand)
#                     await new_channel.send("-------------------------------------")
#                     dealer_points = convert(dealer_hand, dealer_points)
#                     await asyncio.sleep(1)

#                     while True:

#                         if dealer_points > 21:
#                             await new_channel.send("You Won the dealer has more than 21")
#                             await new_channel.send("YOU WON")
#                             await delete_text_channel(ctx.author.guild, f"{ctx.author.name}-blackjack")

#                         if dealer_points <= 16:
#                             get_card_dealer(cards, dealer_hand)
#                             dealer_points = convert(dealer_hand, dealer_points)
#                             await asyncio.sleep(1)
#                         else:
#                             win = decision(points, dealer_points)

#                             if win:
#                                 await new_channel.send(f"You won with {points} against the dealer's {dealer_points}")
#                                 await new_channel.send("YOU WON")
#                                 await delete_text_channel(ctx.author.guild, f"{ctx.author.name}-blackjack")
#                             else:
#                                 await new_channel.send(f"You lost with {points} against the dealer's {dealer_points}")
#                                 await new_channel.send("YOU LOST")
#                                 await delete_text_channel(ctx.author.guild, f"{ctx.author.name}-blackjack")
#             else:
#                 await new_channel.send("invalid answer")


async def setup(bot):
    await bot.add_cog(Games(bot))
