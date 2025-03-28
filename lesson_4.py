import telebot
import requests
import json
from lesson_6.config import TOKEN, TOKENOWM

bot = telebot.TeleBot(TOKEN)
API = TOKENOWM


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши название своего города:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
        f'{API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода в городе {city.capitalize()}:'
                              f' {temp} градусов по цельсию.')
        image = 'clear.png' if temp > 5.0 else 'partly_cloudy.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Такого города нет.')


bot.polling(non_stop=True)
