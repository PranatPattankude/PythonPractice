# # Concatenation
# L1 = [10,20,30]
# L2 = [40,50]
#
# res = L1 + L2
# print(res)
#
#

# D1 = {'A':20,'B':40}
# D2 = {'x':20,'y':40}
# res = D1 + D2
# print(res)


# Duplication
# L1 = [10,20,30]
# res = L1 * 3
# print(res)


# Index and index range
# L1 = [10,20,30,40,50]
# print(L1[0])
# print(L1[-1])
# print(L1[0:2])

# T1 = (10,20,30,40,50)
# print(T1[0])
# print(T1[-1])
# print(T1[0:2])


#  Membership operator

# L1 = [10,20,30,40,50]
# res = 20 in L1
# print(res)


# t1 = ('a','b','c')
# t2 = ('x',10)
#
# res = t1 + t2
# print(res)


# D1 = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 2, 'F': 1,}
# res = 10 in D1
# print(res)
# print(max(D1))


##### Functions

# L1 = [10, 20, 30, 40, 50]
# T1 = (10, 20, 30, 40, 50)
# D1 = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
# D2 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}
#
# print(type(D1))
#
# res = len(L1)
# print(res)
#
# res = max(T1)
# print(res)
#
# res = min(D2)
# print(res)
#
# strlist = ['sandy','ajit', 'ravi', 'prem','santhosh']
# print(max(strlist))


# adding elements
#
# L1 =[10,20,30,40,50]
# L1.append(60)
# print(L1)

# T1 = (10,20,30,40,50)
# T1.append(60)
# print(T1)


# L1.extend([70,80,90,100])
# print(L1)

#
# L1 = [10,20,30,40,50]
#
# L1.insert(0,38)
# print(L1)


## adding elements in dictionary

# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
# D1.setdefault('F',60)
# print(D1)
#
# D2 = {'X':100,'Y':200 , 'Z':300}
# D1.update(D2)
# print(D1)


### delete elements


# L1 = [10, 20, 30, 40, 50]
# del L1[3]
# print(L1)
#
# del L1[0]
# print(L1)

# del L1[0:2]
# print(L1)

# L1 = [10,20,30,40,50]
# res = L1.pop(2) # or del L1[2]
# print(L1)
# print(res)
#
# L1.insert(2,res)
# print(L1)


##### Remove function

# L1 = [10, 20, 30, 40, 50, 30, 60, 30, 70, 30, 80, 30, 90, 30]
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)
#
# L1.remove(30)
# print(L1)


# count function
#
# L1 = [10,20,30,40,50,30,60,30,70,30,80,30,90,30]
#
# cnt = L1.count(30)
# print(cnt)
# print(L1)

# while(cnt > 1):
#     L1.remove(30)
#     cnt -= 1
#
# print(L1)


# for x in range(cnt-1):
#     L1.remove(30)
#
# print(L1)


# #
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
#
# del D1['B']
# print(D1)
#
# D1.clear()
# print(D1)
# #
# L1 = [10,20,30,40,50]
# L1.clear()
# print(L1)


#
# # del L1
# # print(L1)


####### Update the value


# L1 = [10,20,30,40,50]
#
# L1[2] = 33
# print(L1)
#
# L1[0:2] = ["ABCD", 1.5]
# print(L1)
#
# T1 = (10,20,30,40,50,20,60,20)
# res = T1.count(20)
# print(res)

#
# L1 = [10, 20, 30, 40, 50, 60, 50, 90, 50, 100, 60, 50, 10]
# pos = L1.index(10, 0, len(L1))
# print(pos)



#
# L1 = [4,2,1,3,5]
# L1.sort()
# print(L1)
#
# L1.reverse()
# print(L1)
#
#
# names = ['raj','sandy','amit','krishna', 'santhosh']
# names.sort()
# print(names)


# ####  Mistake in copy [ shallow and deep copy ]
# L1 = [10,20,30,40,50]
# L2 = L1.copy()
#
# print(id(L1))
# print(id(L2))
#
#
# print("before delete")
# print(L1)
# print(L2)
#
# del L1[0:3]
#
# print("after delete")
# print(L1)
# print(L2)

#
# L1 = [10,20,30,40,50]
# L2 = L1.copy()
# print(L2)


# L1 = [10,20,30,40,50]
# print(type(L1))
# newvar = tuple(L1)
# print(newvar)


#
# T1 = (10,20,30,40,50)
# newlist = list(T1)
# print(newlist)


#
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
# #
# mykeys = list(D1.keys())
# myvalues = list(D1.values())
# myitems = D1.items()
# #
# print(mykeys)
# print(myvalues)
# print(myitems)


#
# D1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
#
# for k,v in D1.items():
#     if(v > 25):
#         print(k, "====>" , v)
#
#
# stud = {'rahul':90 , 'niki':87 , 'san':32, 'pun' : 31}
#
# for name,per in stud.items():
#     if(per < 35):
#         print(name, per)


#
# L1 = [1,2,7,3,1,2,5,6,2,3,6,2,1]
#
# mylist = list(set(L1))
# print(mylist)


D1 = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
# print(D1['X'])

res = D1.get('X', 60)
print(res)



# L1 = [10,20,30,40,50]
# for x in L1:
#     print(x)
