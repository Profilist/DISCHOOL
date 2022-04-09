import os
from discord.ext import commands

client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

for folder in os.listdir('commands'):
    if os.path.exists(os.path.join('commands', folder, 'cog.py')):
        client.load_extension(f'commands.{folder}.cog')


client.run(os.getenv('TOKEN'))