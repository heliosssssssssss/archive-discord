import discord


from discord.ext import commands 
from tools.QuranAPI import QuranAPI

class IslamBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='.!',
            intents = discord.Intents.all(),
            application_id = "auto-removed"
        )

    async def setup_hook(self):
        await self.load_extension(f"cogs.help")
        await self.load_extension(f"cogs.error_handling")
        await self.load_extension(f"cogs.cquran")
        await self.load_extension(f"cogs.vcquran")
        await self.load_extension(f"cogs.vpquran")
        await bot.tree.sync()

    async def on_ready(self):
        print(f'[SETUP]: BOT: {self.user} is connected.')
        await bot.change_presence(
            status = discord.Status.do_not_disturb,
            activity = discord.Activity(type=discord.ActivityType.watching, name=f'/help | [{len(bot.guilds)} Servers]')
        )

bot = IslamBot()



































bot.run('auto-removed')