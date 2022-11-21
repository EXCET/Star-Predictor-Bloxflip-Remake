from discord.ext import commands
import discord
import random
import json
import requests
import time

bot = commands.Bot(command_prefix='.', help_command=None, intents=discord.Intents.all())




@bot.command()
async def freemines(ctx, round_id):
        mines1, mines2, mines3, mines4, mines5, mines6, mines7, mines8, mines9, mines10, mines11, mines12, mines13, mines14, mines15, mines16, mines17, mines18, mines19, mines20, mines21, mines22, mines23, mines24, mines25 = '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴'
        a = random.randint(1, 8)
        b = random.randint(9, 14)
  
#using a match statement makes code alot simpler :) ~ Contribution: TomScarcity#0001
        match a: #tells the program you want to match the value of a
                case 1: # if a = 1
                        mines1 = "🟢"
                case 2:
                        mines2 = "🟢"
                case 3:
                         mines3 = "🟢"
                case 4:
                        mines4 = "🟢"
                case 5:
                        mines5 = "🟢"
                case 6:
                        mines6 = "🟢"
                case 7:
                        mines7 = "🟢"
                case 8:
                        mines8 = "🟢"
        match b:
                case 9:
                        mines9 = "🟢"
                case 10:
                        mines10 = "🟢"
                case 11:
                        mine11 = "🟢"
                case 12:
                        mines12 = "🟢"
                case 13:
                        mines13 = "🟢"
                case 14:
                        mines14 = "🟢"

        row1 = mines1 + mines2 + mines3 + mines4 + mines5
        row2 = mines6 + mines7 + mines8 + mines9 + mines10
        row3 = mines11 + mines12 + mines13 + mines14 + mines15
        row4 = mines16 + mines17 + mines18 + mines19 + mines20
        row5 = mines21 + mines22 + mines23 + mines24 + mines25

        embed = discord.Embed(title="Star Predictions", description=f"\n**Grid**\n```{row1}\n{row2}\n{row3}\n{row4}\n{row5}```\n**Accuracy**\n```{b}%```")
        embed.set_footer(text="free @ discord.gg/starpredictors")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
        await ctx.send(embed=embed)

@bot.command()
async def towers(ctx, round_id):
  apiembed = discord.Embed(title="Checking Api")
  await ctx.send(embed=apiembed)
  time.sleep(1)
  a = random.randint(1, 3)
  b = random.randint(10, 82)
  if a == 1:
   embed = discord.Embed(description=f"**Star Predictions**\n**Prediction**\n```✅❌❌\n❌✅❌\n✅❌❌\n❌❌✅\n✅❌❌\n❌✅❌\n✅❌❌\n❌✅❌```\n**Accuracy**\n```{b}%```")
   embed.set_footer(text="buy @ discord.gg/starpredictors")
  
   embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
   await ctx.send(embed=embed)
  if a == 2:
   embed = discord.Embed(description=f"**Star Predictions**\n**Prediction**\n```✅❌❌\n❌✅❌\n❌❌✅\n❌✅❌\n❌✅❌\n❌✅❌\n✅❌❌\n✅❌❌```\n**Accuracy**\n```{b}%```")
   embed.set_footer(text="buy @ discord.gg/starpredictors")
  
   embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
   await ctx.send(embed=embed)
  if a == 3:
   embed = discord.Embed(description=f"**Star Predictions**\n**Prediction**\n```✅❌❌\n❌✅❌\n❌❌✅\n❌✅❌\n✅❌❌\n❌✅❌\n❌❌✅\n❌❌✅```\n**Accuracy**\n```{b}%```")
   embed.set_footer(text="buy @ discord.gg/starpredictors")
  
   embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
   await ctx.send(embed=embed)

@bot.command()
async def createkey(ctx, key):
  with open("keys.txt", "a") as f:
   f.write(key + "\n")

@bot.command()
async def claim(ctx, key, member : discord.Member):
 keys = open('keys.txt', 'r')
 read_content = keys.read()
 if f"{key}" in read_content:
    await ctx.send('key valid')
    member = member or ctx.message.author
    guilds = ctx.guild
    role = discord.utils.get(guilds.roles, name="Buyer")
    await member.add_roles(role)
    with open("keys.txt", "r") as f:
     lines = f.readlines()

    with open("keys.txt", "w") as f:
     for line in lines:
        if line.strip("\n") != key:
            f.write(line)
 else:
    await ctx.send('Invalid')

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Star Predictions", description="**.help**\nShows this Message\n**.claim <code>**\nYetkilli\n**.crash**\nHelps you with the outcome of the next game of crash\n**.freemines <amount of mines>**\nHelps you with the outcome of the next game of mines(Free)**\n.mines <amount of mines>**\nHelps you with the outcome of the next game of mines\n**.roulette**\nHelps you with the outcome of the next game of roulette\n**.tower <client seed>**\nHelps you with the outcome of the next game of towers")
  embed.set_footer(text="Free @ discord.gg/MEwqTcMseH")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  await ctx.send(embed=embed)



@bot.command()
async def roulette(ctx):
  purplepred = random.randint(20, 40)
  redpred = random.randint(20, 40)
  yellowpred = random.randint(1, 12)
  embed=discord.Embed(title="Star Predictions")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  embed.add_field(name="Red Prediction", value=f"```{redpred}%```", inline=True)
  embed.add_field(name="Purple Prediction", value=f"```{purplepred}%```", inline=True)
  embed.add_field(name="Yellow Prediction", value=f"```{yellowpred}%```", inline=True)
  Accuracy = redpred + purplepred + yellowpred
  embed.add_field(name="Accuracy", value=f"```{Accuracy}%```", inline=False)
  embed.set_footer(text="Free @ discord.gg/MEwqTcMseH")
  await ctx.send(embed=embed)

@bot.command()
async def crash(ctx):
  embed=discord.Embed(title="Star Predictions")
  A = random.randint(1, 2)
  B = random.randint(1, 2)
  C = random.randint(1, 2)
  if C == 1:
    cur = "above"
  if C == 2:
    cur = "below"
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  embed.add_field(name="Prediction", value=f"```{cur} {A}.{B}```", inline=False)
  Accuracy = random.randint(20, 72)
  embed.add_field(name="Accuracy", value=f"```{Accuracy}%```", inline=False)
  embed.set_footer(text="Free @ discord.gg/MEwqTcMseH")
  await ctx.send(embed=embed)

  
  bot.run(token)
