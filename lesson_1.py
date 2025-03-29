import telebot
import webbrowser
from lesson_6.api_for_bot import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://vk.com/creator_my_life')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, '
                                      f'{message.from_user.first_name} '
                                      f'{message.from_user.last_name}!')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> '
                                      '<em><u>information</u></em>',
                     parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, '
                                          f'{message.from_user.first_name} '
                                          f'{message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)

# bot.infinity_polling()