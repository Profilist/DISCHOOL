from discord.ext import commands
import discord
import asyncio
from datetime import datetime, timedelta

class Remind(commands.Cog, name='commands'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def remind(self, ctx: commands.Context, user: discord.User, arg, *message):
        """Reminds a user in their dms"""

        message = ' '.join(message) or 'Reminder!'

        set_time = arg + ":00"

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        time = datetime.strptime(set_time, '%H:%M:%S') - datetime.strptime(current_time, '%H:%M:%S')
        if time.total_seconds() < 0:
            time += timedelta(days=1)

        await asyncio.sleep(time.total_seconds())
        await user.send(message)

def setup(bot: commands.Bot):
    bot.add_cog(Remind(bot))