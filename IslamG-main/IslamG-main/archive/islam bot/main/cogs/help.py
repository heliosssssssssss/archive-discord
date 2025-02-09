import discord
from discord import app_commands
from discord.ext import commands 

class help(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot 

    @app_commands.command(
        name = 'help',
        description = 'List of commands, and information'
    )
    
    async def help(
        self,
        interact : discord.Interaction
        ):

        author = interact.user

        successSend=discord.Embed(title="You have been sent a DM with the list of commands.", color=0x3d91ff)
        successSend.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

        failedSend=discord.Embed(title="Failed to send you a DM (Error-0001).", color=0x3d91ff)
        failedSend.add_field(name='', value="This is usually because you dont have your DMs enabled, view /errors for info")
        failedSend.set_footer(text=f"Islamic Guidance | Command requested by: {interact.user.name}")

        try:
           await author.send("test")
           await interact.response.send_message(embed=successSend)

        except discord.Forbidden:
            await interact.response.send_message(embed=failedSend)


async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        help(bot)
    )
    print("[SETUP]: -- COG HELP SUCCESS")