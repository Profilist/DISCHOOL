from discord.ext import commands

class anonymousmessage(commands.Cog, name='anonymousmessage'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def anonymousmessage(self, ctx: commands.Context, *, args):
        channel_id = 962205235605033040
        channel = ctx.bot.get_channel(channel_id)
        await channel.send(args)

def setup(bot: commands.Bot):
    bot.add_cog(anonymousmessage(bot))