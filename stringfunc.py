

var = "python is easy"
# print(type(var))

# print(var)
# print(var[5])
# print(var[-1])

# print(var[0:3])
# print(var[3:6])
# print(var[-4:])
# print(var[:])
print(var[-1])


# + => concatenation

# a = "santhosh"
# b = "bangalore"
#
# res = a + b
# print(res)
#
# res = a + " lives in " + b
# print(res)


# #* - Duplication
# var = "India"
# res = var * 5
# print(res)

#
# res = "$" * 4
# print(res)


#
# for x in range(1,6):
#     print("*" * x)
# a = 5
# while(a):
#     print("*" * a)
#     a -= 1





############################# Functions ###############
#
var = "pYThoN iS eSAy"
#
# res = var.capitalize()
# print("capitalize format = " , res)
#
# res = var.title()
# print("title format = " , res)
#
# res = var.upper()
# print("upper format = " , res)
#
# res = var.lower()
# print("lower format = " , res)

#
# res = var.swapcase()
# print("swapcase format = " , res)




# Ex : 1
#
# var = "there was a Network issue in servers"
# res = "network" in var.lower()
# print(res)






var = "pYThoN iS eSAy"
#
# res = max(var)
# print(res)
#
# res = min(var)
# print(res)



### special func ord() and chr()

# res = ord(' ')
# print(res)

#
# for x in range(65,123):
#     res = chr(x)
#     print(res)





# var = "pYThoN iS eSAy"
# res = len(var)
# print(res)




# Ex : 1 :

# while(True):
#
#     pwd = str(input("enter the pwd = "))
#
#     if(len(pwd) >= 8):
#         print("valid")
#         break
#     else:
#         print("invalid")





# Ex 2: userame pwd validation prog
#
# user = "santhosh"
# pwd = "san@123"
#
# success = 0
#
# for x in range(3):
#     username = str(input("enter the user name = "))
#     password = str(input("enter the  password = "))
#
#     if(username == user and password == pwd):
#         print("welcome to home page ")
#         success = 1
#         break
#     else:
#         print("Wrong cred try again")
#
# if(success == 0):
#     print("account locked")
#





# var = "sss#######santhosh############kumar########"
# print(var)
#
# res = var.lstrip('s')
# print(res)
#
# res = var.rstrip('#')
# print(res)
#
# res = var.strip('#')
# print(res)
# #
# res = var.replace('#', '')
# print(res)

#
# pwd = 'santhosh123\n'
# res = pwd.replace('\n','')
# print(res)


# var = """
# santhosh teaches python
# santhosh name is 2nd in the blogger list
# my parents kept my name as santhosh bcoz i will be happy
# """
#
# res = var.replace('santhosh', 'sandy',2)
# print(res)


# var = "india is 4th largest Economy"
#
# res = var.startswith('india')
# print(res)
#
# res = var.lower().endswith('economy')
# print(res)


# email = "sandy@gmail.com"
# res = email.endswith('@gmail.com')
# print(res)



#######################################

# var = "santhosh#560100#bangalore#9986019197"
# res = var.split('#')
# print(res)
#
# email = "sandy@gmail.com"
# res = email.split('@')
# print(res)


# data = ['a','b','c','d','e']
# res = ' '.join(data)
# print(res)


# var = "hi san hello san bye San"
# res = var.upper().count('SAN')
# print(res)



# var = "today we have python class and python is easy"
# res = var.index('python')
# print(res)
#
# resmes = var[res:res+10]
# print(resmes)



# log = """
# parse 1 Network error: db conn failed
# innstances port is not active
# asjkhasck';lcv;ad
# favfvlkdfvvdfjkvhfvgdsjvh
# hjcashckljadckl;sdkvl;4
# aakcshaslkcjasl;cjas
# """
#
# errpos = log.index('error')
# print(errpos)
#
# errmsg = log[errpos:errpos+55]
# print(errmsg)



# # validation func


# var = "Santhosh KUMAR"
# res = var.isalpha()
# print(res)
#
# var = " 9986019197"
# res = var.isdigit()
# print(res)
#
# var = 'san123sandy@'
# res = var.isalnum()
# print(res)
#
#
# var = "SANTHOSH LIKES WHEN THERE IS  A CONFIDENCE 9171819171919"
# res = var.isupper()
# print(res)
#
# res = var.islower()




#
var = "sandy@13141415^^&**(("

# import re
# spchar = re.findall('[0-9]', var)
# print(spchar)
#

































