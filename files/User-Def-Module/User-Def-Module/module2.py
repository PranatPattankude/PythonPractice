# Second module functions

print(" loading second module ")

def mobval(num):
    res1 = len(num)
    res2 = num.isdigit()
    if(res1 == 10 and res2 == True):
        return "Valid Number"
    else:
        return "Invalid number"



def totalbill(curr,bal,disc,fine):
    bill = curr + bal + fine - disc
    return bill


def S1():
    print(" Second module S1 function")

def F1():
    print(" Second module F1 function ")


print("hello i am module2")
