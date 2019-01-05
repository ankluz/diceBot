import vk_api
import random

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
