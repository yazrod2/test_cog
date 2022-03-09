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
    embed=discord.Embed(
        title = f"Tirage d'un dé de {nb} faces",
        description = f"Le dé est tombé sur {result}",
        color = 0xAE02A1
    )









def setup(bot):
    bot.add_cog(dice(bot))