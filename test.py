import discord

client = discord.Client()


@client.event
async def on_ready():
    print("ログインしました！")
    print("-" * 30)
    print("ユーザー名:", client.user.name)
    print("ユーザーID:", client.user.id)
    print("-" * 30)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("イルミナ"):
        msg = "呼んだ？ {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)


client.run("")
