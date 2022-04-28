import discord
import datetime
import os
import math
import time

from discord.ext import commands
from discord.ext.commands import Bot


BotToken = "AddYourBotTokenHere"
BotStatus = "AddYourBotStatusHere"
BotPrefix = "AddYourBotPrefixHere"
SvrURL = "YourServerPermanentInviteLink"
BotURL = "InviteLinkOfYourBot"
YTURL = "YourYouTubeChannelLink" 

bot = commands.Bot(command_prefix = {BotPrefix})
bot.remove_commnand("help")

@bot.event
async def on_ready():
  activity = discord.Game(name =f"{BotStatus}, type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity )
  print ("Launched...")
  print ("My name is " + bot.user.name)
  print ("ID: " + bot.user.id)
                          
@bot.command(aliases = ["Help", "HELP'])
async def help(ctx,  member: discord.Member = None):
   member = ctx.author if not member else member
   e = discord.Embed(title = "Mini Help", description = "Use <Category>Help for extended information.", color=0x2ecc71)
   e.add_field(name = "Category 1", value = f"This Help command has all moderation commands. Use `{BotPrefix}modhelp` to see all moderation commands")  
   e.add_field(name = "Category 2", value = f"This Help command has all gif commands. Use `{BotPrefix}gifhelp` to see all gif commands")     
   e.add_field(name = "Category 3", value = f"This Help command has all games commands. Use `{BotPrefix}gamehelp` to see a;; games commands")  
   e.add_field(name = "Category 4", value = f"This Help command has all Utility commands. Use `{BotPrefix}uhelp` To see all fun commands")
   e.set_thumbnail(url =member.avatar_url)
   e.timestamp = datetime.datetime.utcnow()
   e.set_footer(text = "Requested by {}".format(ctx.message.author.name), icon_url =member.avatar_url)                     
   await ctx.send(embed=e)
 
@bot.command() 
async def modhelp(ctx):   
   e = discord.Embed(title = "Help", description = "This is the Help command for Moderation commands. The commands below check it", color=0xe74c3c)    
   e.add_field(name= "", value = "")                    
   e.add_field(name= "", value = "")                     
   e.add_field(name= "", value = "")                     
   await ctx.send(embed = e)                     
                        
@bot.command()                        
async def gifhelp(ctx):
   await ctx.send(embed = e)                     
                        
@bot.command()                        
async def uhelp(ctx):
   e = discord.Embed(title = "Help", description = "This is the Help command for Utitily commands. The commands below check it", color=0xe74c3c)
   e.add_field(name= "Ping Command :ping_pong:", value = f"This commands shows your ping by valency. Use `{BotPrefix}ping` to check your ping.)                  
   e.add_field(name= "", value = "")
   e.add_field(name=
   e.add_field(name=
   e.add_field(name=
   await ctx.send(embed = e)                         
                        
@bot.command()                        
async def gamehelp(ctx):
   await ctx.send(embed = e)                         
                        
@bot.command()
async def ping(ctx, member: discord.Member = None):
   member = ctx.author if not member else member
   e = discord.Embed(title="Pong :ping_pong:", description = f'Pong! In {round(client.latency * 1000)}ms', color=0xe67e22)
   e.timestamp = datetime.datetime.utcnow()                   
   await ctx.reply(embed = e)
                        
@bot.command(aliases  = ["Invite", "INVITE" ]                      
async def invite(ctx):
   e = discord.Embed(title="Press Me To Invite Bot", description = "Click above hyperlink text to invite the bot to you server", color=0xf1c40f, url={BotURL}
   await ctx.reply(embed = e)
                   
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"{member} has been kicked ")

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You dont have permission to kick the people ")
                          
@bot.command()
commands.has_permissions(ban_members=True)                     
async def ban(ctx, member: discord.Member, *, reason = None):                     
  await member.ban(reason=reason)                     
  await ctx.send(f"{member} has been Banned ")
                                  
@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You dont have permission to kick the people ")                     
                     
                     


bot.run(BotToken)
