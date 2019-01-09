import vk_api
import random
import configobj
import connect



def roll(vk,event, n=20):
    temp = '%i/%i' % (random.randint(1,n),n)
    vk.messages.send(
        chat_id=event.chat_id,
        random_id=event.random_id,
        message=temp)

def flip(vk,event):
    if random.randint(1,2) == 1:
        vk.messages.send(
            chat_id=event.chat_id,
            random_id=event.random_id,
            message='Орел!')
    else:
        vk.messages.send(
            chat_id=event.chat_id,
            random_id=event.random_id,
            message='Решка!')

def adminAdd(vk,event, id, list):
    f = open('admins.txt',"a")
    f.write(id+"\n")
    f.close()
    list.append(id)
    print("admin add\n")
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message='администратор добавлен')

def ban(vk,event,id,list):
    f = open('banlist.txt',"a")
    f.write(id+"\n")
    f.close()
    list.append(id)
    print("banned\n")
    vk.messages.send(
        user_id=event.user_id,
        random_id=event.random_id,
        message='пользователь забанен')
