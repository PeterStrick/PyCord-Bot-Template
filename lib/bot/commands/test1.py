# Helpful Resources:
# Pycord Guide: https://guide.pycord.dev/
# Pycord API Reference: https://docs.pycord.dev/en/stable/api.html
# Pycord Example Github Folder: https://github.com/Pycord-Development/pycord/tree/master/examples

# Imports
import discord
from discord.commands import SlashCommandGroup, Option
from discord.ext import commands


# Test1 Cog:
# Cog Files are Python Classes that contain Discord Commands, including Slash Commands
# See https://guide.pycord.dev/popular-topics/cogs/
class test1(commands.Cog):
    def __init__(self, bot: discord.Bot):  # Make the Bot Variable accessible in Cogs
        self.bot = bot  # This is required for every Cog for the setup(bot) Function

    testgrp = SlashCommandGroup("testgroup", "Testing commands with Cogs!")  # We create a Slash Command Group called "testgroup" with a description

    # This Slash Command will greet the User, that uses it
    @testgrp.command()
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond(f'Hello {ctx.author.display_name}.')

    # Another thing you might want to consider is Commands that are for specific Discord Roles only
    # This can be achieved by the commands.has_role() function
    #
    # Slash Commands that use this will only show up for the Roles that you have specified
    #
    # See: https://docs.pycord.dev/en/stable/ext/commands/api.html?hlighight=has_role#discord.ext.commands.has_role
    @commands.has_role("Cool Role")  # You can use either the Role Name
    @commands.has_role(1234567890123456)  # Or the Role ID
    @testgrp.command()
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond('Hello Cool Person 😎.')

    # This is an example of using Arguments
    # The User will put in an Argument named "message" and the Bot responds with what the user typed in
    async def say(self, ctx: discord.ApplicationContext, message):
        await ctx.respond(f'{ctx.author.display_name} said: {message}')

    # This Example builds upon the first one, by describing what each Argument means to the User
    # The Options Parameter works like this:
    # ... arg1: Option(Data Type Here, "Description here", required=True or False)
    async def say2(self, ctx: discord.ApplicationContext, message: Option(str, "Enter something that I should say", required=True)):
        await ctx.respond(f'{message}')

    # You can define multiple Arguments that use Option or don't use it
    async def addition(self, ctx: discord.ApplicationContext, Number1: int, Number2: Option(int, "Enter Number 2", required=True)):
        await ctx.respond(f'The Answer is {Number1 + Number2}')


# Every Cog File requires a setup(bot) Function outside the Cog Class
# The main Discord Bot File uses this function to load our Cog and all it's Commands
# Syntax: bot.add_cog(CogName(bot))
def setup(bot):
    bot.add_cog(test1(bot))
    print("Test1 Cog loaded")  # This is optional and tells us if a Cog has been loaded


# This Function runs every Time an Extension/Cog is unloaded
# You can use this in case some special discord command needs to process something before being unloaded
# Other than that it is completely Optional and can be safely removed
def teardown(bot):
    print("Test1 Cog unloaded")
