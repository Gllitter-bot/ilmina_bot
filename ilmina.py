# -*- coding: utf-8 -*-

import codecs
import discord
from func import weather


client = discord.Client()


@client.event
async def on_ready():  # Botの立ち上げ
    print("起動しました")
    print("-" * 30)
    print("ユーザー名:", client.user.name)
    print("ユーザーID:", client.user.id)
    print("-" * 30)


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Botのメッセージには反応しない

    if message.content == "!exit":
        await client.send_message(message.channel, "さよなら～")
        await client.logout() # ログアウトとプログラムの終了
        print("終了しました")

    elif message.content.count("イルミナ"):
        await client.send_message(message.channel, "呼んだ？")

    dic = {}
    with codecs.open('template.txt', 'r', 'utf-8') as text:
        for line in text:
            line = line.rstrip('\r\n') # 改行の削除
            fields = line.split('^')   # ^で分割
            dic[fields[0]] = fields[1] # ディクショナリに追加
        keys = dic.keys()
        for value in keys:
            if message.content.count(value):
                await client.send_message(message.channel, "どうぞ！\n{}".format(dic[value]))
                print("テンプレートを送信:", value)

    if message.content.count("天気"):
        msg = message.content
        rep = weather.get_weather(msg)
        await client.send_message(message.channel, rep)


client.run('TOKEN_PHRASE')
