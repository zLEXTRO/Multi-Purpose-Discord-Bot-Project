import discord
from discord.ext import commands
from discord import Embed
import typing

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= "/", intents=intents)

@bot.event
async def on_ready():
    print("Logged in")


@bot.command()
async def rise(ctx):
    await ctx.send("On your Command")

#mute command
@bot.command(name='mute', brief='mute member')
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Muted')
        await ctx.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)
        
#kick command
@bot.command(name='kick', brief='kick member')

async def kick(ctx, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)

    await ctx.send(f' {member} has been kicked out.')
    
    

#Ban Command 
@commands.has_permissions(ban_members=True)
@bot.command(name='ban', brief='ban member')
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f" {user.name} has been demolished :punch: ", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)
    
#unban command"
@bot.command(name='unban', brief='unban member')
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}, Welcome Back.')
            return
    await ctx.send("User not found in the ban list.")

@commands.has_permissions(manage_messages=True)
@bot.command(name='purge', brief='Deletes a specified number of messages')
async def purge(ctx, amount: int):
  
  # Delete the specified number of messages
  deleted = await ctx.channel.purge(limit=amount)
  if len(deleted) == 0:
    
    # If no messages were deleted, create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    embed.description = 'No messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_thumbnail(url=ctx.author.avatar.url)
    
    # Send the embed message
    await ctx.send(embed=embed)
  else:
    
    # Create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    if len(deleted) == 1:
      
      # singular & plural purge message(s)
      embed.description = '1 message was deleted'
    else:
      
      embed.description = f'{len(deleted)} messages were deleted'
      
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_thumbnail(url=ctx.author.avatar.url)
    
    # Send the embed message
    await ctx.send(embed=embed)
             
bot.run('INSERT BOT TOKEN')	