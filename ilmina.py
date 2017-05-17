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

    elif message.content.startswith("イルミナ"):
        await client.send_message(message.channel, "呼んだ？")

    elif message.content.startswith("!exit"):
        await client.send_message(message.channel, "さよなら～")
        await client.logout() # ログアウトとプログラムの終了
        print("終了しました")

    f = {}
    with codecs.open('template.txt', 'r', 'utf-8') as text:
        for line in text:
            line = line.rstrip('\r\n') #改行の削除
            fields = line.split('^')   #^で分割
            f[fields[0]] = fields[1]   #ディクショナリに追加
    keys = f.keys() #キーのリスト化
    for value in keys:
        if message.content.count(value):
            await client.send_message(message.channel, 'どうぞ！\n{}'.format(f[value]))


client.run('TOKEN_PHRASE')
