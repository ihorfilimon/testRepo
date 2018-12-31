import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    print(message.from_user.id)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.from_user.id != 140180537:
        bot.forward_message(140180537, message.chat.id, message.message_id)
    else:
        reply_message = message.reply_to_messa
        bot.send_message(reply_message.forward_from.id, message.text)
bot.polling(none_stop=True)