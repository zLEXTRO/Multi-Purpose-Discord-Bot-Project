from __future__ import annotations
import os
import sys
import typing 
from typing import Any
import discord
from discord.ext import commands
from discord import app_commands, Colour, Embed, HTTPException, Interaction, SelectOption, TextStyle
from discord.utils import get
from discord.ui import View, Select, TextInput
from datetime import datetime
from dispie import EmbedCreator, ModalInput, SelectPrompt
import asyncio


intents = discord.Intents.all()
bot = commands.Bot(command_prefix= "-", intents=intents)
@bot.event
async def on_ready():
    print(f"logged in as {bot.user.name} ({bot.user.id})")
        

#Unleash the Afterburner
@bot.command()
async def rise(ctx):
    await ctx.send("**On your Command**")
    await ctx.send('*Latency: {0}*'.format(round(bot.latency, 9)))

#sync slash commands
@bot.command()
async def sync(ctx: commands.Context):
	await ctx.send('Synced')
	await bot.tree.sync()

#custom TimeConverter
def TimeConverter(time_str):
    if time_str[-1] == 's':
        return int(time_str[:-1])
    elif time_str[-1] == 'm':
        return int(time_str[:-1]) * 60
    elif time_str[-1] == 'h':
        return int(time_str[:-1]) * 3600
    elif time_str[-1] == 'd':
        return int(time_str[:-1]) * 86400
    else:
        raise commands.BadArgument("Invalid time format. Use [1d/h/m/s] format.")

#tempmute command
@bot.hybrid_command(name='mute', description='Mutes the mentioned user for the given amount of time.')
async def mute(ctx: commands.Context,  member:discord.Member, *, time:TimeConverter = None, reason=None):
#Mutes a member for the specified time in [1d/h/m/s] format ex:  @Someone 1d
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            memRole = discord.utils.get(ctx.guild.roles, name='Member')
            await member.remove_roles(memRole)
            await member.add_roles(role)
            await ctx.send(("Muted {} for {}s" if time else "Muted {}").format(member, time))
            if time:
                await asyncio.sleep(time)
                await member.add_roles(memRole)
                await member.remove_roles(role)
                
#unmute command
@bot.hybrid_command(name='unmute', description='Unmutes the mentioned user.')
async def unmute(ctx: commands.Context, member:discord.Member, *, reason=None):
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            memRole = discord.utils.get(ctx.guild.roles, name='Member')
            await member.remove_roles(role)
            await member.add_roles(memRole)
            await ctx.send(f'Unmuted {member}.')
        
#restrict members from accessing the server 
bot.hybrid_command()
async def restrict(ctx, member:discord.Member, duration: int):
    role = discord.utils.get(ctx.guild.roles, name="Restricted")
    await member.add_roles(role)
    await asyncio.sleep(duration)
    await member.remove_roles(role)
    
#kick command
@bot.hybrid_command(name='kick', brief='kick member')

async def kick(ctx: commands.Context, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)

    await ctx.send(f' {member} has been kicked out.')
        
#Give User IDs from the Ban List
@bot.hybrid_command(name='banlist', brief='Get User IDs from the Ban List')
async def banlist(self, ctx):
    bans = await ctx.guild.bans()
    loop = [f"{u[1]} ({u[1].id})" for user in bans]
    _list = "\r\n".join([f"[{str(num).zfill(2)}] {data}" for num, data in enumerate(loop, start=1)])
    await ctx.send(f"```ini\n{_list}```")

#ban & unban a User after X amount of time
@bot.hybrid_command()
async def softban(ctx, user:discord.User, duration: int):
    await ctx.guild.ban(user)
#set time in seconds
    await asyncio.sleep(60)
    await ctx.guild.unban(user)
    
#Ban Command 
@bot.hybrid_command(name='ban', brief='ban member')
async def ban(ctx: commands.Context, user: discord.Member, *, reason="No reason provided"):
    if isinstance(ctx, discord.ApplicationContext):
        await ctx.defer()
    await user.ban(reason=reason)
    ban = discord.Embed(title=f"{user.name} has been demolished :punch:", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    if isinstance(ctx, discord.ApplicationContext):
        await ctx.respond(embed=ban)
    else:
        await ctx.send(embed=ban)

    
#unban command"
@bot.hybrid_command(name='unban', brief='unban member')
async def unban(ctx: commands.Context, *, user_id: int, reason="No reason provided"):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user, reason=reason)
    unban = discord.Embed(title=f"{user.name} has been given another chance.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    if isinstance(ctx, discord.ApplicationContext):
        await ctx.respond(embed=unban)
    else:
        await ctx.send(embed=unban)


# Delete a number of messages
@bot.hybrid_command(name='purge', brief='Deletes a specified number of messages')
async def purge(ctx: commands.Context, amount: int):
  deleted = await ctx.channel.purge(limit=amount)
  if len(deleted) == 0:
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    embed.description = 'No messages were deleted'
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    if len(deleted) == 1:
      embed.description = '1 message was deleted'
    else: 
      embed.description = f'{len(deleted)} messages were deleted'
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.send(embed=embed)


#give Member a Role(s)
@bot.hybrid_command(pass_context=True)
async def honor(ctx: commands.Context, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"🎖️** {user.name}**, in recognition of your contributions, you have been bestowed the role of ~ {role.mention}   May this honor reflect the zenith of your dedication and commitment to our community")      

#server boost update (Server ID required)
@bot.event
async def on_member_update(before, after):
    yourServer = bot.get_guild(YOUR_SERVER_ID_HERE)
    update_time()
    if 'Server Booster' in after.roles:
        if not 'Server Booster' in str(before.roles):
            await after.add_roles(discord.utils.get(yourServer.roles, name="Giga Chad Server Booster"))
            print(f'{current_datetime} INFO: {after.name} has boosted the server and gained the {role.mention} Role!')
    if 'Server Booster' in str(before.roles):
        if not 'Server Booster' in str(after.roles):
            await after.remove_roles(discord.utils.get(yourServer.roles, name="Donor"))
            print(f'{current_datetime} INFO: {after.name} has stopped boosting the server and lost the Donor Role :(')
            
#embed-builder    
@bot.hybrid_command(name='create-embed', brief='create an advanced Embed message')
async def create_embed(ctx: commands.Context):
    view = EmbedCreator(bot=bot)
    await ctx.send(embed=view.get_default_embed, view=view)

bot.run('BOT_TOKEN')