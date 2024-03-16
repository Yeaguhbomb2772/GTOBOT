"""
A Discord that lets you play "guess the anime song"
@Author Brandon
Created 6/02/2021 MM/DD/YYYY
"""
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


PREFIX = "!!"
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())


# Load commands cog
async def load_commands():
    print("Loading all commands..")
    await bot.load_extension("commands")
    await bot.load_extension("tcg_commands")
    print("Finished loading all commands.")


@bot.event
async def on_ready():
    print("Bot is now online.")
    await load_commands()


if __name__ == '__main__':
    print("Loading Bot..")
    bot.run(TOKEN)
