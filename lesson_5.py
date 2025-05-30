import telebot
from currency_converter import CurrencyConverter
from telebot import types
from lesson_6.api_for_bot import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Введите сумму:')
    bot.register_next_step_handler(message, summary)


def summary(message):
    global amount
    try:
        amount = int(message.text.strip())

    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму:')
        bot.register_next_step_handler(message, summary)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение',
                                          callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите пару валют.',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше нуля. '
                                          'Впишите сумму:')
        bot.register_next_step_handler(message, summary)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается: '
                                               f'{round(res, 2)}. '
                                               f'Можете заново вписать сумму:')
        bot.register_next_step_handler(call.message, summary)
    else:
        bot.send_message(call.message.chat.id,
                         'Введите пару валют через слэш "/".')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: '
                                          f'{round(res, 2)}. '
                                          f'Можете заново вписать сумму:')
        bot.register_next_step_handler(message, summary)
    except Exception:
        bot.send_message(message.chat.id, 'Вы ввели не пару валют. '
                                          'Впишите пару валют через слэш "/" '
                                          'снова:')
        bot.register_next_step_handler(message, my_currency)


bot.polling(non_stop=True)
