import vk_api
import random
import configobj
import connect



def roll(n):
        m = '%i/%i' % (random.randint(1,n),n)
        return m

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

def unban(id):
    f = open("banlist.txt","r")
    temp = f.readlines()
    f.close()
    f = open("banlist.txt", "w")
    for line in temp:
        if line != id + "\n":
            f.write(line)
    f.close()
