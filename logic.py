import vk_api
import random
import configobj
import connect
import sqlite3


def roll(n):
        m = '%i/%i' % (random.randint(1,n),n)
        return m


def ban(id,list):
    cn = sqlite3.connect('Drop.db')
    curs = cn.cursor()
    curs.execute("INSERT INTO Banlist (Vkid) VALUES ('%i')" % (id))
    cn.commit()
    list.append(id)
    print("banned\n")
    curs.close()
    cn.close()
    return list

def unban(id,list):
    cn = sqlite3.connect('Drop.db')
    curs = cn.cursor()
    curs.execute("DELETE FROM Banlist (Vkid) WHERE Vkid='%i'" % (id))
    cn.commit()
    curs.close()
    cn.close()
    list.remove(id)

def style():
    cn = sqlite3.connect('Drop.db')
    curs = cn.cursor()
    curs.execute("SELECT * FROM Styles WHERE Id = '%i'" % (random.randint(1,40)))
    row = curs.fetchone()
    curs.close()
    cn.close()
    return row
