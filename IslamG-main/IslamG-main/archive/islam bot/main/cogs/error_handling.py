import discord
from discord import app_commands
from discord.ext import commands 

class error_handling(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print("exd")
        
    

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        error_handling(bot)
    )
    print("[SETUP]: -- COG ERROR_HANDLE SUCCESS")