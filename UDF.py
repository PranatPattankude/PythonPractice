# Creating sample function

# def test(x,y,z):
#     res1 = x + y + z
#     return res1
#
# op = test(10,10,80)
# print(op)
#
# op = test(3,2,1)
# print(op)
#
# op = test(7,2,1)
# print(op)


### Sample use of function


# def mobval(num):
#     res1 = len(num)
#     res2 = num.isdigit()
#     if(res1 == 10 and res2 == True):
#         return "Valid Number"
#     else:
#         return "invalid number"

# op = mobval("176171")
# print(op)
#
# op = mobval("616116")
# print(op)
#
# op = mobval("9986019197")
# print(op)
#
# op = mobval('74116dsdgwkdg')
# print(op)


# =======================================================


# local and global variable concept

# any variable created inside the function is Local Variable
# any variable created outside the function is global Variable

# place = "bangalore"
#
# def test(x,y,z):
#     global name
#     name = "santhosh"
#     print("inside = ", place)
#     res = x + y + z
#     return res
#
# op = test(30,10,5)
# print(op)
#
# print("outside = ", name)


# Explaining multiple return statements

# def test(x,y,z):
#     res1 = x + y + z
#     res2 = x - y - z
#     res3 = x * y * z
#     return res1,res2,res3
#
# op = test(20,10,5)
# print(op)


# types of UDF

# 1. required and positional arg

# def test(x,y,z):
#     res = x + y + z
#     return res
#
# op = test(20,10,5)
# print(op)


# 2. required and non positional keyword  arg

# def test(x,y,z):
#     res = x + y + z
#     return res
#
# op = test(y = 50,z = 10, x = 40)
# print(op)


# 3. default arg func

# def test(x=300,y=1000,z=500):
#     res = x + y + z
#     return res
#
# op = test()
# print(op)


# # # 4. variable length arg func
# Var leng arg shld always be at last

# def test(*z):
#     # print(x)
#     # print(y)
#     print(z)
#
# test(10,20,30,40,50,60,70)


#
# def test(**kwargs):
#     print(kwargs)
#
# test(name='sandy', age=20,place='blr')


#
#
#
#
#
#
#
#
# res1 = 99
#
# def test(x,y,z):
#     global res1,res2,res3
#     res1 = x + y + z
#     res2 = x - y - z
#     res3 = x * y * z
#     return res1,res2,res3
#
# op = test(20,10,5)
# print(op)
#
#
# print("res1 = " , res1)


palindrome = lambda s: "s" == "[-1]"

res = palindrome("pranatas")
print(res)
