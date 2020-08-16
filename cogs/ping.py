import discord, time, os
from discord.ext import commands

embed_toggle= os.environ['EMBED_TOGGLE']

class ping(commands.Cog):
  
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded ping.py')
    
    @commands.command(usage="Get's the bot's ping")
    async def ping(self, ctx):
      before = time.monotonic()
      message = await ctx.send("Pinging")
      ping = (time.monotonic() - before) * 1000
      ping_content = (f":ping_pong:   |   {int(ping)}ms\n"
             f":timer:   |   {self.client.latency * 1000:.0f}ms")
      if(embed_toggle=='0'):
        await message.delete()
        await ctx.send("Ping dose not support non-embeds")
      if(embed_toggle=='1'):
        ping_embed=discord.Embed(color=0x0000, title="Pong", description=ping_content)
        ping_embed.set_footer(text="Created by fire#7010") 
        await message.edit(embed=ping_embed)
        
def setup(client):
    client.add_cog(ping(client))
