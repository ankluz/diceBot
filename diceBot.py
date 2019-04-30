import vk_api
import requests
import connect
import logic
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
Cn = sqlite3.connect('Drop.db')
curs = Cn.cursor()
vk_session = vk_api.VkApi(token=connect.token)
vk = vk_session.get_api()

# получение списка администраторов и забаненых из текстовых файлов
admins = []
banlist = []

curs.execute('SELECT Vkid FROM Admins')
row = curs.fetchone()
while row is not None:
    admins.append(row[0])
    row = curs.fetchone()
print("admins")
print(admins)

curs.execute('SELECT Vkid FROM Banlist')
row = curs.fetchone()
while row is not None:
    banlist.append(row[0])
    row = curs.fetchone()
print("banned")
print(banlist)
curs.close()
Cn.close()
# бесконечный цикл в котором происходит постоянное чтение сообщений в беседах
longpoll = VkBotLongPoll(vk_session, connect.id)
i=0
while i == 0:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            temp = event.obj.text
            temp = temp.replace(connect.strdel,'')
            temp = temp.replace(" ","")
            temp = temp.lower()
            if temp[:8]=='diceroll':
                if event.obj.user_id in banlist:
                    vk.messages.send(
                        user_id=event.obj.user_id,
                        peer_id = event.obj.peer_id,
                        random_id=event.obj.random_id,
                        message="вы забанены")
                else:
                    try:
                        n=int(temp[8:])
                    except:
                        n=20
                    vk.messages.send(
                        user_id=event.obj.user_id,
                        peer_id = event.obj.peer_id,
                        random_id=event.obj.random_id,
                        message=logic.roll(n))


            elif temp[:7] == 'diceban':
                if event.obj.user_id in admins:
                    banlist = logic.ban(temp[7:],banlist)
                    print("banned")
                    print(banlist)
                    vk.messages.send(
                        user_id=event.obj.user_id,
                        peer_id = event.obj.peer_id,
                        random_id=event.obj.random_id,
                        message="пользователь забанен")


            elif temp[:8] == 'diceжанр':
                if event.obj.user_id in banlist:
                    vk.messages.send(
                        user_id=event.obj.user_id,
                        peer_id = event.obj.peer_id,
                        random_id=event.obj.random_id,
                        message="вы забанены")
                else:
                    row = logic.style()
                    vk.messages.send(
                        user_id = event.obj.user_id,
                        peer_id = event.obj.peer_id,
                        random_id = event.obj.random_id,
                        message = "Жанр: %s \nОписание: %s" % (row[1],row[2]))
