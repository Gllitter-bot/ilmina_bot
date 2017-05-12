import codecs
import discord

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

    if message.content.startswith("イルミナ"):
        await client.send_message(message.channel, "呼んだ？")

    if message.content.startswith("!exit"):
        await client.send_message(message.channel, "さよなら～")
        await client.logout() # ログアウトとプログラムの終了
        print("終了しました")

    f = {}

    with codecs.open('template.txt', 'r', 'utf-8') as text :
        for line in text :
            line = line.rstrip('\r\n')
            fields = line.split('^')
            f[fields[0]] = fields[1]

    if message.content in f:
        await client.send_message(message.channel, '{}'.format(f[message.content]))


client.run('TOKEN_PHRASE')
