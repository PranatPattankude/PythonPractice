import time
t1 = time.time()

def square(num):
    for i in num:
        time.sleep(0.5)
        print("square : " , i*i)


def cube(num1):
    for x in num1:
        time.sleep(0.2)
        print("cube : " , x*x*x)


arr = [2,3,4,5]

print(t1)
square(arr)
cube(arr)


t2 = time.time()
print(t2)

print(" Completed in :", round(t2-t1,2))
