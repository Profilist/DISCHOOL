from discord.ext import commands
import discord

class Agenda(commands.Cog, name='commands'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def agenda(self, ctx: commands.Context, *args):
        """Daily agenda to ensure online students are not neglected"""
        guild = ctx.guild
        category = discord.utils.get(ctx.guild.categories, name="today's agenda")

        for channel in args:
            await guild.create_text_channel(channel, category=category)

def setup(bot: commands.Bot):
    bot.add_cog(Agenda(bot))