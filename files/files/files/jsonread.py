import json

# fvar = open(r'saninfo.json', 'r')
# myinfo = json.load(fvar)
# print(myinfo['doornum'])


# fvar = open(r'personalinfo.json', 'r')
# jdata = json.load(fvar)
# fvar.close()
#
# print(jdata)
#
# ipadd = jdata['IP']
# print(ipadd)
#
# user = jdata['username']
# print(user)


# Create JSON File

myinfo = [
    {
        "name": "arun",
        "place": "bangalore",
        "pincode": "560078",
        "dob": "Nov 22",
        "doornum": "02",
        "area": "JP Nagar"
    },
    {
        "name": "ramya",
        "place": "dharmapuri",
        "pincode": "6368",
        "dob": "Aug 13",
        "doornum": "178",
        "area": "palacode"
    }
]

# fvar = open(r'students.json', 'w')
# json.dump(myinfo, fvar)
# fvar.close()


fvar = open(r'students.json', 'a')
json.extend(myinfo, fvar)
fvar.close()