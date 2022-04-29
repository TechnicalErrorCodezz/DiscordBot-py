import keep_alive
import discord
import datetime
import os
import math
import asyncio


from discord.ext import commands
from discord.ext.commands import Bot


BotToken = "AddYourBotTokenHere"
BotStatus = "AddYourBotStatusHere"
BotPrefix = "AddYourBotPrefixHere"
SvrURL = "YourServerPermanentInviteLink"
BotURL = "InviteLinkOfYourBot"
YTURL = "YourYouTubeChannelLink" 

hug = "https://tenor.com/view/super-excited-gif-23565980"
kiss = "https://tenor.com/view/anime-couple-val-ally-kiss-gif-24860682"
slap = "https://tenor.com/view/girl-slap-anime-mad-student-gif-17423278"
kick = "https://tenor.com/view/anime-ouch-kick-fly-gif-15847183"
hit = "https://tenor.com/view/head-hit-anime-cute-gif-15150394"
run = "https://tenor.com/view/anime-run-gif-19844330"
hi = "https://tenor.com/view/gakkou-gurashi-hello-hi-wave-gif-13649735"
hello = "https://tenor.com/view/anime-hello-hi-hi-there-gif-14835859"
bye = "https://tenor.com/view/anime-hello-hi-hi-there-gif-14835859"
shoot = "https://tenor.com/view/nichijou-minigun-comedy-anime-fuck-you-gif-14778256"
kill = "https://tenor.com/view/anime-gif-19109520"
love = "https://tenor.com/view/love-you-gif-22738857"
wtf = "https://tenor.com/view/anime-cute-shocked-zoom-surprised-gif-15198304"
heart = "https://tenor.com/view/heart-floating-gif-24649295"
pat = "https://tenor.com/view/fantasista-doll-anime-headpat-headpats-headpats-anime-gif-24213094"
wth = "https://tenor.com/view/jeanne-vanitas-no-carte-anime-angry-anime-girl-anime-sad-gif-25096160"
shy = "https://tenor.com/view/shy-anime-embarassed-girl-gif-15974488"

bot = commands.Bot(command_prefix = {BotPrefix})
bot.remove_command("help")

@bot.event
async def on_ready():
  activity = discord.Game(name =f"{BotStatus}, type=3)
  await bot.change_presence(status=discord.Status.idle, activity=activity )
  print ("Launched...")
  print ("My name is " + bot.user.name)
  print ("ID: " + bot.user.id)
                          
@bot.command(aliases = ["Help", "HELP"])
async def help(ctx,  member: discord.Member = None):
   member = ctx.author if not member else member
   e = discord.Embed(title = "Mini Help", description = "Use <Category>Help for extended information.", color=0x2ecc71)
   e.add_field(name = "Category 1", value = f"This Help command has all moderation commands. Use `{BotPrefix}modhelp` to see all moderation commands", inline=True)  
   e.add_field(name = "Category 2", value = f"This Help command has all gif commands. Use `{BotPrefix}gifhelp` to see all gif commands", inline=True)     
   e.add_field(name = "Category 3", value = f"This Help command has all games commands. Use `{BotPrefix}gamehelp` to see a;; games commands", inline=True)  
   e.add_field(name = "Category 4", value = f"This Help command has all Utility commands. Use `{BotPrefix}uhelp` To see all fun commands",inline=True)
   e.set_thumbnail(url =member.avatar_url)
   e.timestamp = datetime.datetime.utcnow()
   e.set_footer(text = "Requested by {}".format(ctx.message.author.name), icon_url =member.avatar_url)                     
   await ctx.send(embed=e)
 
@bot.command() 
async def modhelp(ctx):   
   e = discord.Embed(title = "Help", description = "This is the Help command for Moderation commands. The commands below check it", color=0xe74c3c)    
   e.add_field(name= f"{BotPrefix}kick", value = "Kick a user from your server", inline=True)                    
   e.add_field(name= f"{BotPrefix}ban", value = "Ban a user from your server", inline=True)                     
   e.add_field(name= "Coming soon ", value = "Coming Soon", inline=True)                     
   await ctx.send(embed = e)                     
                        
@bot.command()                        
async def gifhelp(ctx):
   e = discord.Embed(title="Help", description = "This is the Help command for GIF commands. The commands are below check it", color=0xe74c3c)
   e.add_field(name=f"{BotPrefix}hi", value = "GIF"                      
   e.add_field(name=f"{BotPrefix}hello", value = "GIF"                         
   e.add_field(name=f"{BotPrefix}bye", value = "GIF"                         
   e.add_field(name=f"{BotPrefix}slap", value = "GIF"                         
   e.add_field(name=f"{BotPrefix}Kick", value = "GIF (Use Capital K)"                         
   e.add_field(name=f"{BotPrefix}kiss", value = "GIF"              
   e.add_field(name=f"{BotPrefix}hug", value = "GIF"  
   e.add_field(name=f"{BotPrefix}love", value = "GIF"              
   e.add_field(name=f"{BotPrefix}pat", value = "GIF"              
   e.add_field(name=f"{BotPrefix}hit", value = "GIF"              
   e.add_field(name=f"{BotPrefix}shoot", value = "GIF"            
   e.add_field(name=f"{BotPrefix}run", value = "GIF"           
   e.add_field(name=f"{BotPrefix}wtf", value = "GIF"           
   e.add_field(name=f"{BotPrefix}wth", value = "GIF"
   e.add_field(name=f"{BotPrefix}shy", value = "GIF"            
   e.add_field(name=f"{BotPrefix}heart", value = "GIF"            
   await ctx.send(embed = e)                     
                        
@bot.command()                        
async def uhelp(ctx):
   e = discord.Embed(title = "Help", description = "This is the Help command for Utitily commands. The commands below check it", color=0xe74c3c)
   e.add_field(name= f"{BotPrefix}ping", value = "This commands shows your ping by valency.", inline=True)                  
   e.add_field(name= f"{BotPrefix}invite", value = "By This command you can this invite this bot", inline=True)
   e.add_field(name= f"{BotPrefix}avatar", value = "Get your/Someone's Avatar", inline=True)
   e.add_field(name= f"{BotPrefix}purge", value = "Delete's the messages how much you want to delete.", inline=True)
   e.add_field(name= f"{BotPrfix}serverinfo", value = "Show's the information of this server", inline=True )                       
   await ctx.send(embed = e) 
               
@bot.command()                        
async def gamehelp(ctx):
   await ctx.send("We Are Working On It")                         
                        
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
 
@bot.command()
async def heart(ctx):
  await ctx.reply("https://tenor.com/view/heart-floating-gif-24649295")
@bot.command()
async def pat(ctx):                     
  await ctx.reply("https://tenor.com/view/fantasista-doll-anime-headpat-headpats-headpats-anime-gif-24213094")
@bot.command()                     
async def love(ctx):                     
  await ctx.reply("https://tenor.com/view/love-you-gif-22738857")                  
@bot.command()                     
async def Kick(ctx):
  await ctx.reply("https://tenor.com/view/anime-ouch-kick-fly-gif-15847183")                                      
@bot.command()                     
async def hi(ctx):                     
   await ctx.reply("https://tenor.com/view/gakkou-gurashi-hello-hi-wave-gif-13649735")
@bot.command()                     
async def bye(ctx):                     
   await ctx.reply("https://tenor.com/view/anime-hello-hi-hi-there-gif-14835859")                   
@bot.command()                     
async def hug(ctx):                     
   await ctx.reply("https://tenor.com/view/super-excited-gif-23565980")                    
@bot.command()                     
async def kiss(ctx):                     
   await ctx.reply("https://tenor.com/view/anime-couple-val-ally-kiss-gif-24860682")
@bot.command()                     
async def slap(ctx):                     
   await ctx.reply("https://tenor.com/view/girl-slap-anime-mad-student-gif-17423278")                     
@bot.command()                     
async def hit(ctx):                     
   await ctx.reply("https://tenor.com/view/head-hit-anime-cute-gif-15150394")                     
@bot.command()                     
async def shy(ctx):                     
   await ctx.reply("https://tenor.com/view/shy-anime-embarassed-girl-gif-15974488")                     
@bot.command()                     
async def kill(ctx):                     
   await ctx.reply("https://tenor.com/view/anime-gif-19109520")                     
@bot.command()                     
async def shoot(ctx):                     
   await ctx.reply("https://tenor.com/view/nichijou-minigun-comedy-anime-fuck-you-gif-14778256")                     
@bot.command()                     
async def hello(ctx):                     
   await ctx.reply("https://tenor.com/view/anime-hello-hi-hi-there-gif-14835859")                                         
@bot.command()                     
async def wtf(ctx):                     
   await ctx.reply("https://tenor.com/view/anime-cute-shocked-zoom-surprised-gif-15198304")                       
@bot.command()                     
async def wth(ctx):                     
   await ctx.reply("https://tenor.com/view/jeanne-vanitas-no-carte-anime-angry-anime-girl-anime-sad-gif-25096160")                       
@bot.command()                     
async def run(ctx):                     
   await ctx.reply("https://tenor.com/view/anime-run-gif-19844330")                       
                     
@bot.command(aliases = ["av"])
async def avatar(ctx, member: discord.Member=None):
   if member = None:
      member = ctx.author               
   memberAvatar = member.avatar_url
   e = discord.Embed(title=f"{member.name}'s Avatar")
   e.set_image(url =memberAvatar                  
   await ctx.send(embed = e)                  
@bot.command(aliases = ["clear", "purge"])
async def purge(ctx, amount=int):
   if amount > 1000:
      await ctx.send(f"Too many messages to purge ({amount}/1000)
   else:
      count_members = {}
      messages = await ctx.channel.history(limit=amount).flatten()
      for message in messages[1:]:
         if (message.author) in count_members:
            count_members[str(message.author)] += 1
         else:
            count_members[str(message.author)] = 1 
      new_string = []
      deleted_messages = 0           
      for author, message_deleted in list(count_members.items()):
         new_string.append(f"**{author}**: {message_deleted")
         deleted_messages += message_deleted
      final_string = "\n".join(new_string)               
      await ctx.channel.purge(limit=amount+1)
      if deleted_messages == 1:
         msg = await ctx.send(f"{deleted_messages} message were Deleted successfully. \n\n{final_string}")  
      elif:
         msg = await ctx.send("No messages were deleted. Make sure messages aren't more than 2 weeks old.")
      else:
         msg = await ctx.send(f"{deleted_messages} messages were Deleted successfully. \n\n{final_string}")    
      await asyncio.sleep(2)   
      await msg.delete()

@bot.command(aliases = ["si", "server"], pass_context=True)
async def serverinfo(ctx, member: discord.Member=None):
   e = discord.Embed(tilte="Server Information", color=0x9208ea)
   e.add_field(name="Server Name", value=f"{ctx.guild.name}", inline=True)
   e.add_field(name="Server ID", value = f"{ctx.guild.id}", inline=True
   e.add_field(name="Roles", value =f"{ctx.guild.roles}", inline=True)
   e.add_field(name="Members count", value=f"{ctx.guild.member_count}", inline=True)
   e.set_thumbnail(url=f"{ctx.guild.icon_url}")
   e.set_footer(text = "Requested by {}".format(ctx.message.author.name), icon_url =member.avatar_url)
   await ctx.reply(embed = e)




keep_alive.keep_alive()
bot.run(BotToken)
