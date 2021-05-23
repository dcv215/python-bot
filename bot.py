import discord, asyncio, os
from discord.ext import commands

game = discord.Game("😓빵 계산")
bot = commands.Bot(command_prefix='.', status=discord.Status.online, activity=game)
@bot.command(aliases=['안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')









bot.run('ODQ1ODcyNzU2NzU4OTM3NjAw.YKnSZA.9byTo2rjteB1JUyAhMICzIjQYrw')

