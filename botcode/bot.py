import discord
from discord.ext import commands

TOKEN = ''

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    await ctx.send(left + right)

bot.run(TOKEN)
