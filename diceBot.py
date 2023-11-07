import vk_api
import requests
import connect
import logic
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

Cn = sqlite3.connect(connect.dbn)
curs = Cn.cursor()
vk_session = vk_api.VkApi(token=connect.token)
vk = vk_session.get_api()

# получение списка администраторов и забаненых из текстовых файлов
admins = {}
banlist = []

curs.execute('SELECT * FROM Admins')
row = curs.fetchone()
while row is not None:
    admins[row[0]]=row[1]
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

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        temp = event.obj.text
        temp = temp.replace(connect.strdel,'')
        temp = temp.replace(" ","")
        temp = temp.lower()
        if temp[:8]=='diceroll':
            if event.obj.from_id in banlist:
                logic.sendmsg(vk,event,"вы забанены")
            else:
                try:
                    n=int(temp[8:])
                except:
                    n=20
                logic.sendmsg(vk,event,logic.roll(n))

        elif temp[:7] == 'diceban':
            if event.obj.from_id in admins:
                banlist = logic.ban(temp[7:],banlist)
                print("banned")
                print(banlist)
                logic.sendmsg(vk,event,"пользователь забанен")

        elif temp[:9] == 'diceunban':
            if event.obj.from_id in admins:
                banlist = logic.unban(temp[9:],banlist)
                print("unbanned")
                print(banlist)
                logic.sendmsg(vk,event,"пользователь разбанен")

        elif temp[:8] == 'diceжанр':
            if event.obj.from_id in banlist:
                logic.sendmsg(vk,event,"вы забанены")
            else:
                row = logic.style()
                logic.sendmsg(vk,event,"Жанр: %s \nОписание: %s" % (row[1],row[2]))
        elif temp[:5] == 'diceя':
            if event.obj.from_id in banlist:
                logic.sendmsg(vk,event,"вы забанены")
            elif logic.chkchr(event.obj.from_id)==1:
                row = logic.getchr(event.obj.from_id)
                logic.sendmsg(vk,event,"ИМЯ: %s\n---------\nУровень: %i\nСила: %i\nЛовкость: %i\nИнтелект: %i\nОчки параметров: %i\nАттрибут: %s\n---------" % (row[1],row[2],row[3],row[4],row[5],row[7],row[6]))
            else:
                logic.sendmsg(vk,event,"Персонаж еще не был создан")

        elif temp[:14] == 'diceсоздайменя':
            if logic.chkchr(event.obj.from_id)==1:
                logic.sendmsg(vk,event,"Но вы уже созданы!")
            else:
                logic.crtchr(event.obj.from_id, temp[14:])
                logic.sendmsg(vk,event,"Персонаж создан")
