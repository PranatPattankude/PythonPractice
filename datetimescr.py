import math
# from datetime import date, datetime
# import time

# # get today's date
# mydate = date.today()
# print(mydate)
#
# print("Current year:", mydate.year)
# print("Current month:", mydate.strftime("%b"))
# print("Current month:", mydate.month)
# print("Current day:", mydate.day)
#
# dateformat = str(mydate.day) + ":" + str(mydate.month) + ":" + str(mydate.year)
# print(dateformat)


# #
# current_datetime = datetime.now()
# print(current_datetime)
#
# # time.sleep(10)
# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)


##### all() any() funcs

#
# a = 10
# b = 20
# c = 30

# res1 = a<10
# res2 = b == 20
# res3 = c < 25
#
# if(res1 == True and res2 == True and res3 == True):
#     print("yes")
# else:
#     print("no")


# USING all() and any()


# a = 10
# b = 20
# c = 30
#
# res =[a<10, b==20 , c<25]
# print(res)
#
# op = any(res)
# print(op)
#
# op = all(res)
# print(op)

# Example for any and all

# username = str(input("enter the usrname = "))
# passwd = str(input("enter the password = "))
# otp = str(input("enter the otp = "))
#
# res = [username=="santhosh",passwd=="San@123",otp=='1234']
# print(res)
#
# op = all(res)
# print(op)


# res =[a==10, b==25 , c>25]
# op = all(res)
# print(op)


### Lambda ###########

#
# def test(x,y):
#     res = x + y
#     return res
#
# res = test(50,40)
# print(res)


# # # variable = lambda parameters : return result
#
# var = lambda x,y : x+y
# op = var(20,5)
# print(op)

# op = lambda x,y : x+y
# res = op(8,10)
# print(res)

# var = lambda x : x + 10
# op = var(50)
# print(op)


#
# def test(a,b):
#     res = a * b
#     return res
#
# op = test(10,30)
# print(op)
#
#
# # # # # variable = lambda parameters : return result
#
# var = lambda a,b : a * b
# op = var(7,3)
# print(op)


# def sample(x):
#     res = x.replace(' ','').upper()
#     return res
#
# op = sample("     dev              talwar   ")
# print(op)


# # # # # variable = lambda parameters : return result

# var = lambda x : x.replace(' ','').upper()
# res = var("          sachin       tendulkar       ")
# print(res)


### map() , reduce() , filter()

# map() : use for  functions of list or tuple
# it will evaluate the func for all elemenst of list or tuple

# import math
# def sqrt(x):
#     return math.sqrt(x)
#
# def powerOfTen(x):
#     return 10**x
#
# nums = [2,4,6,8]
# res = map(sqrt,nums)
# for x in res:
#     print(x)

# op = map(powerOfTen, nums)
#
# for x in op:
#     print(x)


# def convertdata(x):
#     return x.lower()
#
#
# fname = ['Santhosh','RAVI', 'AjIt', 'KrIShna']
#
# op = map(convertdata,fname)
# for x in op:
#     print(x)
#
#
#


# filter()
# Note here the return should be true or false only
# it returns which all cond was true
#
# def stud(x):
#     if(x < 35):
#         return True
#     else:
#         return False
#
# perc = [77,56,32,90,52,21]
# op = filter(stud,perc)
# print(op)
#
# for x in op:
#     print(x)
#


# reduce()

# from functools import reduce
# def addp(a, b):
#     return a + b
#
#
# num = [10, 17, 34, 42, 12]
# z = reduce(addp, num)
# print(z)

# def addn(x,y):
# return x - y
#
# nums = [10,20,30,40,50]
# op = reduce(addn, nums)
# print(op)
#
# def addn(x,y):
#     return x + y
#
# marks = [89,56,65,90,78]
# op = reduce(addn, marks)
# print(op)


# op = reduce(lambda a,b:a*b, [10,20,30,40,50])
# print(op)


############ Hkcker Rank###########
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# coordinates = []
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 coordinates.append([i, j, k])
#
#
# print(coordinates)

# from functools import reduce



