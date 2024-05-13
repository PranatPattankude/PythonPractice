import json


### read json file data
#
# fvar = open(r'personalinfo.json', 'r')
# myinfo = json.load(fvar)
# fvar.close()
#
# print(myinfo)
#
# ipaddr = myinfo['ip']
# print(ipaddr)
#
# pwd = myinfo['password']
# print(pwd)




### write the dictionary in to json file , create one


students = {
    'sharmini' : 'KK',
    'sirisha' : 'vellore',
    'ali' : 'bangalore',
    'shivani' : 'hyderabad'
}

fvar = open(r'studinfo.json', 'w')
json.dump(students, fvar)
fvar.close()











