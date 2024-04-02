import os
import sys
import typing 
from typing import Any
import discord
from discord.ext import commands
from discord import app_commands 
from discord import Embed
from discord.utils import get
from discord.ui import Select
from datetime import datetime
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
@bot.hybrid_command()
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
"""Mutes a member for the specified time in [1d/h/m/s] format ex: -mute @Someone 1d"""
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
        
#kick command
@bot.hybrid_command(name='kick', brief='kick member')

async def kick(ctx: commands.Context, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)

    await ctx.send(f' {member} has been kicked out.')
        
#Give User IDs from the Ban List
@bot.command(name="banlist")
async def banlist(ctx):
    guild = ctx.guild
    if guild:
        banned_ids = await get_banned_user_ids(guild)
        if banned_ids:
            await ctx.send(f"**Banned User IDs:**\n{', '.join(str(uid) for uid in banned_ids)}")
        else:
            await ctx.send("This server doesn't have anyone banned (yet)")
async def get_banned_user_ids(guild):
    banned_users = await guild.bans()
    return [user.user.id for user in banned_users]

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


# Delete the specified number of messages
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


#give role (optional)
@bot.hybrid_command(pass_context=True)
async def honor(ctx: commands.Context, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"🎖️** {user.name}**, in recognition of your contributions, you have been bestowed the role of ~ {role.mention}   May this honor reflect the zenith of your dedication and commitment to our community")      
    

bot.run('BOT_TOKEN')	