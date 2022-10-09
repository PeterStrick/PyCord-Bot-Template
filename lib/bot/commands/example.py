# Helpful Resources:
# Pycord Guide: https://guide.pycord.dev/
# Pycord API Reference: https://docs.pycord.dev/en/stable/api.html
# Pycord Example Github Folder: https://github.com/Pycord-Development/pycord/tree/master/examples

# Imports
import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands


# Example Cog:
# Cog Files are Python Classes that contain Discord Commands, including Slash Commands
# See https://guide.pycord.dev/popular-topics/cogs/
class Example(commands.Cog):
    def __init__(self, bot: discord.Bot):  # Make the Bot Variable accessible in Cogs
        self.bot = bot                     # This is required for every Cog for the setup(bot) Function

    greetings = SlashCommandGroup("greetings", "Various greeting from cogs!")  # We create a Slash Command Group called "greetings" with a description

    international_greetings = greetings.create_subgroup("international", "International greetings") # We create a subgroup of the "greetings" group with a description

    # We create an entirely new Slash Command Group that only Discord Users defined in owner_id can access the Commands inside this Group
    secret_greetings = SlashCommandGroup(
        "secret_greetings",
        "Secret greetings",
        checks=[commands.is_owner().predicate],  # Ensures the owner_id user can access this group, and no one else
    )

    # For Slash Commands you use the SlashCommandGroup name, in this instance "greetings" and add .command() after that
    @greetings.command()
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond("Hello, this is a slash subcommand from a cog!")  # Discord Slash Commands always require a Response to your Slash Command Interaction
                                                                            # If the Bot takes longer than 3 Seconds to process your Slash Command an Error will be
                                                                            # displayed on the Discord Client, stating that the Interaction has failed
    
    # The same rule applies to every Slash Command Group
    @international_greetings.command()
    async def aloha(self, ctx: discord.ApplicationContext):
        await ctx.respond("Aloha, a Hawaiian greeting")

    @secret_greetings.command()
    async def secret_handshake(self, ctx: discord.ApplicationContext, member: discord.Member):  # Slash Commands can have multiple Arguments
        await ctx.respond(f"{member.mention} secret handshakes you")                            # Every Argument here after self and ctx will be displayed as required
                                                                                                # on the Discord Client side, forcing you to input something for the
                                                                                                # Argument
    
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, commands.NotOwner):                    # This Error Handler responds to your Message if a commands.NotOwner Error has occurred
            await ctx.respond("You can't use that command!")        # For Example using a Command that is only accessible for the Discord Bot Owner
        else:
            raise error  # Raise other errors so they aren't ignored


# Every Cog File requires a setup(bot) Function outside of the Cog Class
# The main Discord Bot File uses this function to load our Cog and all it's Commands
# Syntax: bot.add_cog(CogName(bot))
def setup(bot):
    bot.add_cog(Example(bot))
    print("Example Cog loaded")  # This is optional and tells us if a Cog has been loaded


# This Function runs every Time an Extension/Cog is unloaded
# You can use this in case some special discord command needs to process something before being unloaded
# Other than that it is completely Optional and can be safely removed
def teardown(bot):
    print("Example Cog unloaded")
