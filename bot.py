import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет я Нумеробот пришли мне слово!',parse_mode='html')
    

@bot.message_handler()
def get_user_text(message):
    new_msg = config.transform_text(message.text)
    bot.send_message(message.chat.id,new_msg,parse_mode='html')


bot.polling(none_stop=True)