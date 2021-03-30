import telebot
import configure
from telebot import types
import random

list = ["Да", "Нет"]
client = telebot.TeleBot(configure.config['token'])

@client.message_handler()
def user_answer(message):
    text = message.text
    text = text.lower()
    if '!аладин' in text:
        otvet = random.choice(list)
        client.send_message(message.chat.id, otvet)


client.polling(none_stop=True, interval=0)