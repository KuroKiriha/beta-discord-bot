import os

import nextcord
from nextcord.ext import commands

import config

from stroage import badwordlist



my_guild = 988346089105149992  # Replace with your guild ID

Intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix='km!', intents=Intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(extension)
    await ctx.send(f'Loaded {extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(extension)
    await ctx.send(f'Unloaded {extension}')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(extension)
    await ctx.send(f'Reloaded {extension}')

@bot.slash_command(description="My first slash command", guild_ids=[my_guild])
async def hello(interaction: nextcord.Interaction):
    await interaction.response.send_message("Hello!", ephemeral=True)

bot.run(config.TOKEN)    