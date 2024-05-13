


# First Module Fuctions
global place
place = "Electroniccity"

print("loading the first module ")

import os



def createfiles(*files):
    ''' create files function will take n number of files and it will create it '''
    for x in files:
        fvar = open(x,'w')
        fvar.close()    
        print("created the file " , x)


def deletefiles(*files):
    ''' delete files function will take n number of files and it will delete it '''
    for x in files:
        os.remove(x)
        print("deleted file " , x)

def formatname(F,M,L="Sinha"):
    fullname = F + ' ' + M + ' ' + L
    return fullname


def removespace(var):
    op = var.replace(' ','')
    res = op.upper()
    return res
    

def calcbill(*items):
    '''This function takes any number of item price and give total and tax amount also considering 10%'''
    amnt = 0
    for x in items:
        amnt += x

    # res = sum(items)

    taxamnt = (amnt * 10) / 100
    finalbill = amnt + taxamnt

    return finalbill , taxamnt



def F1():
    print(" First module F1 function ")

def F2():
    print(" First module F2 function ")

print("hello i am module1")
