import math

from discord.ext import commands
from discord.utils import get


class breakoutrooms(commands.Cog, name='breakoutrooms'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.count = 1

    @commands.command()
    async def breakoutrooms(self, ctx: commands.Context, arg):
        voice_state = ctx.author.voice
        if voice_state is None:
            await ctx.send('You need to be connected to a voice channel to use this command!')
        else:
            await ctx.send("REACHED")
            channel = voice_state.channel
            channel_members = channel.members
            bot = commands.Bot(command_prefix='+')
            guild = ctx.guild
            channel_list = []

            category = await guild.create_category('Breakout Rooms')
            groupcount = int(arg)

            if groupcount > len(channel_members):
                groupcount = len(channel_members)

            memberspergroup = math.ceil(len(channel_members) / groupcount)
            memberindex = 0
            for i in range(groupcount):
                channel_list.append(await guild.create_voice_channel('Breakout ' + str(self.count), category=category))
                self.count += 1
                for j in range(memberspergroup):
                    await channel_members.pop(memberindex).move_to(channel_list[i])

def setup(bot: commands.Bot):
    bot.add_cog(breakoutrooms(bot))