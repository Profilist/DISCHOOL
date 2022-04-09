from discord.ext import commands, tasks


class prompt(commands.Cog, name='prompt'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def prompt(self, ctx: commands.Context, arg):
        channel_id = 962440578686140416
        channel = ctx.bot.get_channel(channel_id)
        if arg.isdigit():
            minutes = int(arg)
            print(minutes)
            @tasks.loop(minutes=minutes)
            async def routineprompt():
                message = await channel.send('@here React to this prompt so we know you are with us!!')
                emoji = '\N{THUMBS UP SIGN}'
                await message.add_reaction(emoji)
            routineprompt.start()

def setup(bot: commands.Bot):
    bot.add_cog(prompt(bot))