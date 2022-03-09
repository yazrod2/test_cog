import discord
from discord.ext import commands
import asyncio 
from random import randint



class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@commands.command(pass_context=True, name = "dice", aliases = ["dé","dés","dices"])
async def dice(self,ctx,nb:int):
    result = randint(1,nb)
    await ctx.send(f"le dé est tombé sur {result}")
   








def setup(bot):
    bot.add_cog(dice(bot))