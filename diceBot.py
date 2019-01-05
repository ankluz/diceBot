import vk_api
import requests
import connect
import logic

session = requests.Session()
vk_session = vk_api.VkApi(connect.login, connect.password)

try:
        vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
        print(error_msg)

vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
n = 1
longpoll = VkLongPoll(vk_session)
while n<10:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_chat:
                temp=event.text
                temp = temp.replace(' ', '')
                temp = temp.lower()
                if temp[0:4] == 'roll':
                    try:
                        n=int(temp[4:])
                    except:
                        n=20
                    logic.roll(vk,event,n)
                if temp[0:4] =='flip':
                    logic.flip(vk,event)
                del temp
