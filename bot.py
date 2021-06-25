import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
	print("Bot ready")

for fn in os.listdir("./cogs"):
	if fn.endswith(".py"):
		bot.load_extension(f"cogs.{fn[:-3]}")
	else:
		print(f"{fn[:-3]} could not be loaded!")

bot.run("ODU1NTAwMDg0OTUwNTk3NjMz.YMzYig.OidZfWgwCsejNPPZckUNl6uAGKs")