import discord
from discord import app_commands
from discord.ext import commands 

from utils.QuranAPI import QuranAPI

class quran(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

    group = app_commands.Group(name="quran", description="Commands for the Quran")

    @group.command(
        name = 'chapterinfo',
        description = 'Get information about a specfic chapter'

    )

    async def cinfo(
        self,
        interaction : discord.Interaction,
        chapter : int
    ):
        
        is_allowed = True

        aboveNumber = discord.Embed(color=0x008142)
        aboveNumber.add_field(name="Well that is awkward...", value = f"We could not find chapter: {str(chapter)}")

        if chapter > 114:
            await interaction.response.send_message(embed=aboveNumber)
            is_allowed = False
        if chapter < 1: 
            await interaction.response.send_message(embed=aboveNumber)
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

            rspembed=discord.Embed(title=f"{name} | Chapter: {chapter_num}", color=0x008142)
            rspembed.add_field(name='Verses', value=f'{verse_count}')
            rspembed.add_field(name='Pages', value=f'{pages1}-{pages2}')
            rspembed.add_field(name='Revelation Place', value=f'{reval}')
            rspembed.add_field(name=" ", value=f'```{short_text}```')
            rspembed.add_field(name="Source", value=f"```{source}```")
            await interaction.response.send_message(embed=rspembed)
        

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        quran(bot)
    )
    print('[cogs]: cog --> quran is good')