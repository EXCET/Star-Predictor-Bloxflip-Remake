from discord.ext import commands
import discord
import random
import json
import requests
import time
import string
from webserver import keep_alive
import os

bot = commands.Bot(command_prefix='.', help_command=None, intents=discord.Intents.all())


ids = []

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def mines(ctx, mines, id):
 if id in ids:
   await ctx.send('Prediction Already Made')
 else:
  if ctx.channel.id == 1051221668267311134:
   if len(id) == 36:
        mines1, mines2, mines3, mines4, mines5, mines6, mines7, mines8, mines9, mines10, mines11, mines12, mines13, mines14, mines15, mines16, mines17, mines18, mines19, mines20, mines21, mines22, mines23, mines24, mines25 = ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:', ':question:'
        a = random.randint(1, 8)
        b = random.randint(9, 14)
        c = random.randint(15, 25)
        if a == 1:
            mines1 = ":white_check_mark:"
        elif a == 2:
            mines2 = ":white_check_mark:"
        elif a == 3:
            mines3 = ":white_check_mark:"
        elif a == 4:
            mines4 = ":white_check_mark:"
        elif a == 5:
            mines5 = ":white_check_mark:"
        elif a == 6:
            mines6 = ":white_check_mark:"
        elif a == 7:
            mines7 = ":white_check_mark:"
        elif a == 8:
            mines8 = ":white_check_mark:"
        if b == 9:
            mines9 = ":white_check_mark:"
        elif b == 10:
            mines10 = ":white_check_mark:"
        elif b == 11:
            mine11 = ":white_check_mark:"
        elif b == 12:
            mines12 = ":white_check_mark:"
        elif b == 13:
            mines13 = ":white_check_mark:"
        elif b == 14:
            mines14 = ":white_check_mark:"
        if c == 15:
          mines15 = ":white_check_mark:"
        elif c == 16:
          mines16 = ":white_check_mark:"
        elif c == 17:
          mines17 = ":white_check_mark:"
        elif c == 18:
          mines18 = ":white_check_mark:"
        elif c == 19:
          mines19 = ":white_check_mark:"
        elif c == 20:
          mines20 = ":white_check_mark:"
        elif c == 21:
          mines21 = ":white_check_mark:"
        elif c == 22:
          mines22 = ":white_check_mark:"
        elif c == 23:
          mines23 = ":white_check_mark:"
        elif c == 24:
          mines24 = ":white_check_mark:"
        elif c == 25:
          mines25 = ":white_check_mark:"

        row1 = mines1 + mines2 + mines3 + mines4 + mines5
        row2 = mines6 + mines7 + mines8 + mines9 + mines10
        row3 = mines11 + mines12 + mines13 + mines14 + mines15
        row4 = mines16 + mines17 + mines18 + mines19 + mines20
        row5 = mines21 + mines22 + mines23 + mines24 + mines25
        chance = random.randint(1, 99)

        embed = discord.Embed(title="Star Predictions", description=f"\n**Prediction**\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n**Accuracy**\n{chance}%", color=0xff0000)
        embed.set_footer(text="Buy @ https://discord.gg/weXekdMMSb")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
        await ctx.send(embed=embed)
        ids.append(id)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def towers(ctx, id):
 if id in ids:
   await ctx.send('Prediction Already Made')
 else:
  if ctx.channel.id == 1051221668267311134:
   if len(id) == 36:
        tower1,tower2,tower3,tower4,tower5,tower6,tower7,tower8,tower9,tower10,tower11,tower12,tower13,tower14,tower15,tower16,tower17,tower18,tower19,tower20,tower21,tower22,tower23,tower24 = ":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:",":question:"
        a = random.randint(1, 3)
        b = random.randint(1, 3)
        c = random.randint(1, 3)
        d = random.randint(1, 3)
        e = random.randint(1, 3)
        f = random.randint(1, 3)
        g = random.randint(1, 3)
        h = random.randint(1, 3)

        if a == 1:
            tower1 = ":white_check_mark:"
        elif a == 2:
            tower2 = ":white_check_mark:"
        elif a ==3:
            tower3 = ":white_check_mark:"
        if b == 1:
            tower4 = ":white_check_mark:"
        elif b == 2:
            tower5 = ":white_check_mark:"
        elif b ==3:  
            tower6 = ":white_check_mark:"
        if c == 1:
            tower7 = ":white_check_mark:"
        elif c == 2:
            tower8 = ":white_check_mark:"
        elif c ==3:
            tower9 = ":white_check_mark:"
        if d == 1:
            tower10 = ":white_check_mark:"
        elif d == 2:
            tower11 = ":white_check_mark:"
        elif d ==3:
            tower12 = ":white_check_mark:"
        if e == 1:
            tower13 = ":white_check_mark:"
        elif e == 2:
            tower14 = ":white_check_mark:"
        elif e ==3:
            tower15 = ":white_check_mark:"
        if f == 1:
            tower16 = ":white_check_mark:"
        elif f == 2:
            tower17 = ":white_check_mark:"
        elif f ==3:
            tower18 = ":white_check_mark:"
        if g == 1:
            tower19 = ":white_check_mark:"
        elif g == 2:
            tower20 = ":white_check_mark:"
        elif g ==3:
            tower21 = ":white_check_mark:"
        if h == 1:
            tower22 = ":white_check_mark:"
        elif h == 2:
            tower23 = ":white_check_mark:"
        elif h ==3:
            tower24 = ":white_check_mark:"


        row1 = tower1 + tower2 + tower3
        row2 = tower4 + tower5 + tower6
        row3 = tower7 + tower8 + tower9
        row4 = tower10 + tower11 + tower12
        row5 = tower13 + tower14 + tower15
        row6 = tower16 + tower17 + tower18
        row7 = tower19 + tower20 + tower21
        row8 = tower22 + tower23 + tower24
        #await ctx.send(row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8)
        info = str(random.randint(45, 95))
        pfp = 'https://cdn.discordapp.com/attachments/1049781596401700924/1051224884447023174/download_12.jpg'
        list = [0xff0000]
        color = random.choice(list)
        em = discord.Embed(color=color)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Buy @ https://discord.gg/weXekdMMSb")
        em.add_field(name="Star Predictions", value=row1 + "\n" + row2 + "\n" + row3 + "\n" +row4 + "\n" +row5 + "\n" +row6 + "\n" +row7 + "\n" +row8 + "\n" + "**Accuracy**" + "\n" + info + "%")   
        await ctx.send(embed=em)
        ids.append(id)
        

@bot.command()
@commands.has_role("Hidden")
async def createkey(ctx):
  key = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

  with open("keys.txt", "a") as f:
   f.write(key + "\n")
   await ctx.send(f'{key}')

@bot.command()
async def claim(ctx, key):
 keys = open('keys.txt', 'r')
 read_content = keys.read()
 if f"{key}" in read_content:
    embed=discord.Embed(title="Subscription", description="Buy @ discord.gg/weXekdMMsb", color=0xff0000)
    embed.add_field(name="Subscription Valid", value="You Now Have Access", inline=False)
    await ctx.send(embed=embed)
    member = ctx.message.author
    guilds = ctx.guild
    role = discord.utils.get(guilds.roles, name="Buyer")
    await member.add_roles(role)
    with open("keys.txt", "r") as f:
     lines = f.readlines()

    with open("keys.txt", "w") as f:
     for line in lines:
        if line.strip("\n") != f'{key}':
            f.write(line)
 else:
    await ctx.send('Invalid')

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Star Predictions", description="**.help**\nShows this Message\n**.claim <code>**\nClaims A Key We Send When You Buy\n**.crash**\nHelps you with the outcome of the next game of crash\n**.mines <amount of mines> <round id>**\nHelps you with the outcome of the next game of mines\n**.roulette**\nHelps you with the outcome of the next game of roulette\n**.towers <round id>**\nHelps you with the outcome of the next game of towers", color=0xff0000)
  embed.set_footer(text="Buy @ https://discord.gg/weXekdMMSb")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  await ctx.send(embed=embed)


@commands.cooldown(1, 23, commands.BucketType.user)
@bot.command()
async def roulette(ctx):
 if ctx.channel.id == 1051221668267311134:
  purplepred = random.randint(20, 40)
  redpred = random.randint(20, 40)
  yellowpred = random.randint(1, 12)
  embed=discord.Embed(title="Star Predictions", color=0xff0000)
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  embed.add_field(name="Red Prediction", value=f"```{redpred}%```", inline=True)
  embed.add_field(name="Purple Prediction", value=f"```{purplepred}%```", inline=True)
  embed.add_field(name="Yellow Prediction", value=f"```{yellowpred}%```", inline=True)
  Accuracy = redpred + purplepred + yellowpred
  embed.add_field(name="Accuracy", value=f"```{Accuracy}%```", inline=False)
  embed.set_footer(text="Free @ discord.gg/MEwqTcMseH")
  await ctx.send(embed=embed)
@commands.cooldown(1, 25, commands.BucketType.user)
@bot.command()
async def crash(ctx):
 if ctx.channel.id == 1051221668267311134:
  embed=discord.Embed(title="Star Predictions", color=0xff0000)
  A = random.randint(1, 2)
  B = random.randint(1, 9)
  C = random.randint(1, 1)
  if C == 1:
    cur = "above"

  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  embed.add_field(name="Prediction", value=f"```{cur} {A}.{B}```", inline=False)
  Accuracy = random.randint(20, 72)
  embed.add_field(name="Accuracy", value=f"```{Accuracy}%```", inline=False)
  embed.set_footer(text="Free @ discord.gg/MEwqTcMseH")
  await ctx.send(embed=embed)



bot.run('token-here')

