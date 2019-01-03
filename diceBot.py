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
        if event.text == 'Roll':
            vk.messages.send(
                chat_id=event.chat_id,
                random_id=event.random_id,
                message=random.randint(1,20))
