import vk_api
import requests
import random
import connect

session = requests.Session()
vk_session = vk_api.VkApi(connect.login, connect.password)

try:
        vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
        print(error_msg)

vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_chat:
            temp=event.text
            temp = temp.replace(' ', '')
            temp = temp.lower()
            if temp[0:4] == 'roll':
                try:
                    n=int(temp[4:])
                    temp = '%i/%i' % (random.randint(1,n),n)
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=event.random_id,
                        message=temp)
                except:
                    temp = '%i/20' % (random.randint(1,20))
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=event.random_id,
                        message=temp)
            del temp
