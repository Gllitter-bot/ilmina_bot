import discord
import sys

client = discord.Client()


@client.event
async def on_ready():  # Botの立ち上げ
    print("ログイン完了")
    print("-" * 30)
    print("ユーザー名:", client.user.name)
    print("ユーザーID:", client.user.id)
    print("-" * 30)


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Botのメッセージには反応しない

    if message.content.startswith("イルミナ"):
        await client.send_message(message.channel, "呼んだ？")

    if message.content.startswith("!shutdown"):
        print("シャットダウン")
        sys.exit() #プログラムの終了

client.run('token')
