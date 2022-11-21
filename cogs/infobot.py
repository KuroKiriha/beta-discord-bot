from datetime import datetime
from datetime import timedelta
import time
import nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption


    

class infobot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    my_guild = 988346089105149992  # Replace with your guild ID

            
    @nextcord.slash_command(name='ping', description='check ping (ms) bot api.', guild_ids=[my_guild])
    async def testinternet(self, bot: nextcord.Interaction):
        test_internet = round(self.bot.latency * 1000)
        if test_internet >= 300:
            emping=nextcord.Embed(title=self.bot.user, description=f'Ping is {test_internet} MS', color=0xff0000)
            await bot.response.send_message(embed=emping)
        if test_internet <=300:
            emping=nextcord.Embed(title=self.bot.user, description=f'Ping is {test_internet} MS', color=0xff8800)
            await bot.response.send_message(embed=emping)
        if test_internet <=200:
            emping=nextcord.Embed(title=self.bot.user, description=f'Ping is {test_internet} MS', color=0xfff700)
            await bot.response.send_message(embed=emping)
        if test_internet <=100:
            emping=nextcord.Embed(title=self.bot.user, description=f'Ping is {test_internet} MS', color=0x4dff00)
            await bot.response.send_message(embed=emping)
        if test_internet <=50: 
            emping=nextcord.Embed(title=self.bot.user, description=f'Ping is {test_internet} MS', color=0xff61f2)
            emping.add_field(name='No way', value='That impossible')
            await bot.response.send_message(embed=emping)
       
    @nextcord.slash_command(name='botsupport', description='Server support.', guild_ids=[my_guild])
    async def serversupport(self, bot: nextcord.Interaction):
        emsupport=nextcord.Embed(title='Server Support.', description="This is server support about bot, api, etc.", url='https://google.com', color=0x00eeff)
        emsupport.add_field(name='Server Link', value='https://google.com')
        emsupport.set_author(name='Kiriha Developer House', url='https://google.com', icon_url='https://cdn.discordapp.com/attachments/909007484621037578/1027429887490928690/KURO_PROFILE_DIS.webp')
        emsupport.timestamp = datetime.now()
        emsupport.set_footer(text='Owner by : Kuro Kiriha#6690', icon_url='https://cdn.discordapp.com/attachments/909007484621037578/1027429887490928690/KURO_PROFILE_DIS.webp')
        await bot.response.send_message(embed=emsupport)

def setup(bot):
  bot.add_cog(infobot(bot))