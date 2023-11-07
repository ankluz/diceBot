import vk_api
import random


def roll(n):
        m = '%i/%i' % (random.randint(1,n),n)
        return m


def ban(id,list):
    cn = sqlite3.connect(connect.dbn)
    curs = cn.cursor()
    curs.execute("INSERT INTO Banlist (Vkid) VALUES ('%i')" % (id))
    cn.commit()
    list.append(id)
    print("banned\n")
    curs.close()
    cn.close()
    return list

def unban(id,list):
    cn = sqlite3.connect(connect.dbn)
    curs = cn.cursor()
    curs.execute("DELETE FROM Banlist (Vkid) WHERE Vkid='%i'" % (id))
    cn.commit()
    curs.close()
    cn.close()
    list.remove(id)
    return list

def style():
    cn = sqlite3.connect(connect.dbn)
    curs = cn.cursor()
    curs.execute("SELECT * FROM Styles WHERE Id = '%i'" % (random.randint(1,40)))
    row = curs.fetchone()
    curs.close()
    cn.close()
    return row

def chkchr(id):
    cn = sqlite3.connect(connect.dbn)
    curs = cn.cursor()
    curs.execute("SELECT * FROM Users WHERE Vkid='%i'" % id)
    row = curs.fetchone()
    curs.close()
    cn.close()
    if row is not None:
        return 1
    else:
        return 0

def getchr(id):
    cn = sqlite3.connect(connect.dbn)
    curs = cn.cursor()
    curs.execute("SELECT * FROM Users WHERE Vkid ='%i'" % (id))
    row = curs.fetchone()
    curs.close()
    cn.close()
    return row

def sendmsg(vk,event,mess):
    vk.messages.send(
        user_id=event.obj.user_id,
        peer_id = event.obj.peer_id,
        random_id=event.obj.random_id,
        message=mess)

def crtchr(id,name):
    cn = sqlite3.connect(connect.dbn)
    curs = cn.cursor()
    n = random.randint(1,4)
    curs.execute("SELECT * FROM Attrib WHERE id = '%i'" % n)
    row = curs.fetchone()
    attrib = "%s - %s" % (row[1],row[2])
    curs.execute("INSERT INTO Users VALUES ('%i','%s',1,1,1,1,'%s',3,0)" % (id,name,attrib))
    cn.commit()
    curs.close()
    cn.close()
