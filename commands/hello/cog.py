from discord.ext import commands

class Hello(commands.Cog, name='commands'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """Says hello"""
        await ctx.send('Hello! Do +help to see a list of commands')

def setup(bot: commands.Bot):
    bot.add_cog(Hello(bot))