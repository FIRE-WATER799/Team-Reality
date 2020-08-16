import discord, os, random, time
from discord import Embed, Colour, Member, User
from discord.ext import commands
from typing import Union

embed_toggle = os.environ['EMBED_TOGGLE']

client = commands.Bot(command_prefix=os.environ['PREFIX'], pm_help=True, owner_id=702954010008748174, case_insensitive=True)

client.remove_command("help")
client._uptime = None

@client.event
async def on_connect():
	if client._uptime is None:
		print(f"Connected to Discord. Getting ready...")
		print(f'-----------------------------')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="To commands and my coder fire#7010"))

@client.command(usage="Learn how to join a role")
async def How_do_I_join_Xetiq(ctx):
  join=""
  join+="1. What server are you \n"
  join+="-NAE \n"
  join+="-NAW \n"
  join+="-EU \n"
  join+="-ASIA \n"
  join+="-OCE \n \n"
  join+="2. What do you want to join as \n \n"
  join+="Cretive Warrior: U need to know to do retakes and edit good. \n \n"
  join+="Comp Player: U need at least 1k in arena. Play alot of solos/duos/squads \n \n"
  join+="TrickShotter: Need to do good trickshots or insane trickshots to join as a Trickshotter \n \n"
  join+="Content Creator: U need atleast 100+ subs to be a content creator \n \n"
  join+="GFX/VFX: U have to make good work and dm staff or owners ur work \n \n"
  join+="And thats how u Join Xetiq so try to join this clan and be apart with the members in the clan!"
  if(embed_toggle=='0'):
    await ctx.send(join)
  if(embed_toggle=='1'):
    join_embed=discord.Embed(color=0x0000, title="How to join", description=join)
    join_embed.set_footer(text="Created by fire#7010") 
    await ctx.send(embed=join_embed)

  
@client.command(usage="Gives help about commands")
async def help(ctx):
    help= "**"
    for command in client.commands:
        help+=f"{command}- `{command.usage}`\n"
    help+="**"   
    if(embed_toggle=='0'):
      await ctx.send(help)
    if(embed_toggle=='1'):
      help_embed=discord.Embed(color=0x0000, title="My Commands", description=help)
      help_embed.set_footer(text="Created by fire#7010") 
      help_embed.set_thumbnail(url='https://image.ibb.co/caM2BK/help.gif')
      help_embed.set_image(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')

      await ctx.send(embed=help_embed)
    
@client.command(hidden=True)
async def Congratulations(ctx, *, arg=None):
  if(ctx.message.author.id==702954010008748174):
    if arg == None:
      if(embed_toggle=='0'):
        await ctx.send("Error: Please specify who you want to congratulate")
      if(embed_toggle=='1'):
        Congratulations_embed_empty = discord.Embed(
          color=0xFF0000
          )
        Congratulations_embed_empty.add_field(name='Error', value="Please specify who you want to congratulate", inline=False)
        Congratulations_embed_empty.set_footer(text="Created by fire#7010") 
        await ctx.send(embed=Congratulations_embed_empty)
    else:
      if(embed_toggle=='0'):
        await ctx.send(f"{ctx.message.author.name}: Congratulates {arg} for joing the team")
      if(embed_toggle=='1'):
        Congratulations_embed_full = discord.Embed(
        color=0x2ECC7
        )
        Congratulations_embed_full.add_field(name=f'{ctx.message.author.name}', value=f"Congratulates {arg} for joing the team", inline=False)
        Congratulations_embed_full.set_footer(text="Created by fire#7010") 
        await ctx.send(embed=Congratulations_embed_full)
  else:
    if(embed_toggle=='0'):
      await ctx.send("Error: You do not have permission to do this")
    if(embed_toggle=='1'):
      Congratulations_embed_error = discord.Embed(
         color=0xFF0000
         )
      Congratulations_embed_error.add_field(name="Error", value="You do not have permission to do this")
      Congratulations_embed_error.set_footer(text="Created by fire#7010") 
      await ctx.send(embed=Congratulations_embed_error)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
		
client.run(os.environ['TOKEN'])