from datetime import datetime
from datetime import timedelta
import time
import nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
    

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    my_guild = 988346089105149992  # Replace with your guild ID

            
    @nextcord.slash_command(name='cat', description='Send rendom cat picture.', guild_ids=[my_guild])
    async def randomcatpictre(self, bot: nextcord.Interaction):
       await bot.response.send_message('Neko!')
       
    


def setup(bot):
  bot.add_cog(fun(bot))