import discord
from discord import app_commands
from discord.ext import commands 
import asyncio

class dev(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

import discord
from discord import app_commands
from discord.ext import commands 

class dev(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 
    

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        dev(bot)
    )
    print('[cogs]: cog --> developer (cmds) is good')