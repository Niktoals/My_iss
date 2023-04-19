import json
import os
import emoji
import requests
import telebot
import youtube_dl
from bs4 import BeautifulSoup as b
from string import digits


API_KEY='5505410546:AAHxnzeBdA3BT4UrCKaSYHxGyvfg7vS9EIg'
token = 'vk1.a.lQww5JnTWu8W4pXUv3pl9DsBQOX9S3CKkkuXmUNLOpppIeBmIxdd_QNBDyS2FC8-ev4HajSQcvhpDMA7-A_CaLj35ugDowucvTdz9yte-e_LvCN1_g0wrcXMrRqfwXBJc9Zpyc6BjbDhU-EJ6Tj4NFgiZPlLCchY8b84y-EPRLURGAeeqJyj4K0IIfXAL8aop'
def get_wall_posts(group_name, message, count):

    url= f"https://api.vk.com/method/wall.get?domain={group_name}&count={count}&access_token={token}&v=5.131"
    req=requests.get(url)
    src=req.json()
    fresh_posts_id=[]
    posts=src["response"]["items"]
    #проверям существование директории с именем группы
    if os.path.exists(f'{group_name }'):
        print(f'Директория с именем {group_name} уже существует')
    else:
        os.mkdir(group_name)
        with open(f'{group_name }/{group_name }.json', 'w', encoding='utf-8') as file:
            json.dump(src, file, indent=4, ensure_ascii=False)
            for fresh_post_id in posts:
                fresh_post_id=fresh_post_id['id']
                fresh_posts_id.append(fresh_post_id)
    print(fresh_posts_id)

    if not os.path.exists(f'{group_name}/grop_posts'):
        os.mkdir(f'{group_name}/grop_posts')
    #собираем ID новых постов в список


    """Проверка, если файла не существует,
    значит это первый парсинг группы(отправляем все новые посты).
    Иначе начинаем проверку и отправляем только новые"""
    if not os.path.exists(f'{group_name }/exist_posts_{group_name }.txt'):
        print('Файла с ID посто не существуетб создаем файл!')
        with open(f'{group_name }/exist_posts_{group_name }.txt', 'w') as file:
            for item in fresh_posts_id:
                file.write(str(item) + '\n')
        for post in posts:
            #Функция для сохранения изображений по ссылке
            def download_img(url, post_id, group_name):
                res=requests.get(url)
                if not os.path.exists(f'{group_name}/grop_posts/{post_id}'):
                    os.mkdir(f'{group_name}/grop_posts/{post_id}')
                    with open(f'{group_name}/grop_posts/{post_id}/{post_id}.jpg', 'wb') as img:
                        img.write(res.content)
                else:
                    x='_'
                    c=0
                    with open(f'{group_name}/grop_posts/{post_id}/{str(post_id)+x+str(c)}.jpg', 'wb') as img:
                        img.write(res.content)


            #Функция для сохранения видео по ссылке
            def download_video(url, post_id, group_name):
                global ydl
                try:
                    if not os.path.exists(f'{group_name}/grop_posts/{post_id}'):
                        os.mkdir(f'{group_name}/grop_posts/{post_id}')
                        ydl_opts= {"outtmpl" : f'{group_name}/grop_posts/{post_id}/{post_id}'}
                        with  youtube_dl.YoutubeDL(ydl_opts)as ydl:
                            ydl.download([url])
                    else:
                        x='_'
                        c=0
                        ydl_opts= {"outtmpl" : f'{group_name}/grop_posts/{post_id}/{str(post_id)+x+str(c)}'}
                        with youtube_dl.YoutubeDL(ydl_opts)as ydl:
                            ydl.download([url])              
                except Exception:
                    print('Не удалось скачать видео')

            post_id= post['id']
            print(f'отправляем пост с ID {post_id}')
            print(post['text'])
            if post['text']!='':
                post_id_text=post_id
                bot.send_message(message.chat.id, 'Пост номер: ' + str(post_id_text))
                bot.send_message(message.chat.id, post['text'])
            post_id_count=0
            try:
                if 'attachments' in post:
                    post=post['attachments']
                    #Проверка на фото/или видео
                    if post[0]['type']=='photo':
                        for post_item_photo in post:
                            post_id_photo=post_id
                            post_photo = post_item_photo["photo"]["sizes"][-1]["url"]
                            download_img(post_photo, post_id, group_name)
                            print(post_photo)
                            if post_id_text==post_id_photo:
                                bot.send_photo(message.chat.id, post_photo)
                            else:
                                bot.send_message(message.chat.id, 'Пост номер: ' + str(post_id_photo))
                                bot.send_photo(message.chat.id, post_photo)
                            post_id_count+=1
                    elif post[0]['type']=='video':
                        post_id_video=post_id
                        print('Видео пост')
                        video_access_key=post[0]["video"]["access_key"]
                        video_post_id=post[0]["video"]["id"]
                        video_owner_id=post[0]["video"]["owner_id"]
                        video_get_url=f'https://api.vk.com/method/video.get?videos={video_owner_id}_{video_post_id}_{video_access_key}&access_token={token}&v=5.131'
                        req=requests.get(video_get_url)
                        res=req.json()
                        video_url=res["response"]["items"][0]["player"]
                        download_video(video_url, post_id, group_name)
                        print(video_url)
                        if post_id_text==post_id_video:
                            video = open(f'C:/Users/User/программы/pozor/grop_posts/{post_id}/{post_id}', 'rb')
                            bot.send_video(message.chat.id, video, timeout=10)
                        else:
                            bot.send_message(message.chat.id, 'Пост номер: ' + str(post_id_photo))
                            video = open(f'C:/Users/User/программы/pozor/grop_posts/{post_id}/{post_id}', 'rb')
                            bot.send_video(message.chat.id, video, timeout=10)

            except Exception:
                print(f'что-то пошло не так с постом ID {post_id}!')
    else:
        def download_img(url, post_id, group_name):
                res=requests.get(url)
                if not os.path.exists(f'{group_name}/grop_posts/{post_id}'):
                    os.mkdir(f'{group_name}/grop_posts/{post_id}')
                    with open(f'{group_name}/grop_posts/{post_id}/{post_id}.jpg', 'wb') as img:
                        img.write(res.content)
                else:
                    x='_'
                    c=0
                    with open(f'{group_name}/grop_posts/{post_id}/{str(post_id)+x+str(c)}.jpg', 'wb') as img:
                        img.write(res.content)
        
        def download_video(url, post_id, group_name):
                global ydl
                try:
                    if not os.path.exists(f'{group_name}/grop_posts/{post_id}'):
                        os.mkdir(f'{group_name}/grop_posts/{post_id}')
                        ydl_opts= {"outtmpl" : f'{group_name}/grop_posts/{post_id}/{post_id}'}
                        with  youtube_dl.YoutubeDL(ydl_opts)as ydl:
                            ydl.download([url])
                    else:
                        x='_'
                        c=0
                        ydl_opts= {"outtmpl" : f'{group_name}/grop_posts/{post_id}/{str(post_id)+x+str(c)}'}
                        with youtube_dl.YoutubeDL(ydl_opts)as ydl:
                            ydl.download([url])              
                except Exception:
                    print('Не удалось скачать видео')
        print('Файл с ID постов существует, начинаем выборку свежих постов!')
        fresh_posts_id_old=[]
        with open(f'{group_name }/exist_posts_{group_name }.txt') as file:
            for item in file:
                fresh_posts_id_old.append(int(item[:-1:]))
        posts=src["response"]["items"]
        fresh_posts_id_new=[]
        for fresh_post_id_new in posts:
            fresh_post_id_new=fresh_post_id_new['id']
            fresh_posts_id_new.append(fresh_post_id_new)
        print(fresh_posts_id_new)
        print(fresh_posts_id_old)
        result_ans=[]
        result = list(set(fresh_posts_id_new) ^ set(fresh_posts_id_old))
        for i in fresh_posts_id_new:
            for j in result:
                if j==i:
                    result_ans.append(j)
        
        print(result_ans)
        with open(f'{group_name }/exist_posts_{group_name }.txt', 'a') as file:
            for item in result_ans:
                file.write(str(item) + '\n')
        if len(result_ans)!=0:
            for post in posts:
                post_id= post['id']
                for id in result_ans:
                    if post_id==id:
                        print(f'отправляем пост с ID {post_id}')
                        print(post['text'])
                        if post['text']!='':
                            post_id_text=post_id
                            bot.send_message(message.chat.id, 'Пост номер: ' + str(post_id_text))

                        post_id_count=0
                        try:
                            if 'attachments' in post:
                                post=post['attachments']
                                #Проверка на фото/или видео
                                if post[0]['type']=='photo':
                                    for post_item_photo in post:
                                        post_id_photo=post_id
                                        post_photo = post_item_photo["photo"]["sizes"][-1]["url"]
                                        print(post_photo, post_id, group_name)
                                        download_img(post_photo, post_id, group_name)
                                        if post_id_text==post_id_photo:
                                            bot.send_photo(message.chat.id, post_photo, caption=post['text'])
                                        else:
                                            bot.send_message(message.chat.id, 'Пост номер: ' + str(post_id_photo))
                                            bot.send_photo(message.chat.id, post_photo, caption=post['text'])
                                        
                                        post_id_count+=1
                                elif post[0]['type']=='video':
                                    post_id_video=post_id
                                    print('Видео пост')
                                    video_access_key=post[0]["video"]["access_key"]
                                    video_post_id=post[0]["video"]["id"]
                                    video_owner_id=post[0]["video"]["owner_id"]
                                    video_get_url=f'https://api.vk.com/method/video.get?videos={video_owner_id}_{video_post_id}_{video_access_key}&access_token={token}&v=5.131'
                                    req=requests.get(video_get_url)
                                    res=req.json()
                                    video_url=res["response"]["items"][0]["player"]
                                    download_video(video_url, post_id, group_name)
                                    print(video_url)
                                    if post_id_text==post_id_video:
                                        video = open(f'C:/Users/User/программы/pozor/grop_posts/{post_id}/{post_id}', 'rb')
                                        bot.send_video(message.chat.id, video, timeout=10, caption=post['text'])
                                    else:
                                        bot.send_message(message.chat.id, 'Пост номер: ' + str(post_id_photo))
                                        video = open(f'C:/Users/User/программы/pozor/grop_posts/{post_id}/{post_id}', 'rb')
                                        bot.send_video(message.chat.id, video, timeout=10, caption=post['text'])
                                    del result_ans[0]
                        except Exception:
                            print(f'что-то пошло не так с постом ID {post_id}!')
                            bot.send_message(message.chat.id, 'что-то пошло не так с постом ID {post_id}!')
                    else:
                        if len(result_ans)==0:
                            bot.send_message(message.chat.id, 'Посты закончились!')
                        else:
                            continue
        else:
            bot.send_message(message.chat.id, 'Пока что новых постов нет(')

bot=telebot.TeleBot(API_KEY)   

def main():
    @bot.message_handler(commands=['start'])
    def hello(message):
        bot.send_message(message.chat.id, 'Привет.\nЯ могу собрать инфу о паблике в вк для этого напиши "/go"')
    @bot.message_handler(commands=['go'])
    def info(message):
        bot.send_message(message.chat.id, 'А теперь пожалуйста кинь полную ссылку на паблик')
    @bot.message_handler(content_types=['text'])
    def answer(message):
        global group_name
        name=message.text
        if name.lower()=='я тебя люблю':
            for word in range(100):
                bot.send_message(message.chat.id, emoji.emojize('я тебя  тоже очень люблю :red_heart:', variant="emoji_type"))
        elif name[:5:]=='https':
            index=name.rfind('/')
            group_name=name[index+1::]
            print(group_name)
            bot.send_message(message.chat.id, 'Перед тем как отправить тебе посты, напиши сколько тебе отправить')
        elif name[0] in digits:
            count=message.text
            print(count)
            get_wall_posts(str(group_name), message, str(count))
        else:
            bot.send_message(message.chat.id, 'Проверь что ты отправил, и отправь еще раз верное')
    bot.polling()



if __name__=="__main__":
    main()
