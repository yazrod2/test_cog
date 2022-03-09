import discord 
from discord.ext import commands
import os
bot = commands.Bot(command_prefix = "!")

bot.run("OTQ5OTcxMDQwMjc1MTUyOTU2.YiSHeQ.E3bv87NQcZZruHmSJ0MGNarT4g8")




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')










bot.run("OTQ5OTcxMDQwMjc1MTUyOTU2.YiSHeQ.a20bxrCY8CuYG8AOFU7aVfCn4tM")