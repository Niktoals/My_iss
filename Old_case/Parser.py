import random
import requests
import telebot
from bs4 import BeautifulSoup as b
from telebot import types

URL1 = 'https://www.anekdot.ru/last/good/'
API_KEY='5505410546:AAHxnzeBdA3BT4UrCKaSYHxGyvfg7vS9EIg'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]
list_of_jokes = parser(URL1)
random.shuffle(list_of_jokes)

bot=telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def hello(group_name, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn=types.KeyboardButton('Анекдот')
    markup.add(btn)
    bot.send_group_name(group_name.chat.id, 'Привет. Чтобы поржать введи любую цифру. Если не хочешь писать цифры нажми кнопку', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def jokes(group_name):
    if group_name.text.lower() in '123456789'or group_name.text.strip() == 'Анекдот':
        bot.send_group_name(group_name.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_group_name(group_name.chat.id, 'Введите любую цифру.')

bot.polling(non_stop=True, interval=0)