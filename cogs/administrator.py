from datetime import datetime
from datetime import timedelta
import time
import nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption


    

class administrator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    my_guild = 988346089105149992  # Replace with your guild ID

            
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)

    @nextcord.slash_command(name='kick', description='Kick some member in your guild.', guild_ids=[my_guild]) #Work
    @application_checks.has_permissions(administrator=True)
    async def kick(self, bot: nextcord.Interaction, member: nextcord.Member=SlashOption(description="Select a member"), reason: str=SlashOption(description='Tell me your reason why kick', required=False)):
        if reason == None:
            reason = f"No reason by {bot.user}"
            em = nextcord.Embed(title=f'{member.mention}',description=f'{member.mention} has been kicked out of guild.', color=0xff0000)
            em.add_field(name=f'Reason', value=f'{reason}')
            em.timestamp = datetime.now()
            await bot.response.send_message(embed=em, ephemeral=True)
            dm = nextcord.Embed(title='Your has been kicked from server', description=f'{member.mention} you has been kicked from __**{bot.guild}**__', color=0xff0000)
            dm.add_field(name=f'Reason', value=f'{reason}')
            dm.add_field(name='Info', value=f'Guild name : {bot.guild}\n Guild ID : {bot.guild_id}')
            await member.send(embed=dm)
            await member.guild.kick(member, reason=reason)
        else:
            em = nextcord.Embed(title=f'{member.mention}',description=f'{member.mention} has been kicked out of guild.', color=0xff0000)
            em.add_field(name=f'Reason', value=f'{reason}')
            em.timestamp = datetime.now()
            await bot.response.send_message(embed=em, ephemeral=True)
            dm = nextcord.Embed(title='Your has been kicked from server', description=f'{member.mention} you has been kicked from __**{bot.guild}**__', color=0xff0000)
            dm.add_field(name=f'Reason', value=f'{reason}')
            dm.add_field(name='Info', value=f'Guild name : {bot.guild}\n Guild ID : {bot.guild_id}')
            await member.send(embed=dm)
            await member.guild.kick(member, reason=f'{reason} kick by : {bot.user}')

    @nextcord.slash_command(name='ban', description='Ban some member in your guild.', guild_ids=[my_guild]) #Work
    @application_checks.has_permissions(administrator=True)
    async def ban(self, bot: nextcord.Interaction, member: nextcord.Member=SlashOption(description='Select a member'), reason: str=SlashOption(description='Tell me your reason why ban.', required=True), delete_message_days=SlashOption(description='How many day to delete message (max 7 day)', required=False) ):
        if reason == None:
            await bot.response.send_message(f"Sorry i can't ban this user because no reason to ban.")
            return
        else:
            em = nextcord.Embed(title=f'{member}',description=f'{member} has been baned out of guild.', color=0xff0000)
            em.add_field(name=f'Reason', value=f'{reason}')
            em.timestamp = datetime.now()
            await bot.response.send_message(embed=em, ephemeral=True)
            dm = nextcord.Embed(title='Your has been baned from server', description=f'{member} you has been baned from __**{bot.guild}**__', color=0xff0000)
            dm.add_field(name=f'Reason', value=f'{reason}')
            dm.add_field(name='Info', value=f'Guild name : {bot.guild}\n Guild ID : {bot.guild_id}')
            await member.send(embed=dm)
            await member.guild.ban(member, reason=f'{reason} kick by : {bot.user}')
            
    @nextcord.slash_command(name='timeout', description='Soft ban with timeout.', guild_ids=[my_guild]) #Work
    async def timeout(self, bot: nextcord.Interaction, member:nextcord.Member, reason: str=SlashOption(description='Tell me your reason why timeout', required=True), days: int=SlashOption(description='How many days', required=False), hour: int=SlashOption(description='How many hour(s)', required=False), min: int=SlashOption(description='How many minutes', required=False), sec: int=SlashOption(description='How many seconds', required=False)):
        if days == None:
            days=0
        if hour == None:
            hour=0
        if min == None:
            min=0
        if sec == None:
            sec=0
        timeoutdelta = timedelta(days=days, hours=hour, minutes=min, seconds=sec)
        if reason == None:
            await bot.response.send_message(f"Sorry i can't timeout this user because no reason to timeout.")
            return
        else:
            await member.edit(timeout=timeoutdelta)
            await bot.response.send_message(f'User {member.mention} has been timeout for {days} day {hour} Hour {min} min and {sec} sec.', ephemeral=True)

    @nextcord.slash_command(name="clear", description="Clears messages", guild_ids=[my_guild])
    @application_checks.has_guild_permissions(administrator=True)
    async def clear(self, interaction: nextcord.Interaction, amount: int = SlashOption(name="amount", description="Enter the amount of the messages.")):
        if amount > 1000:
            await interaction.response.send_message('Cannot delete more than 1000 messages.', ephemeral=True)
        else:
            await interaction.channel.purge(limit=amount)  # type: ignore
            await interaction.response.send_message(f"Successfully cleared {amount} messages", ephemeral=True)

    
    @nextcord.slash_command(name='create-embed',description='Create a custom embed.', guild_ids=[my_guild])
    @application_checks.has_permissions(administrator=True)
    async def create_mbed(self, bot: nextcord.Interaction, title: str, description: str, url=None, ):
        em = nextcord.Embed(title=title, description=description, url=url, color=0x00ffbf)
        em.set_author(name=bot.user)
        em.timestamp = datetime.now()
        await bot.response.send_message(embed=em)

     
        

    @nextcord.slash_command(name='hellocommand', description='test commands in cogs', guild_ids=[my_guild])
    async def hellocommand(self, bot: nextcord.Interaction):
        await bot.response.send_message('Test commands in cogs is working!')
        

def setup(bot):
  bot.add_cog(administrator(bot))