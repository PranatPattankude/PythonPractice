
#try - except


#############################################################

# print("simple prog with out Exception Handlng")
#
# var = "today we are learning EH in python"
# res = var.index('java')
# print("the position of python = " , res)
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")
#






## example with exception handling

# print("simple prog with out Exception Handlng")
#
# var = "today we are learning EH in python"
#
# try:
#     res = var.index('java')
#
# except Exception as err:
#     print("hey its ok lets ignore this error")
#     res = "Not found"
#     print("error reason  = ", err)
#
#
# print("the position of java = " , res)
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")












# File Example with out EH
#
# print("opening file ")
#
# try:
#     fvar = open(r'sandy.txt' , 'r')
#
# except Exception as err:
#     print("creating the file sandy.txt")
#     fvar = open(r'sandy.txt', 'w')
#
# fvar.close()
#
# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")







#####################################################################

#EH Example with File concept with data inside
#
# print("opening file ")
#
# try:
#     fvar = opn(r'sandy.txt' , 'r')
#
# except Exception as err:
#     print("creating the file sandy.txt")
#     fvar = open(r'sandy.txt', 'w')
#
# fvar.close()
#
# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")



# EH Example with File concept

# print("EH Example with File concept")
#
# try:
#     fvar = open('sandy.txt','r')
#
# except FileNotFoundError as err:
#     print("\n =============== Exception FNFE Block ========= \n")
#     print("Hey boss its ok lets create file ")
#     fvar = open('sandy.txt' , 'w')
#     print("created file successfully")
#     print("\n =============== Exception Block ========= \n")
#
# except NameError as err:
#     print("\n =============== NAME ERR Block ========= \n")
#     print("Hey boss lets correct the name ")
#     fvar = open('sandy.txt' , 'r')
#     print("\n =============== Exception Block ========= \n")
#
#
# fvar.close()
# print("complete")






############################ creating errors ##############################

# assert and raise



### assert statement example to create error
# assert condition , message


# simple example

# mobnum  = str(input("enter the mobile number = "))
# res1 = len(mobnum)
# res2 = mobnum.isdigit()
# # assert condition , message
# assert res1==10 and res2 == True, "hey sarathi give correct number "
# print("Valid Mobile number")
#
# age = str(input("enter the age = "))
# assert  int(age) >= 22 and int(age) <= 35 , "Invaid age"
# print("Valid age")
#
# print("complete")
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")












# flag = 0
# while(True):
#
#     mobnum  = str(input("enter the mobile number = "))
#
#     res1 = len(mobnum)
#     res2 = mobnum.isdigit()
#
#     # assert condition , "error message"
#     try:
#         assert res1==10 and res2 == True, "hey boss please give correct number "
#         flag = 1
#     except AssertionError as err:
#         print("enter the mobile number again = ")
#         mobnum = str(input("enter the mobile number = "))
#
#     if(flag == 1):
#         print("success i am goint to next step")
#         break
#     else:
#         print("again enter te number boss")
#
# print("Valid Mobile number")


#  using raise statement
#
# mobnum  = str(input("enter the mobile number = "))
#
# res1 = len(mobnum)
# res2 = mobnum.isdigit()
#
# # raise category("error msg")
#
# if(res1 != 10 or res2 != True):
#     raise FileNotFoundError("ashwini enter correct data ")
#
# else:
#     print("Valid mobile number")
#
# print("complete")
#
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")











### assert

#
# username = "santhosh"
# password = "Krishna@123"
# otp = 3428
#
# userin = str(input("enter the user name = "))
# assert userin == username , "invalid username"
# print("valid user name proceed next ")
#
# pwdin = str(input("enter the password = "))
# assert pwdin == password , "invalid password"
# print("valid password  proceed next ")
#
# otpin = int(input("enter the otp = "))
# assert otpin == otp , "invalid otp"
# print("valid otp  proceed next ")
#
#
# print("welcome to home page")





### raise
### if(cond):
#### raise Ecategory("msg")

username = "santhosh"
password = "Krishna@123"
otp = 3428
#
# userin = str(input("enter the user name = "))
# if(username != userin):
#     raise KeyError("invalid username")
# print("valid user name proceed next ")
#
#
pwdin = str(input("enter the password = "))
# if(pwdin != password):
#     raise ValueError("invalid password")
# print("valid password  proceed next ")
#
#
otpin = int(input("enter the otp = "))
if(otpin != otp):
    raise ValueError("invalid otp")
print("valid otp  proceed next ")
#
#
#
# print("welcome to home page")
#
#
#
#
#
#
#
#
#





#assert userin == username and pwdin == password and otpin == otp , "Invalid cread try agaian"



# % >= 60
# back logs == 0
# end duration == 4
# interview == cleared

# perc = int(input("enter the perc = "))
# assert perc >= 60 , "Sorry you dont have enough perc"
# print("percentage is validated")
#
# backlogs = int(input("enter the backlogs = "))
# assert backlogs == 0 , "Sorry you have backlogs"
# print("backlogs is validated")
#
# duration = int(input("enter the eng duration = "))
# assert duration == 4 , "Sorry you dont have enough duration for the course"
# print("duration is validated")
#
# interview = str(input("did u clear the interview = "))
# assert interview == 'yes' , "Sorry  dint clear interview"
# print("interview is validated")
#
# print("welcome to the company XYZ")
#
#
#
#
#
















