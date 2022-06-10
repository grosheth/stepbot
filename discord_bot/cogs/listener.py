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
    async def on_voice_state_update(self,member,before,after):
        if member.bot:
            if not before.channel:
                print(f'{member.name} joined {after.channel.name}')

            if before.channel and not after.channel:
                print(f'bot left channel')

            if before.channel and after.channel:
                if before.channel.id != after.channel.id:
                    print("bot switched channel")
                else:
                    print("somethin else happened")
                    if member.voice.self_stream:
                        print("User started streaming")
                    if member.voice.self_deaf:
                        print("User deafened")

def setup(bot):
    bot.add_cog(Activities(bot))