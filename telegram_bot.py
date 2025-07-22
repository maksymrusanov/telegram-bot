import os

import telebot
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['s'])
def send_welcome(message):
    bot.reply_to(message, "hello,do you want to start bot?")


bot.infinity_polling()
