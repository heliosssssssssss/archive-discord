import discord
from discord import app_commands
from discord.ext import commands 

class helpView(discord.ui.View):
    @discord.ui.select(
        placeholder = "Choose a category of commands",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label = "Quran",
                description = "Commands for the Quran"
            ),
            discord.SelectOption(
                label = "Hadith",
                description = "Commands for Hadiths"
            ),
            discord.SelectOption(
                label = "Calender",
                description = "Commands for the Calender"
            ),
            discord.SelectOption(
                label = "Islam Quiz",
                description = "Commands for Islam Quiz"
            ),
            discord.SelectOption(
                label = "Recitations",
                description = "Commands for Recitations"
            ),
            discord.SelectOption(
                label = "Live Radio",
                description = "Commands for Live radio"
            ),
            discord.SelectOption(
                label = "Bot",
                description = "Commands for the bot (info/error)"
            ),
            discord.SelectOption(
                label = "Islamic Wordle",
                description = "Commands for Islamic Wordle"
            ),
            discord.SelectOption(
                label = "Server Commands",
                description = "Commands for server owners"
            ),
            discord.SelectOption(
                label = "Developer commands",
                description = "Commands for developers (to debug)"
            )
        ]
    )

    async def select_callback(self, select, interaction):
        await select.response.send_message("We do not have the commands view system done yet, it will be done later on")

class helpcmd(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

    group = app_commands.Group(name="help", description="A list of helpful information (cmds, support)")

    @group.command(
        name = 'cmds',
        description = 'Interactable list of commands in IslamG'
    )
    async def cmds(
        self,
        interaction : discord.Interaction
    ):
        embed=discord.Embed(color=0x008142)
        embed.add_field(name="IslamG Commands", value="Please choose a option to view commands.", inline=False)
        await interaction.response.send_message(embed=embed, view=helpView())
    

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        helpcmd(bot)
    )
    print('[cogs]: cog --> help is good')