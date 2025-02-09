import discord
from discord import app_commands
from discord.ext import tasks
from discord.ext import commands 
from tools.QuranAPI import QuranAPI
from pprint import pprint
import json
import time


class vcquran(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name = 'vcquran',
        description = 'Get all the verses in a specfic chapter of the Quran'
    )

    async def vcquran(
        self,
        interact : discord.Interaction,
        chapter : int
    ): 
        
        abovenum=discord.Embed(title=f"Chapter {str(chapter)} does not exist (Error: 0002)", color=0x3d91ff)
        abovenum.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")
        
        is_allowed = True 

        if chapter > 114:
            await interact.response.send_message(embed=abovenum)
            is_allowed = False
        if chapter < 1: 
            await interact.response.send_message(embed=abovenum)
            is_allowed = False

        if is_allowed == "maint":
            err1=discord.Embed(title=f"Error (0004) - Command has been flagged [under_maintence] by developer", color=0x3d91ff)
            err1.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

            await interact.response.send_message(embed=err1)
            return
        

        if is_allowed == True:
            print('debug')
            
                


            
            



async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        vcquran(bot)
    )
    print("[SETUP]: -- COG VQURAN")