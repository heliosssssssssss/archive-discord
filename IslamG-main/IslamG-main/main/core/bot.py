# [IMPORTS]

import discord
import os, time, pprint, math, json
import api, utils


# [IMPORTS V2]

from discord.ext import commands
from utils.DataHandler import DataHandler

global MAIN_COGS

MAIN_COGS = [
    'bot', 
    'quiz', 
    'help',
    'quran',
    'developer'
]

class IslamG(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix =".dev-",
            intents = discord.Intents.all(),
            application_id = DataHandler.read_file('main/IslamG/main/core/secure/id.txt'),
            help_command = None
        )

    async def setup_hook(self):
        for cog in MAIN_COGS:
            await self.load_extension(f'cogs.{cog}')
        await bot.tree.sync()

    async def on_ready(self):
        print(f"[startup-main]: start command received >.< | @helioss | {self.user} connected.")
        print(f"[startup-main]: ily - Session ID: P57JxKM - Data Chain ID: auto-removed - startup complete! :3")
        print(f"[database-main]: @auto-removed [xd - info]: sql check is all good")
        print(f"[utils-manager]: chicken butt :p (serious dev stuff: file intergrity: good)")
        print(f"[notifcation@auto]: all systems, apis, databases, and auth are great | goodluck.. <3 | from: core.bot.on_ready(self)")
        await bot.change_presence(
            status = discord.Status.online,
            activity = discord.Activity(type=discord.ActivityType.playing, name=f"/help | [{len(bot.guilds)}] Servers")
        )

    async def getchannel(idx):
        return bot.get_channel(idx)

bot = IslamG()

@bot.command()
async def accept(ctx, userid, question, reason):
    user = await bot.fetch_user(userid)
    await ctx.send(f"**Sending successful notification message to: {userid} | {user.name}** ")

    embed=discord.Embed(color=0x008142)
    embed.add_field(name="Your Question has been accepted.", value="Accepted by: helioss | You are most likely to receive this message when the bot has updated meaning your question will be on our database.", inline=False)
    embed.add_field(name="Question", value=f"```{question}```", inline=False)
    embed.add_field(name="Reason", value=f"```{reason}```", inline=False)
    await user.send(embed=embed)

    await ctx.send(f"**Message has been sent!**")

@bot.command()
async def we4private(ctx, userid, question, reason):
    user = await bot.fetch_user(userid)
    await ctx.send(f"**Sending successful notification message to: {userid} | {user.name}** ")

    await user.send('testingbranch')

    await ctx.send(f"**Message has been sent!**")

@bot.command()
async def deny(ctx, userid, question, reason):
    user = await bot.fetch_user(userid)
    await ctx.send(f"**Sending successful notification message to: {userid} | {user.name}** ")

    embed=discord.Embed(color=0x008142)
    embed.add_field(name="Your Question has been denied.", value="Denied by: helioss | View further details on the reason your question was denied in the 'Reason' box or look for your question in #submissions", inline=False)
    embed.add_field(name="Question", value=f"```{question}```", inline=False)
    embed.add_field(name="Reason", value=f"```{reason}```", inline=False)
    await user.send(embed=embed)

    await ctx.send(f"**Message has been sent!**")


file = DataHandler.read_file(r'main/IslamG/main/core/secure/token.json')
IO_File = json.loads(file)
IO_Token = IO_File['data']['token']
IO_Token = IO_Token.replace('"', "")

bot.run(IO_Token)