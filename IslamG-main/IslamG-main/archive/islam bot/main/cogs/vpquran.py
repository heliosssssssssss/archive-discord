import discord
from discord import app_commands
from discord.ext import tasks
from discord.ext import commands 
from tools.QuranAPI import QuranAPI
from pprint import pprint
import json
import time


class vpquran(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name = 'vpquran',
        description = 'Get all the verses in a specfic page of the Quran'
    )

    async def vpquran(
        self,
        interact : discord.Interaction,
        page : int
    ): 
        
        abovenum=discord.Embed(title=f"page {str(page)} does not exist (Error: 0002)", color=0x3d91ff)
        abovenum.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

        httperror=discord.Embed(title=f"We could not get the verse information (Error-0003)", description="This is usually because our service provider (quran.com)'s API is inactive", color=0x3d91ff)
        httperror.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")
        
        is_allowed = True 

        if  page > 604:
            await interact.response.send_message(embed=abovenum)
            is_allowed = False
        if  page  < 1: 
            await interact.response.send_message(embed=abovenum)
            is_allowed = False

        if is_allowed == "maint":
            err1=discord.Embed(title=f"Error (0004) - Command has been flagged [under_maintence] by developer", color=0x3d91ff)
            err1.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

            await interact.response.send_message(embed=err1)
            return
        

        if is_allowed == True:
            response = QuranAPI.getChapterVerseByPage(page)

            QuranVerses = response[0]['verses']
            success = response[1]

            if success == False:
                await interact.response.send_message(embed=httperror)
            else:
                for verse in QuranVerses:
                    pprint(verse['hzib_number'])


            
            



async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        vpquran(bot)
    )
    print("[SETUP]: -- COG VPQURAN")