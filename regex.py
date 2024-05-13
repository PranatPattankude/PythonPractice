import re

# var = "my mobile nums are 7411694426 and 9986019197abcd"
#
# temp = var.split(' ')
# print(temp)
#
# for x in temp:
#     if(len(x) == 10 and x.isdigit()):
#         print(x)




import re

var = "today python is easy to learn i love python and python rocks"

# res = re.match('today', var)
# print(res)
#
# res = re.search('python', var)
# print(res)

# res = re.findall('python', var)
# print(res)


var = "today python is easy to learn i love python and PYthon rocks PYThoN"

# res = re.findall('python',var, re.I)
# res = re.sub('python' , 'java' , var.lower())
# print(res)




# regex examples

# var = "my mobile nums are 7411694426 and 9986019197abcd and 9986019193"
# pat = '[0-9]{10}'
# res = re.findall(pat, var)
# print(res)







#

# var = "my fav dest places are SINGAPORE and MALDIVES and LOSVEGAS and BALI"
# pat = '[A-Z]{2,}'
# res = re.findall(pat,var)
# print(res)




# var = """
# India ip address is 192.3.4.67
# Australia ip address is 23.123.5.4
# Canada ip address is 165.211.90.43 and 1.45.78
# """
#
# patc = '[A-Z][a-z]{1,}'
# pati = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
#
# countries = re.findall(patc, var)
# ips = re.findall(pati,var)
#
# print(countries)
# print(ips)










var = """
16.09.2000 and email is chethanasonami16092000@gmail.com
26/11/1994 and email is dipalioj26@reddiff123.com
26-04-2000 and email is JayaShreebharathi10@yahoo.com
"""

# patd = '[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}'
# pate = '[A-Za-z0-9]{1,}[@][A-Za-z0-9]{1,}[.]com'
#
# dates = re.findall(patd,var)
# emails = re.findall(pate, var)
#
# print(dates)
# print(emails)



# file example to format uneven spaces
import re

# fvar = open(r'D:\SANTHOSH\Batches\Batch138-8am\files\data.txt', 'r')
# info = fvar.read()
# fvar.close()
#
# print(info)
#
# res = re.sub('[ ]{1,}', ' ', info)
#
# fvar = open(r'D:\SANTHOSH\Batches\Batch138-8am\files\data.txt', 'w')
# fvar.write(res)
# fvar.close()




# password Validation function

# pwd = str(input("enter the password = "))
#
# caps = len(re.findall('[A-Z]', pwd))
# lows = len(re.findall('[a-z]', pwd))
# digs = len(re.findall('[0-9]', pwd))
# spec = len(re.findall('[^A-Za-z0-9]', pwd))
# pwdlen = len(pwd)
#
# if(caps > 0 and lows > 0 and digs > 0 and spec > 0 and pwdlen >= 8):
#     print("Valid Password")
# else:
#     print("Invalid password")




# print(caps)
# print(lows)
# print(digs)
# print(spec)
# print(pwdlen)


#
# var = """
# hello  $$$$ %%%% * ( )))           all            how
# are you        $$$$ %%%% * ( )))         hope
# all are   $$$$ %%%% * ( )))      revising            python
# """
#
# res = re.sub('[ ]{1,}', ' ', var)
# print(res)
# #
# patsp = '[ ]'
#
# patsp = '[ ]{1,}'
# patc = '[^A-Za-z0-9]' + '|' +  patsp
# op = re.sub(patc, ' ', res)
# print(op)

#
#
#
