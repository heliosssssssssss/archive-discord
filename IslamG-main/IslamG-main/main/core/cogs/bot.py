import discord
from discord import app_commands
from discord.ext import commands 

class info(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

    group = app_commands.Group(name="bot", description="Information/errors about the bot")

    @group.command(
        name = 'info',
        description = 'General information regarding IslamG'

    )


    async def info(
        self,
        interaction : discord.Interaction
    ):
        author = interaction.user
        viewFrame = discord.ui.View()
        supportButton = discord.ui.Button(label="Support Server", url="https://discord.gg/SUkeTjve5x")
        linkButton = discord.ui.Button(label="Invite IslamG", url="https://discord.com/api/oauth2/authorize?client_id=1146492970678353931&permissions=8&scope=bot")
        viewFrame.add_item(supportButton)
        viewFrame.add_item(linkButton)


        embed=discord.Embed(title="IslamG", description="Made by the **Islamic Guidance Development Team**", color=0x008142)
        embed.add_field(name="", value=f"Assalamu Alaikum **{str(author)}**", inline=False)
        embed.add_field(name="Support ", value="You can directly message **helioss** or join: *https://discord.gg/SUkeTjve5x*", inline=False)
        embed.add_field(name="Developement Team", value="helioss. (Developer) | SamuraiXeon2 (Developer) | Ugly Step Sister (Tester) | Nehan (CA - CM)", inline=False)
        embed.add_field(name="Status", value="```Online```", inline=True)
        embed.add_field(name="Version", value=f"```0.3 (Hotfix #1)```", inline=True)

        await interaction.response.send_message(embed=embed, view=viewFrame)

    @group.command(
        name = 'errors',
        description = 'View information on a specfic error'

    )

    async def errors(
        self,
        interaction : discord.Interaction,
        error_number : int
    ):

        print("hi")

    @group.command(
        name = "credits",
        description = "The credits of IslamG"
    )

    async def credits(
        self, 
        interaction : discord.Interaction
    ):
        
        embed=discord.Embed(color=0x008142)
        embed.add_field(name="IslamG Credits", value="IslamG was developed on 9/30/2023 by helioss. ", inline=False)
        embed.add_field(name="Team", value="helioss. (Developer) | SamuraiXeon2 (Developer) | Amin (Tester) | Nehan (CA) ", inline=False)
        embed.add_field(name="Special Thanks", value="shaeikh (Inspiration + code improvements after looking at his source code on a IslamiQ. | Nour Sharabash (Provided real time support in DMs with the Quran API) | Practical Hosting & ImTheMark (provided support, and also a cheap provider) | ", inline=False)
        embed.add_field(name="APIs used (last updated on version 0.3)", value="Quran API ", inline=False)

        await interaction.response.send_message(embed=embed)

    

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        info(bot)
    )
    print('[cogs]: cog --> info is good')