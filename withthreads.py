import time
import threading

def square(num):
    for i in num:
        time.sleep(0.5)
        print("square : " , i*i)


def cube(num1):
    for x in num1:
        time.sleep(0.2)
        print("cube : " , x*x*x)


L1 = [2,3,4,5]
starttime = time.time()
'''
square(arr)
cube(arr)

'''

t1 = threading.Thread(target=square, args=(L1,))
t2 = threading.Thread(target=cube, args=(L1,))

t1.start()
t2.start()

t1.join()
t2.join()


endtime = time.time()

totaltime = endtime - starttime
print(" Completed in :", totaltime)
