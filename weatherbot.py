import telebot
from weather import getWeather

bot = telebot.TeleBot('1470632926:AAE3gBAO9-J2A86tkxX07XGNcw-AUDNfx0M')

print(getWeather('Chegem'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, getWeather(message.text))


bot.polling()
