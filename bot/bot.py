import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# Initialize Discord client
bot = commands.Bot(command_prefix='!')

# Function to scrape information from Cornell Lab of Ornithology website
def get_bird_info(bird_name):
    url = f"https://www.allaboutbirds.org/guide/{bird_name.replace(' ', '-').lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Parse required information from the webpage
        description = soup.find('div', class_='species-info').get_text().strip()
        return description
    else:
        return "Bird not found or an error occurred."

# Define command to get bird information
@bot.command()
async def bird(ctx, *, bird_name):
    bird_info = get_bird_info(bird_name)
    await ctx.send(bird_info)

# Run the bot
bot.run('MTIxOTI1NDY1OTM5NTYxNjg0MA.G32dp6.03qAk8FsXES3wgMgYCfYG5G2sBUX3DFXCrCTgk')

