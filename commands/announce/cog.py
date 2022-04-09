from discord.ext import commands
import discord
import asyncio
from datetime import datetime, timedelta

class Announce(commands.Cog, name='commands'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx: commands.Context, arg, *message):
        """Makes a scheduled announcement to all students"""

        message = ' '.join(message) or 'Announcement!'

        set_time = arg + ":00"

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        time = datetime.strptime(set_time, '%H:%M:%S') - datetime.strptime(current_time, '%H:%M:%S')
        if time.total_seconds() < 0:
            time += timedelta(days=1)

        await asyncio.sleep(time.total_seconds())
        channel_id = 962414470930522112
        channel = ctx.bot.get_channel(channel_id)
        allowed_mentions = discord.AllowedMentions(everyone=True)
        await channel.send(content="@everyone "+message, allowed_mentions=allowed_mentions)

def setup(bot: commands.Bot):
    bot.add_cog(Announce(bot))