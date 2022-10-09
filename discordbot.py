# Helpful Resources:
# Pycord Guide: https://guide.pycord.dev/
# Pycord API Reference: https://docs.pycord.dev/en/stable/api.html
# Pycord Example Github Folder: https://github.com/Pycord-Development/pycord/tree/master/examples

# Imports
import discord, os
from dotenv import load_dotenv

# Load .env file from the current working directory
load_dotenv()

# Variables
intents = discord.Intents.default()
intents.members = True  # This is required for the Greeting Command Examples, for more info on Intents see here: https://guide.pycord.dev/popular-topics/intents/
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # Get a "DISCORD_TOKEN" Variable from a .env file in the current working directory.
                                            # This is safer than just putting the Token directly into the Source Code
bot = discord.Bot(intents=intents, owner_id=YOUR_DISCORD_ID_HERE)
# Specifying the Owner ID is useful, in case you want to create a Discord Command that can only be accessed by the Owner.
# You can also specify multiple Owner IDs by replacing "owner_id=YOUR_DISCORD_ID_HERE" with "owner_ids=[DISCORD_ID_1, DISCORD_ID_2]"

# Load Extensions
# Extensions are essentially just Discord Cogs in a separate file. For more information on Cogs see here: https://guide.pycord.dev/popular-topics/cogs
bot.load_extension('lib.bot.commands.test1')  # A Python File called test1.py will be loaded from ./lib/bot/commands/
bot.load_extension('lib.bot.commands.example')  # A Python File called example.py will be loaded from ./lib/bot/commands/


# Print a Message in the Console when the Bot logs in
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# Run the Bot using our Discord Bot Token
bot.run(DISCORD_TOKEN)
