import discord
from discord.ui import Button,View

bot=discord.Bot()
guild_id=open('guild_id.txt','r',encoding='UTF-8').read()[:-1]

class

@bot.event
async def on_ready():
    print("Raedy...")

@bot.slash_command(guild_ids=[guild_id])
async def ping(ctx):
    await ctx.respond('pong')

@bot.slash_command(guild_ids=[guild_id])
async def button(ctx):
    button=Button(label="test",style=discord.ButtonStyle.green)
    view=View()
    view.add_item(button)
    await ctx.respond("test",view=view)


token=open('token.txt','r',encoding='UTF-8').read()[:-1]
bot.run(token)
