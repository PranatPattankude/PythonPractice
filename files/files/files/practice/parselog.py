# # below block will read the data in list format
# fvar = open(r'log.txt', 'r')
# data = fvar.readlines()
# fvar.close()
# # print(data)
#
# ips = []
#
# for x in data:
#     if('error' in x.lower()):
#         temp = x.split(':')
#         if(len(temp) == 3):
#             ipaddr = temp[-1]
#             print("Ip address = ", ipaddr)
#             ips.append(ipaddr)
#
#
# print(ips)


# import re
#
# fvar = open(r'log.txt', 'r')
# data = fvar.read()
# fvar.close()
#
# ip = re.findall('[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}',data)
# print(ip)


#########################################################

# reding data from json file

# import json
#
# fjson = open(r'personalinfo.json', 'r')
# jdata = json.load(fjson)
# fjson.close()
#
# # print(jdata)
#
# girlsinfo = jdata['Girls']
# boysinfo = jdata['Boys']
#
# girlscount = 0
# boyscount = 0
#
# for x in girlsinfo:
#     if(x['age'] >= 25 and x['place'] == "Bangalore"):
#         print(x['name'])
#
#     if(x['place'] == "Bangalore"):
#         girlscount += 1
#
#
# for x in boysinfo:
#     if(x['age'] >= 25 and x['place'] == "Mumbai"):
#         print(x['name'])
#
#     if(x['place'] == "Bangalore"):
#         boyscount += 1
#
#
#
# print("Total girls from bangalore = ", girlscount)
# print("Total boys from bangalore = ", boyscount)













