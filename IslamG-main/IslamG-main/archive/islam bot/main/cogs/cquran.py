import discord
from discord import app_commands
from discord.ext import commands 
from tools.QuranAPI import QuranAPI
from pprint import pprint
import json

class cquran(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

    @app_commands.command(
        name = 'cquran',
        description = 'Quick information on a chapter in the Quran'
    )
    
    async def cquran(
        self,
        interact : discord.Interaction,
        chapter : int
        ):

        is_allowed = True

        abovenum=discord.Embed(title=f"Chapter: {str(chapter)} does not exist (Error-0002)", color=0x3d91ff)
        abovenum.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

        httperror=discord.Embed(title=f"We could not get the chapter information (Error-0003)", description="This is usually because our service provider (quran.com)'s API is inactive", color=0x3d91ff)
        httperror.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

        if chapter > 114:
            await interact.response.send_message(embed=abovenum)
            is_allowed = False
        if chapter < 1:
            await interact.response.send_message(embed=abovenum)
            is_allowed = False
        
        if is_allowed == True:
            response = QuranAPI.GetChaptersInfo(chapter)

            information1 = response[0]['chapter_info']
            information2 = response[1]['chapter']
            success = response[2]

            chapter_num = information2['id']
            name = information2['name_complex']
            verse_count = information2['verses_count']
            pages1 = information2['pages'][0]
            pages2 = information2['pages'][1]
            reval = information2['revelation_place']
            short_text = information1['short_text']
            source = information1['source']

            rspembed=discord.Embed(title=f"{name} | Chapter: {chapter_num}", color=0x3d91ff)
            rspembed.add_field(name='Verses', value=f'{verse_count}')
            rspembed.add_field(name='Pages', value=f'{pages1}-{pages2}')
            rspembed.add_field(name='Revelation Place', value=f'{reval}')
            rspembed.add_field(name=" ", value=f'```{short_text}```')
            rspembed.add_field(name="Source", value=f"```{source}```")
            rspembed.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

            if success == False:
                await interact.response.send_message(embed=httperror)
            else:
                await interact.response.send_message(embed=rspembed)

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        cquran(bot)
    )
    print("[SETUP]: -- COG CQURAN SUCCESS")