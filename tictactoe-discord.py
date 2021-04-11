
import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
#client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client}')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')
#
# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left a server.')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')




client.run('TOKEN')
