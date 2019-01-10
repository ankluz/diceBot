import vk_api
import requests
import connect
import logic


session = requests.Session()
vk_session = vk_api.VkApi(connect.login, connect.password)

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

# аутентификация бота в VK.com
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

#установка параметров для longpoll
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
n = 1
longpoll = VkLongPoll(vk_session)

# бесконечный цикл в котором происходит постоянное чтение сообщений в беседах
while n<10:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            #обработка сообщений из бесед

            if event.from_chat:
                temp = event.text
                temp = temp.lower().replace(' ','')
                if temp[0:4] == 'roll':
                    if str(event.user_id) in banlist:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=event.random_id,
                            message='вы забанены')
                    else:
                        try:
                            n=int(temp[4:])
                        except:
                            n=20
                        logic.roll(vk,event,n)
                elif temp[0:4] =='flip':
                    if str(event.user_id) in banlist:
                        vk.messages.send(
                            chat_id=event.chat_id,
                            random_id=event.random_id,
                            message='вы забанены')
                    else:
                        logic.flip(vk,event)

            #обработка личных сообщений
            elif event.from_user:
                if event.to_me:
                    print("user with id %s writed %s \n" % (event.user_id, event.text))
                    temp = event.text
                    temp = temp.lower().replace(' ','')
                    if temp[:8] == "adminadd":
                        if str(event.user_id) in admins:
                            if temp[8:] in banlist:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=event.random_id,
                                    message='пользователь забанен, никакого толку нет от того что вы его добавите в админы')
                            else:
                                print("try to add admin \n")
                                try:
                                    logic.adminAdd(vk,event,temp[8:],admins)
                                    print(admins)
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=event.random_id,
                                        message='администратор добавлен')
                                except:
                                    print("error \n")
                                    vk.messages.send(
                                        user_id=event.user_id,
                                        random_id=event.random_id,
                                        message='Админ не добавлен, возникла ошибка')
                        else:
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=event.random_id,
                                message='вас нет в списке админов')
                            print("dont have permissions\n")
                    elif temp[:3] == "ban":
                        if str(event.user_id) in admins:
                            if temp[3:] in admins:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=event.random_id,
                                    message='пользователь в списке администраторов, вы же не хотите чтобы началась великая война админов?')
                            else:
                                print("try to ban %s" % (temp[3:]))
                                logic.ban(temp[3:],banlist)
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=event.random_id,
                                    message='пользователь забанен')

                    elif temp[:5] =="unban":
                        if str(event.user_id) in admins:
                            print("try to unban %s" % (temp[5:]))
                            logic.unban(temp[5:],banlist)
                            with open("banlist.txt") as f:
                                banlist = f.readlines()
                            print(banlist)
                            vk.messages.send(
                                user_id=event.user_id,
                                random_id=event.random_id,
                                message='пользователь разбанен')
