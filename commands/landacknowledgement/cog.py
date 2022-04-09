import asyncio
from datetime import datetime, timedelta

from discord.ext import tasks, commands

class landacknowledgement(commands.Cog, name='landacknowledgement'):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def landacknowledgement(self, ctx, arg):
        channel_id = 962429959945728090
        channel = ctx.bot.get_channel(channel_id)
        message = "We affirm that we are all treaty people and acknowledge that the York Region District School Board is located on the lands of two treaties. These treaties have been signed with the Mississaugas of the Credit First Nation and the First Nations of the Williams Treaties who are: the Mississaugas of Alderville, Curve Lake, Hiawatha, Scugog Island; and the Chippewas of Beausoleil, Rama, and Georgina Island who is our closest neighbour and partner in education. To honour this agreement we will take up our responsibility to be respectful of their traditions, knowledge and inherent rights as sovereign nations. We will respect their relationship with these lands and recognize that our connection to this land is through the continued relationship with these First Nations, and we acknowledge our shared responsibility to respect and care for the land and waters for future generations."

        @tasks.loop(hours=24)
        async def dailymessage():
            await channel.send(message)
            print('ive been called')

        set_time = arg + ":00"

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        time = datetime.strptime(set_time,'%H:%M:%S') - datetime.strptime(current_time,'%H:%M:%S')
        if time.total_seconds() < 0:
            time += timedelta(days=1)

        await asyncio.sleep(time.total_seconds())
        dailymessage.start()

def setup(bot: commands.Bot):
    bot.add_cog(landacknowledgement(bot))