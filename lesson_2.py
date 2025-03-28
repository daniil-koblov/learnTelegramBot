import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти в поисковик.')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото.')
    btn3 = types.KeyboardButton('Изменить текст.')
    markup.row(btn2, btn3)
    file = open('./bot_hello.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти в поисковик.':
        bot.send_message(message.chat.id, 'Поисковик открылся.')
    elif message.text == 'Удалить фото.':
        bot.send_message(message.chat.id, 'Фото удалено.')
    elif message.text == 'Изменить текст.':
        bot.send_message(message.chat.id, 'Текст изменен.')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти в поисковик.',
                                          url='https://ya.ru/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото.',
                                      callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст.',
                                      callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Это фото.', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id,
                           callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id,
                              callback.message.message_id)


bot.polling(non_stop=True)
