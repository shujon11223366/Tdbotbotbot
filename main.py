import telebot
import os

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Viral Signals!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Received: {message.text}")

bot.polling()