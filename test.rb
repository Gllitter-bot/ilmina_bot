require 'discordrb'

#botのトークンとクライアントIDを入力
bot = Discordrb::Commands::CommandBot.new token: 'client_token', client_id: 000000000000000000, prefix: '!'

bot.message(containing: "にゃあ") do |event|
  event.respond "わん！"
end

bot.message(containing: ["いるみな", "イルミナ"]) do |event|
  event.respond "呼んだ？"
end

bot.message(containing: ["はげ", "ハゲ", "禿"]) do |event|
  event.respond "わーい！"
end

bot.message(containing: ["何時", "何分"]) do |event|
  t = Time.now
  event.respond "#{t.hour}時#{t.min}分です！"
end

bot.message(containing: ["何月", "何日"]) do |event|
  t = Time.now
  event.respond "#{t.month}月#{t.day}日です！"
end

bot.command(:exit, help_available: false) do |event|
  #退出のコマンド
  break unless event.user.id == User ID
  # 自分のIDを入力
  bot.send_message(event.channel.id, 'さよなら～')
  exit
end

bot.run
