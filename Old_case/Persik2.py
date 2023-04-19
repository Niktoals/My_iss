import telebot
import os
from telebot import types
import random
API_KEY='5505410546:AAHxnzeBdA3BT4UrCKaSYHxGyvfg7vS9EIg'
bot=telebot.TeleBot(API_KEY)    

def send_info_prof(message):
    info=''
    with open(f'АРХИВ/Архив {user}/text.txt') as file:
        for i in file:
            info=info + i
    with open(f'АРХИВ/Архив {user}/user_name.txt') as username:
        for i in username:
            info=info + i
    photo = open(f'АРХИВ/Архив {user}/photo.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=info )


def info_text(message):
    info_profile=['Пол', 'Имя', 'Возраст', 'Кого ищешь', 'Что-то о себе']
    ls=[]
    message=message.split('\n')
    for i in message:
        i=i+'\n'
        ls.append(i)
    inf=''
    lengh=len(info_profile)
    for i in range(lengh):
        inf+=info_profile[i]+': ' + ls[i]
    with open(f'АРХИВ/Архив {user}/text.txt', 'w') as file:
        file.write(str(inf))
    with open(f'АРХИВ/Архив {user}/user_name.txt', 'w') as file_name:
        file_name.write('@'+str(user_name))

def handle_docs_photo(message):
        try:
            file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(f'АРХИВ/Архив {user}/photo.jpg', 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message,"Фото добавлено") 
        except Exception as e:
            bot.reply_to(message,e )

def main():
    @bot.message_handler(commands=['start'])
    def hello(message):
        global list_of_search_edited
        bot.send_message(message.chat.id, 'Привет, я бот знакомств и хотелось бы скарасить твою жизнь.\nНу что начнем?/yea')
        with open(f'АРХИВ\id_of_users') as Arxiv:
            list_of_search_test=",".join(Arxiv)
            list_of_search_edited=list_of_search_test.split(',')
    @bot.message_handler(commands=['yea'])
    def access(message):
        global user
        user=message.from_user.id
        if not os.path.exists(f'АРХИВ/Архив {user}'):
            os.mkdir(f'АРХИВ/Архив {user}')
            bot.send_message(message.chat.id, 'Напиши о себе.\nПол\nИмя\nВозраст\nКого ищешь(Парня, Девушку)\nЧто-то о себя')
        else:
            bot.send_message(message.chat.id, 'Вы уже создавали анкету')
            send_info_prof(message)
    @bot.message_handler(commands=['go'])
    def searching(message):
        if len(list_of_search_edited)==0:
            bot.send_message(message.chat.id, 'Больше постов нет')
        info=''
        if list_of_search_edited[0][0]==' ':
            list_of_search_edited[0]=list_of_search_edited[0][1::]
        with open(f'АРХИВ/Архив {list_of_search_edited[0]}/text.txt') as filee:
            for i in filee:
                info=info + i
        photo = open(f'АРХИВ/Архив {list_of_search_edited[0]}/photo.jpg', 'rb')
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_like=types.KeyboardButton('Нравится')
        btn_next=types.KeyboardButton('Дальше')
        markup.add(btn_like)
        markup.add(btn_next)
        bot.send_photo(message.chat.id, photo, caption=info, reply_markup=markup)
        del list_of_search_edited[0]
        
    @bot.message_handler(content_types=['text'])
    def inf(message):
        global user_name
        answer=message.text
        user_name=message.from_user.username
        info_text(str(answer))
        bot.send_message(message.chat.id, 'Отправь свое фото')
        
    @bot.message_handler(content_types=['photo'])
    def photo(message):
        handle_docs_photo(message)
        bot.send_message(message.chat.id, 'Это твоя анкета')
        send_info_prof(message)
    
    bot.polling()

if __name__=="__main__":
    main()