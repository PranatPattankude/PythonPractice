
# practicepython.org

######   User name pwd validation prog ############


# usr = "santhosh"
# pwd = "San@123"
# flag = 0
#
#
# for x in range(3):
#
#     username = str(input("enter the user name = "))
#     password  = str(input("enter the password = "))
#
#     if(username == usr and password == pwd):
#         print("welcome to home page")
#         flag = 1
#         break
#
#     else:
#         print("wrong cred try again")
#
#
# if(flag == 0):
#     print("account is locked as u exceeded the attempts")




# a = 1
# while(a <= 3):
#     print("sandy")
#     a = a + 1






####  snake and ladder prog

# import random
#
# pos = 0
# attempt = 0
#
# while(pos < 100):
#
#     dice = random.randrange(1,7)
#     pos = pos + dice
#     attempt += 1
#
#     print("====> ", pos)
#
#     if(pos == 100):
#         print("Game over ")
#         break
#
#     if(pos > 100):
#         pos = pos - dice
#
#
#     if(pos == 7):
#         pos = 78
#         print("ladder at 7")
#
#     if(pos == 12):
#         pos = 97
#         print("ladder at 12")
#
#     if(pos == 45):
#         pos = 79
#         print("ladder at 45")
#
#
#     if(pos == 56):
#         pos = 8
#         print("snake at 56")
#
#     if(pos == 92):
#         pos = 17
#         print("snake at 92")
#
#     if(pos == 70):
#         pos = 13
#         print("snake at 70")
#
#
#
#
# print("total attempts taken to complete game = ", attempt)


# fibbonaci serier

# 0 1 1 2 3 5 8 13 21 34 ........

# first = 0
# second = 1
#
# print(first , end = " ")
# print(second, end = " ")
#
# for x in range(10):
#     temp = first + second
#     print(temp, end = " ")
#     first = second
#     second = temp
#





























