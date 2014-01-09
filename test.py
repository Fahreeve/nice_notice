# -*- coding: UTF-8 -*-
import pyvk
import os
import urllib2
import urllib

def save_photos(urls, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    print urls
    names = urls[urls.rfind('/')+ 1:]
    filename = os.path.join(directory, names)
    print "Downloading %s" % filename
    urllib.urlretrieve(urls, filename)
    #open(filename, "w").write(urllib2.urlopen(urls).read())

myvk = pyvk.pyvk("fahreeve@yandex.ru", "flop1996!", "2951857", "messages")
message = myvk.getDialogs(10)
uids = []
print message[1][0]
for mes in message[1]:
    uids += [mes['uid']]
print uids
data_id = myvk.get(uids, ["uid", "first_name", "last_name","online", "photo"])
#print data_id
for data in data_id:
    save_photos(data["photo"], "C:\\Projects\\vk_messenger")
#for i in range(len(data_id)):
    #a = data_id[i]
    #b = message[1][i]
    #print "%d) %d %s %s: %s" % (i + 1, a["online"], a["first_name"], a["last_name"], b['body'])
#number = int(raw_input("enter number a dialog: ")) - 1
#history = myvk.getHistory("user_id", message[1][number]['uid'], 10)[1]
#print history
#for mes in history:
    #print "%d %d\n: %s" % (mes["read_state"], mes["date"], mes["body"])
#mail = raw_input("enter mail: ")
#print myvk.send("user_id", message[1][number]['uid'], mail)

#print myvk.getHistory(, 145605995, 3)
#
#print myvk.getLastActivity(58441774)