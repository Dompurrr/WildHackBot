#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
bot = telebot.TeleBot('5004146707:AAHXsREczeGn1xpICEgXLJGaalDh4-mZaMU')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Ку")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Не помогу, брат...")
    else:
        bot.send_message(message.from_user.id, "Не понял тебя, брат.")

bot.polling(none_stop=True, interval=0)
