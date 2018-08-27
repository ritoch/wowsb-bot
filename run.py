import discord
from discord.ext import commands
import glob
import sys
import os.path
import importlib
import re
import asyncio

from version import VERSION as BOTVERSION

bot = commands.Bot(command_prefix='!!')
client = discord.Client()

@bot.event
async def on_ready():
    print('ロード中')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('{0.user}にログインしました。'.format(client))
    print('WoWsb-Botバージョン'+ BOTVERSION+'は正常に起動しました。')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="WoWsb-Bot開発メンバー", color=0xeee657)

    embed.add_field(name="開発リーダー", value="Kosugi_kun")
    embed.add_field(name="軍艦の情報入力", value="MT3\nura4316")
    embed.add_field(name="開発協力", value="WoWsb 日本コミュニティ")
    embed.add_field(name="Botバージョン", value=BOTVERSION)
    embed.add_field(name="ライセンス", value="MIT License")
    embed.add_field(name="著作権", value="Copyright (c) 2018 WoWsb Japan community")
    await ctx.send(embed=embed)

#日本巡洋艦

@bot.command()
async def hashidate(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier I Hashidate (橋立)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Hashidate.jpg")

    # give info about you here
    embed.add_field(name="生存性", value="**継戦能力**\n9858\n**抗堪性**\n･防郭防御5.00％･火災浸水耐性10.00％･装甲5.60％･対水雷防御4.50％\n**装甲**\n ･装甲6mm-30mm･防郭 6mm-30mm･艦首/艦尾 6mm･装甲甲板 10mm")
    embed.add_field(name="主砲射程", value="待っててね")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="機動性", value="待っててね")
    embed.add_field(name="隠蔽性", value="待っててね")
    embed.add_field(name="推力", value="待っててね")

    await ctx.send(embed=embed)

@bot.command()
async def chikuma(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier II Chikuma (筑摩型防護巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Chikuma.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n11990\n**抗堪性**\n･防郭防御7.50％･火災浸水耐性10.00％･装甲5.00％･対水雷防御4.50％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="8.22km")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def tenryu(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier III Tenryu (天龍型軽巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Tenryu.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def kuma(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier IV Kuma (球磨型軽巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/kuma.png")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def furutaka(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier V Furutaka (古鷹型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/furutaka.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def aoba(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier VI Aoba (青葉型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/aoba.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def myoko(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier VII Myoko (妙高型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Myoko.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def takao(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier VIII Takao (妙高型重巡洋艦)", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Takao.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def ibuki(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier IX Ibuki (伊吹型重巡洋艦(改鈴谷型重巡洋艦))", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Ibuki.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

@bot.command()
async def zao(ctx):
    embed = discord.Embed(title="大日本帝国海軍", description="巡洋艦Tier X Zao (蔵王(マル六甲巡))", color=0xeee657)

    embed.set_image(url="https://mcpenano.net/WoWsB/Zao.jpg")

    embed.add_field(name="生存性", value="**継戦能力**\n数値\n**抗堪性**\n･防郭防御<数値>％･火災浸水耐性<数値>％･装甲<数値>％･対水雷防御<数値>％\n**装甲**\n ･装甲さ<数値>mm-<数値>mm･防郭 <数値>mm-<数値>mm･艦首/艦尾 <数値>mm･装甲甲板 <数値>mm")
    embed.add_field(name="主砲射程", value="<数値>")
    embed.add_field(name="機動性", value="<数値>")
    embed.add_field(name="隠蔽性", value="<数値>")
    embed.add_field(name="推力", value="<数値>")

    await ctx.send(embed=embed)

#ここからヘルプ
bot.remove_command('help')
#大日本帝国海軍ヘルプ
@bot.command()
async def japan(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="大日本帝国海軍のコマンドのリストを表示します。", color=0xeee657)

    embed.add_field(name="!!zao", value="大日本帝国海軍 巡洋艦Tier X Zao (蔵王(マル六甲巡))", inline=False)
    embed.add_field(name="!!ibuki", value="大日本帝国海軍 巡洋艦Tier IX Ibuki (伊吹型重巡洋艦(改鈴谷型重巡洋艦))", inline=False)
    embed.add_field(name="!!takao", value="大日本帝国海軍 巡洋艦Tier VIII Takao (妙高型重巡洋艦)", inline=False)
    embed.add_field(name="!!myoko", value="大日本帝国海軍 巡洋艦Tier VII Myoko (妙高型重巡洋艦)", inline=False)
    embed.add_field(name="!!aoba", value="大日本帝国海軍 巡洋艦Tier VI Aoba (青葉型重巡洋艦)", inline=False)
    embed.add_field(name="!!furutaka", value="大日本帝国海軍 巡洋艦Tier V Furutaka (古鷹型重巡洋艦)", inline=False)
    embed.add_field(name="!!kuma", value="大日本帝国海軍 巡洋艦Tier IV Kuma (球磨型軽巡洋艦)", inline=False)
    embed.add_field(name="!!tenryu", value="大日本帝国海軍 巡洋艦Tier III Tenryu (天龍型軽巡洋艦)", inline=False)
    embed.add_field(name="!!chikuma", value="大日本帝国海軍 巡洋艦Tier II chikuma (筑摩型防護巡洋艦)", inline=False)
    embed.add_field(name="!!hashidate", value="大日本帝国海軍 巡洋艦Tier I Hashidate (橋立)", inline=False)


    await ctx.send(embed=embed)

#普通のヘルプ
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="WoWsb Bot", description="船の数が多いので国別のヘルプになります。", color=0xeee657)
    embed.add_field(name="!!info", value="このBotの開発者などを表示します。", inline=False)
    embed.add_field(name="!!help", value="ヘルプを表示します。", inline=False)
    embed.add_field(name="!!japan", value="大日本帝国海軍の軍艦一覧を表示します。", inline=False)


    await ctx.send(embed=embed)

bot.run('bot-token')
