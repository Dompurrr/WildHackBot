#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import sqlite3

bot = telebot.TeleBot('5004146707:AAHXsREczeGn1xpICEgXLJGaalDh4-mZaMU')

@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
            #connecting to db
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()

            #creating db if doesn't exists
            cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
                id INTEGER,
                name TEXT,
                surname TEXT,
                patronymic TEXT,
                sex TEXT,
                age INTEGER,
                status INTEGER
            )""")
            connect.commit()

            #Check if user is already in db
            people_id = message.chat.id
            cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
            data = cursor.fetchone()
            if data is None:
                user_id = [message.chat.id, "Null", "Null", "Null", "Null", 0]
                print("INFO: id", message.chat.id, " sended message")
                cursor.execute("INSERT INTO login_id(id, name, surname, patronymic, sex, status) VALUES(?, ?, ?, ?, ?, ?);", user_id)
                connect.commit()

                bot.send_message(message.from_user.id, "Здравствуйте, мы рады, что вы проявили интерес и желаете стать волонтером.")
                bot.send_message(message.from_user.id, "В начале мы бы хотели задать вам пару вопросов для лучшего общения  с вами.")
                bot.send_message(message.from_user.id, "Как вас зовут?")
                bot.register_next_step_handler(message, get_name)
            else:
                bot.send_message(message.chat.id, 'Вы уже начали подавать заявку :)')

def get_name(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    inpName = (message.text)
    cursor.execute(f"UPDATE login_id SET name = '{inpName}' WHERE id = {message.chat.id}")
    connect.commit()
    bot.send_message(message.from_user.id, 'А фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    inpSurname = message.text;
    cursor.execute(f"UPDATE login_id SET surname = '{inpSurname}' WHERE id = {message.chat.id}")
    connect.commit()
    bot.send_message(message.from_user.id, 'Сколько вам лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    inpAge = 0;
    while inpAge == 0:
        try:
             age = int(message.text)
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    cursor.execute(f"UPDATE login_id SET age = {inpAge} WHERE id = {message.chat.id}")
    connect.commit()
    bot.send_message(message.from_user.id, 'Какой ваш пол? (Просто 1 русской буквой: М или Ж)');
    bot.register_next_step_handler(message, get_sex);

def get_sex(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    inpSex = message.text;
    cursor.execute(f"UPDATE login_id SET sex = '{inpSex}' WHERE id = {message.chat.id}")
    connect.commit()







bot.polling(none_stop=True, interval=0)

# @bot.message_handler(commands=['start'])
# def start(message):
#     #connecting to db
#     connect = sqlite3.connect('users.db')
#     cursor = connect.cursor()
#
#     #creating db if doesn't exists
#     cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
#         id INTEGER,
#         name TEXT,
#         surname TEXT,
#         patronymic TEXT,
#         sex TEXT,
#         status INTEGER
#     )""")
#     connect.commit()
#
#     #Check if user is already in db
#     people_id = message.chat.id
#     cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
#     data = cursor.fetchone()
#     if data is None:
#         user_id = [message.chat.id, "Null", "Null", "Null", "Null", 0]
#         print("INFO: id", message.chat.id, " sended message")
#         cursor.execute("INSERT INTO login_id(id, name, surname, patronymic, sex, status) VALUES(?, ?, ?, ?, ?, ?);", user_id)
#         connect.commit()
#     else:
#         bot.send_message(message.chat.id, 'Вы уже начали подавать заявку :)')
