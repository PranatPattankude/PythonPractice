

### Reading data from file

fvar = open(r'D:\SANTHOSH\Batches\Batch157-9amto8am-Weekday-Python\files\filesNew\names.txt','r')
#data = fvar.read()
data = fvar.readlines()
fvar.close()

print(data)
print(type(data))


### create text file and write data in  to the text file


fdata = open(r'data.txt', 'w')
info = """
this is 
a sample multi
line string variable 
writing in to file 
"""

listinfo = ['sachin','rahul','prasad','yuvraj','kholi']

newlistinfo = []

for x in listinfo:
    x = x + '\n'
    newlistinfo.append(x)

print(listinfo)
print(newlistinfo)

#fdata.write(info)

fdata.writelines(newlistinfo)

fdata.close()






