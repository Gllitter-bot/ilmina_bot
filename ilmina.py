# -*- coding: utf-8 -*-

import codecs
import discord
import json
import urllib.request
import urllib.parse

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
        rep = get_weather(msg)
        await client.send_message(message.channel, rep)

def get_weather(msg):
    '''
    天気はWeather Hacks(http://weather.livedoor.com/weather_hacks/)を利用
    HTTP/GETのリクエストに対してXMLかJSONのデータを返す
    ここではJSONを使用する
    また、場所を追加したい場合は全国の地点定義表(http://weather.livedoor.com/forecast/rss/primary_area.xml)を参照
    '''

    if msg.count("札幌") or msg.count("北海道"):
        city_id = '016010'
    elif msg.count("仙台") or msg.count("宮城"):
        city_id = '040010'
    elif msg.count("水戸") or msg.count("茨城"):
        city_id = '080010'
    elif msg.count("宇都宮") or msg.count("栃木"):
        city_id = '090010'
    elif msg.count("前橋") or msg.count("群馬"):
        city_id = '100010'
    elif msg.count("さいたま") or msg.count("埼玉"):
        city_id = '110010'
    elif msg.count("千葉"):
        city_id = '120010'
    elif msg.count("東京"):
        city_id = '130010'
    elif msg.count("横浜") or msg.count("神奈川"):
        city_id = '140010'
    elif msg.count("新潟"):
        city_id = '150010'
    elif msg.count("名古屋") or msg.count("愛知"):
        city_id = '230010'
    elif msg.count("豊橋"):
        city_id = '230020'
    else:
        responce_str = "場所はどこ？"
        return responce_str

    apiurl = 'http://weather.livedoor.com/forecast/webservice/json/v1'

    try:
        dic = {'city': city_id}
        data = urllib.parse.urlencode(dic)
        url = apiurl + '?' + data
        with urllib.request.urlopen(url) as responce:
            params = json.loads(responce.read().decode('utf-8'))
        # 以下から取得した要素
        title = params['title']
        description = params['description']['text']
        responce_str = ""
        responce_str += title + "です。\n\n"
        forecasts = params['forecasts']
        forecast_array = []
        for forecast in forecasts:
            telop = forecast['telop']

            temperature = forecast['temperature']
            temp_min = temperature['min']
            temp_max = temperature['max']
            temp = ""
            if temp_min is not None:
                if len(temp_min) > 0:
                    temp += "\n最低気温は" + temp_min['celsius'] + "℃"
            if temp_max is not None:
                if len(temp_max) > 0:
                    temp += "\n最高気温は" + temp_max['celsius'] + "℃"
            forecast_array.append(forecast['dateLabel'] + " " + telop + temp)

        if len(forecast_array) > 0:
            responce_str += '\n\n'.join(forecast_array)
        responce_str += '\n\n' + description

    except Exception:
        responce_str = "失敗しちゃった…。"

    return responce_str


client.run('TOKEN_PHRASE')
