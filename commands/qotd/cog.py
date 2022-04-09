import asyncio
from datetime import datetime, timedelta
import requests
import json

from discord.ext import tasks, commands

def get_quote():
  response = requests.get ("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "-" + json_data[0]['a']
  return (quote)

class qotd(commands.Cog, name='qotd'):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def qotd(self, ctx, arg):
        channel_id = 962421141648076800
        channel = ctx.bot.get_channel(channel_id)
        @tasks.loop(hours=24)
        async def dailymessage(self):
            await channel.send(get_quote())

        set_time = arg + ":00"

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        time = datetime.strptime(set_time,'%H:%M:%S') - datetime.strptime(current_time,'%H:%M:%S')
        if time.total_seconds() < 0:
            time += timedelta(days=1)

        await asyncio.sleep(time.total_seconds())
        await channel.send(get_quote())
        dailymessage.start(self)

def setup(bot: commands.Bot):
    bot.add_cog(qotd(bot))