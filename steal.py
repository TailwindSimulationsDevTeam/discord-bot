import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

# Create bot instance with intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Channel IDs
TARGET_CHANNEL_ID = 1326363512762794076  # Your monitoring channel ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('Bot is ready to forward messages!')

@bot.event
async def on_message(message):
    try:
        # Ignore messages from the bot itself
        if message.author == bot.user:
            return
            
        # Get the monitoring channel
        monitoring_channel = bot.get_channel(TARGET_CHANNEL_ID)
        
        if monitoring_channel:
            # Forward all messages to the monitoring channel
            await monitoring_channel.send(
                f"**{message.author}** in #{message.channel.name}: {message.content}"
            )
            
            # If the message has attachments, forward them too
            for attachment in message.attachments:
                await monitoring_channel.send(attachment.url)
                
    except Exception as e:
        print(f'Error forwarding message: {str(e)}')

    await bot.process_commands(message)

# Get the token from environment variable
TOKEN = os.getenv('MTI4NzI1NjE0NjY1MDA3NTIyOA.GSjFmn.Px_daKIgxY5AZvcKIVMmLwlMUXyNANreWbJyXo')
bot.run(TOKEN)


