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

def adminAdd( id, list):
    with open('admins.txt',"a") as f:
        f.write(id+"\n")
    list.append(id)
    print("admin add\n")

def ban(id,list):
    with open('banlist.txt',"a") as f:
        f.write(id+"\n")
    list.append(id)
    print("banned\n")

def unban(id,list):
    f = open("banlist.txt","r")
    temp = f.readlines()
    f.close()
    f = open("banlist.txt", "w")
    for line in temp:
        if line != id + "\n":
            f.write(line)
    f.close()
