import telebot
from telebot import types
import sqlite3
from lesson_6.api_for_bot import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)
name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('learnTBot.sqlite3')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users '
                '(id int auto_increment primary key, '
                'name varchar(50), '
                'pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегистрируем! '
                                      'Введите ваше имя:')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль:')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('learnTBot.sqlite3')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей',
                                          callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('learnTBot.sqlite3')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info_users = ''
    for el in users:
        info_users += f'Имя: {el[1]}, пароль {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info_users)


bot.polling(non_stop=True)
