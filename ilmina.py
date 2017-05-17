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
    # 試験用
    # コマンドラインにメッセージを表示
    print (message.content)
    if message.author == client.user:
        return  # Botのメッセージには反応しない

    elif message.content.count("イルミナ"):
        await client.send_message(message.channel, "呼んだ？")

    elif message.content.startswith("!exit"):
        await client.send_message(message.channel, "さよなら～")
        await client.logout() # ログアウトとプログラムの終了
        print("終了しました")

    pageDic = {}
    with codecs.open('template.txt', 'r', 'utf-8') as text :
        for line in text :
            line = line.rstrip('\r\n') #改行の削除
            fields = line.split('^')   #^で分割
            pageDic[fields[0]] = fields[1]   #ディクショナリに追加
    keys = pageDic.keys()
    # error:::count(x)のときxはstr必須
    if message.content.count(keys):
        await client.send_message(message.channel, 'どうぞ！\n{}'.format(pageDic[message.content]))

# イルミナさんは挨拶する
async def greeting():
    print ('a')
    # 時刻の取得
    # 挨拶文を決定
    # メッセージを送信
    # 他になにか定型文があっても良いかも

if __name__=='__main__':
    # ilmina.py:52: RuntimeWarning: coroutine 'greeting' was never awaited greeting()
    # greeting()
    client.run('TOKEN_PHRASE')
