from discord.ext import commands
import discord
import random
import json
import requests
import time

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.command()
async def mines(ctx, round_id):
        mines1, mines2, mines3, mines4, mines5, mines6, mines7, mines8, mines9, mines10, mines11, mines12, mines13, mines14, mines15, mines16, mines17, mines18, mines19, mines20, mines21, mines22, mines23, mines24, mines25 = '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴', '🔴'
        a = random.randint(1, 8)
        b = random.randint(9, 14)
        if a == 1:
            mines1 = "🟢"
        elif a == 2:
            mines2 = "🟢"
        elif a == 3:
            mines3 = "🟢"
        elif a == 4:
            mines4 = "🟢"
        elif a == 5:
            mines5 = "🟢"
        elif a == 6:
            mines6 = "🟢"
        elif a == 7:
            mines7 = "🟢"
        elif a == 8:
            mines8 = "🟢"
        if b == 9:
            mines9 = "🟢"
        elif b == 10:
            mines10 = "🟢"
        elif b == 11:
            mine1 = "🟢"
        elif b == 12:
            mines12 = "🟢"
        elif b == 13:
            mines13 = "🟢"
        elif b == 14:
            mines14 = "🟢"

        row1 = mines1 + mines2 + mines3 + mines4 + mines5
        row2 = mines6 + mines7 + mines8 + mines9 + mines10
        row3 = mines11 + mines12 + mines13 + mines14 + mines15
        row4 = mines16 + mines17 + mines18 + mines19 + mines20
        row5 = mines21 + mines22 + mines23 + mines24 + mines25

        embed = discord.Embed(title="Star Predictions", description=f"\n**Grid**\n```{row1}\n{row2}\n{row3}\n{row4}\n{row5}```\n**Accuracy**\n```42%```")
        embed.set_footer(text="free @ discord.gg/starpredictors")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
        await ctx.send(embed=embed)

@bot.command()
async def towers(ctx, round_id):
  apiembed = discord.Embed(title="Checking Api")
  await ctx.send(embed=apiembed)
  time.sleep(1)
  embed = discord.Embed(description="**Star Predictions**\n**Prediction**\n```✅❌❌\n✅❌❌\n✅❌❌\n❌❌✅\n✅❌❌\n❌✅❌\n✅❌❌\n❌✅❌```\n**Accuracy**\n```25%```")
  embed.set_footer(text="buy @ discord.gg/starpredictors")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009242757413474365/1009834266626113676/Star_Transparent.png?width=657&height=657")
  await ctx.send(embed=embed)
  
  bot.run(token)
