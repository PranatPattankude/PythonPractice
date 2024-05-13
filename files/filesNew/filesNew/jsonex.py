
import json


### read json file data

# fvar = open(r'personalinfo.json', 'r')
# myinfo = json.load(fvar)
# fvar.close()

# print(myinfo)
# print(myinfo['ip'], myinfo['dbname'])


#### sample desc

fvar = open(r'studinfo.json','r')
data = json.load(fvar)
fvar.close()

# print(data)

# boysdata = data['Boys']
# print(boysdata['name'])
# for x in boysdata:
#     # print(x['name'])
#     if(x['place'] == "Bangalore"):
#         print(x['name'])
#
# girlsdata = data['Girls']
# for x in girlsdata:
#     if(x['age'] < 25):
#         print(x['name'])
#






### write the dictionary in to json file , create one

# students = {
#     'sharmini' : 'KK',
#     'sirisha' : 'vellore',
#     'ali' : 'bangalore',
#     'shivani' : 'hyderabad'
# }
#
# fvar = open(r'batch159.json', 'w')
# json.dump(students, fvar)
# fvar.close()


#######################

# d1 = {'A':10, 'B':20, 'C':30}
#
# print(d1.keys())
# print(d1.values())
# print(d1.items())
#
# for k,v in d1.items():
#     print(k , "===>", v)






