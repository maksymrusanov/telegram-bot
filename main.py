import telebot
bot=telebot.TeleBot('7954199406:AAFisYc8lOMOqBHmske-LtscKqlj-49Bae0')
@bot.message_handler(commands=['start'])
def main(message):
    bot.reply_to(message,'hello')

bot.infinity_polling()
