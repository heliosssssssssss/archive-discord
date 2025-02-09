import discord
from discord import app_commands
from discord.ext import commands 
import json
from pprint import pprint
import asyncio
import random

global xy1g


from utils.DataHandler import DataHandler
from utils.DatabaseManager import DatabaseManager

def grantData(userid):
    if DatabaseManager.getPointsFromUserID(userid) == []:
        DatabaseManager.createUser(userid)
        DatabaseManager.grantUser(userid, 1)
    else:
        DatabaseManager.grantUser(userid, 1)


def checkData(userid):
    if DatabaseManager.getPointsFromUserID(userid) == []:
        DatabaseManager.createUser(userid)
        DatabaseManager.grantUser(userid, 1)
        return False
    else:
        return DatabaseManager.getPointsFromUserID(userid)

class islamQuiz(commands.Cog):
    def __init__(self, bot : commands.bot) -> None:
        self.bot = bot

    group = app_commands.Group(name="quiz", description="Commands on the Islamic Quiz")

    @group.command(
        name = 'play',
        description = 'Play the Islamic Quiz, there is up to 50 random Islamic questions.'


    )

    async def islamQuiz(
        self,
        interaction : discord.Interaction
    ):
        author = interaction.user
        viewFrame = discord.ui.View()

        questionsDB = json.loads(DataHandler.read_file("main/IslamG/main/core/secure/questionsDB.json"))
        count = questionsDB["total_questions"]
  
        r = random.randint(1, count)
        
        question = questionsDB["questions"][f"{r}"]
        
        actualQuestion = question['question']
        ans1 = question['ans1']
        ans2 = question['ans2']
        ans3 = question['ans3']
        actualAnswer = question['answer']
        submission = question['submitted_by']
        storageID = None

        winEmbed=discord.Embed(title=f"You have got the question right {author}", description="You have been give one point for choosing the right answer", color=0x008142)
        loseEmbed=discord.Embed(title=f"You have got the question wrong {author}", description="You guessed the wrong answer", color=0x008142)
        timeoutembed=discord.Embed(title=f"You took to long to answer {author}", description="You were not able to answer in time.", color=0x008142)
       
        class myview(discord.ui.View):

            async def on_timeout(self):
                try:
                    await interaction.edit_original_response(embed=timeoutembed, view=None)
                except discord.errors.NotFound:
                    print("[cogs.quiz] uh oh! >.< | ignore this error (HTTP-404 EXT.API.NOT_FOUND_404_10008)")


            @discord.ui.button(label="Option 1", style=discord.ButtonStyle.primary)
            async def button_callback1(self, button, int):

                if button.user.id is not author.id:
                    ant=discord.Embed(title=f"You cannot click this button {button.user}", description="", color=0x008142)
                    errors = await interaction.channel.send(embed=ant)
                    await errors.delete(delay=5)
                    return 
                
                if actualAnswer == "1": 
                    await interaction.edit_original_response(embed=winEmbed, view=None)
                    return grantData(interaction.user.id)
                else:
                    return await interaction.edit_original_response(embed=loseEmbed, view=None)

            
            @discord.ui.button(label="Option 2", style=discord.ButtonStyle.primary)
            async def button_callback2(self, button, int):

                if button.user.id is not author.id:
                    ant=discord.Embed(title=f"You cannot click this button {button.user}", description="", color=0x008142)
                    errors = await interaction.channel.send(embed=ant)
                    await errors.delete(delay=5)
                    return 
                
                if actualAnswer == "2": 
                    await interaction.edit_original_response(embed=winEmbed, view=None)
                    return grantData(interaction.user.id)
                else:
                    return await interaction.edit_original_response(embed=loseEmbed, view=None)

            
            @discord.ui.button(label="Option 3", style=discord.ButtonStyle.primary)
            async def button_callback3(self, button, int):

                if button.user.id is not author.id:
                    ant=discord.Embed(title=f"You cannot click this button {button.user}", description="", color=0x008142)
                    errors = await interaction.channel.send(embed=ant)
                    await errors.delete(delay=5)
                    return 
                
                if actualAnswer == "3": 
                    await interaction.edit_original_response(embed=winEmbed, view=None)
                    return grantData(interaction.user.id)
                else:
                    return await interaction.edit_original_response(embed=loseEmbed, view=None)
            

            @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
            async def button_callback4(self, button, int):

                if button.user.id is not author.id:
                    ant=discord.Embed(title=f"You cannot click this button {button.user}", description="", color=0x008142)
                    errors = await interaction.channel.send(embed=ant)
                    await errors.delete(delay=5)
                    return 
                
                return await interaction.delete_original_response()
                

        embed=discord.Embed(title=f"{actualQuestion}", description="If you choose the right option, you will be given **1** point", color=0x008142)
        embed.add_field(name="Option 1", value=f"```{ans1}```", inline=False)
        embed.add_field(name="Option 2", value=f"```{ans2}```", inline=False)
        embed.add_field(name="Option 3", value=f"```{ans3}```", inline=False)
        embed.set_footer(text=f"IslamG Quiz | Question submitted by: {submission} | Want to have your own question featured? do: /quiz submit")

        await interaction.response.send_message(embed=embed, view=myview(timeout=120))

    @group.command(
        name = "points",
        description = 'View how many points you have'
    )

    async def points(
        self,
        interaction : discord.Interaction,
    ):
        author = interaction.user

        check = checkData(author._user.id)
        embed1=discord.Embed(title=f"My Points | {author}", description=f"This is your first time using /quiz or /mypoints we have given you **1** point to start off with, you can earn more by doing Islamic quizes (/quiz)", color=0x008142)

        if check == False:
            await interaction.response.send_message(embed=embed1)
        else:
            embed=discord.Embed(title=f"My Points | {author}", description=f"You currently have **{check[0][1]}** points", color=0x008142)
            await interaction.response.send_message(embed=embed)

    @group.command(
        name = "submit",
        description = "Submit a question that can be reviewed, and put onto the list of questions for /quiz play",
    )


    async def submit(
        self,
        interaction : discord.Interaction,
        question : str,
        option_one : str,
        option_two : str,
        option_three : str,
        answer : str
    ):
        
        xy1 = interaction.client.get_channel(1147653280504221756)
        author = interaction.user
        check_id = 1147653280504221756

        timeoutembed=discord.Embed(title=f"You took to long to answer {author}", description="You were not able to answer in time.", color=0x008142)
        
        class view1(discord.ui.View):        

            async def on_timeout(self):
                try:
                    await interaction.edit_original_response(embed=timeoutembed, view=None)
                except discord.errors.NotFound:
                    print("[cogs.quiz] uh oh! >.< | ignore this error (HTTP-404 EXT.API.NOT_FOUND_404_10008)")

            @discord.ui.button(label="Submit", style=discord.ButtonStyle.green)
            async def button_callback5(self, button, int):

                if button.user.id is not author.id:
                    ant=discord.Embed(title=f"You cannot click this button {button.user}", description="", color=0x008142)
                    errors = await interaction.channel.send(embed=ant)
                    await errors.delete(delay=5)
                    return 

                target = xy1              

                await target.send(embed=embedReview2)
                await interaction.edit_original_response(embed=embedSent, view=None)
            
            @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
            async def button_callback6(self, button, int):

                if button.user.id is not author.id:
                    ant=discord.Embed(title=f"You cannot click this button {button.user}", description="", color=0x008142)
                    errors = await interaction.channel.send(embed=ant)
                    await errors.delete(delay=5)
                    return 
                
                return await interaction.delete_original_response()
            


        embedReview = discord.Embed(title=f"Review your question", description=f"Please confirm that everything is correct before you submit.", color=0x008142)
        embedReview.add_field(name="Question", value=f"```{question}```", inline=False)
        embedReview.add_field(name="Option 1", value=f"```{option_one}```", inline=False)
        embedReview.add_field(name="Option 2", value=f"```{option_two}```", inline=False)
        embedReview.add_field(name="Option 3", value=f"```{option_three}```", inline=False)
        embedReview.add_field(name="Answer", value=f"```{answer}```", inline=False)

        embedReview2 = discord.Embed(title=f"Question for review ", description=f"This question was submitted by: {interaction.user} | {interaction.user.id}", color=0x008142)
        embedReview2.add_field(name="Question", value=f"```{question}```", inline=False)
        embedReview2.add_field(name="Option 1", value=f"```{option_one}```", inline=False)
        embedReview2.add_field(name="Option 2", value=f"```{option_two}```", inline=False)
        embedReview2.add_field(name="Option 3", value=f"```{option_three}```", inline=False)
        embedReview2.add_field(name="Answer", value=f"```{answer}```", inline=False)
        embedReview2.add_field(name="Developer Details", value=f"```Sent from: {interaction.guild} | {interaction.guild_id}```", inline=False)
        
        embedSent = discord.Embed(title=f"Your question has been sent!", description=f"It will take a few days for us to review your question, you will be DMed its status once done or view #submissions in our support server.", color=0x008142)
        await interaction.response.send_message(embed=embedReview, view=view1(timeout=360))
        
        

async def setup(bot : commands.Bot) -> None:
    await bot.add_cog(
        islamQuiz(bot)
    )
    print('[cogs]: cog --> islamQuiz is good')