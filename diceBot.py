import vk_api
import requests
import connect
import logic
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token=connect.token)
vk = vk_session.get_api()

# получение списка администраторов и забаненых из текстовых файлов
admins = []
banlist = []
with open('admins.txt') as f:
    admins = f.read().splitlines()
print("admins")
print(admins)

with open('banlist.txt') as f:
    banlist = f.read().splitlines()
print("banned")
print(banlist)


# бесконечный цикл в котором происходит постоянное чтение сообщений в беседах
longpoll = VkBotLongPoll(vk_session, connect.id)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        temp = event.obj.text
        temp = temp.replace(connect.strdel,'')
        temp = temp.replace(" ","")
        temp = temp.lower()
        if temp[:4]=='roll':
            if event.obj.user_id in banlist:
                vk.messages.send(
                    user_id=event.obj.user_id,
                    peer_id = event.obj.peer_id,
                    random_id=event.obj.random_id,
                    message="вы забанены")
            else:
                try:
                    n=int(temp[4:])
                except:
                    n=20
                vk.messages.send(
                    user_id=event.obj.user_id,
                    peer_id = event.obj.peer_id,
                    random_id=event.obj.random_id,
                    message=logic.roll(n))
        elif temp[:3] == 'ban':
            if event.obj.user_id in admins:
                logic.ban(temp[3:])
                with open('banlist.txt') as f:
                    banlist = f.read().splitlines()
                print("banned")
                print(banlist)
                vk.messages.send(
                    user_id=event.obj.user_id,
                    peer_id = event.obj.peer_id,
                    random_id=event.obj.random_id,
                    message="пользователь забанен")
