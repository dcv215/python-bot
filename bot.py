import discord, asyncio, os
from discord.ext import commands

game = discord.Game("πλΉ΅ κ³μ°")
bot = commands.Bot(command_prefix='.', status=discord.Status.online, activity=game)
@bot.command(aliases=['μλ', 'hi', 'μλνμΈμ'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}λ μλνμΈμ!')









bot.run('ODQ1ODcyNzU2NzU4OTM3NjAw.YKnSZA.9byTo2rjteB1JUyAhMICzIjQYrw')

