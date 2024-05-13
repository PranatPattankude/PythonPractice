
import os, shutil

# 1.

# res = os.access(r'sandy.txt', os.R_OK)
# print(res)

# os.F_OK , os.R_OK , os.X_OK , os.W_OK


#2. delete the file
# os.remove(r'sandy.txt')
# os.remove(r'C:\Users\prana\Downloads\Python Class\files\new.py')


#3. mkdir ( create folder )
# os.mkdir(r'D:\SANTHOSH\Batches\Batch159-Python-Weekday-7am\Thursday')

#4.
# os.rmdir(r'D:\SANTHOSH\Batches\Batch159-Python-Weekday-7am\Thursday')

# 5
# shutil.rmtree(r'D:\SANTHOSH\Batches\Batch159-Python-Weekday-7am\Thursday')




# 7. rename

# os.rename(r'abc.txt',r'kajal.txt')
# os.rename(r'C:\Users\prana\Downloads\Python Class\files\old.txt', r'C:\Users\prana\Downloads\Python Class\files\new.py')



# 8. : gets the current folder path

# res = os.getcwd()
# print(res)
#



# 10 , list current directory files and folders

# res = os.listdir()
# print(res)




# 9.

# print("before shifting my path = "  , os.getcwd())
# print(os.listdir())
#
# os.chdir(r'C:\Users\prana\Downloads')
#
# print("after shifting my path = "  , os.getcwd())
# print(os.listdir())



# 11. only files

# shutil.copy(r'kajal.txt' , r'./thupaki/trisha.txt')




# 12. files & Folders

# moving file
# shutil.move(r'kajal.txt' , r'./thupaki/trisha.txt')



# moving folder
# shutil.move(r'om',r'./thupaki')
# shutil.move(r'new', r'C:\Users\prana\Downloads\new')


# shutil.move(r'D:\SANTHOSH\Batches\Batch138-8am\tuesday', \
# r'D:\SANTHOSH\Batches\Batch138-8am\files\tuesday')
#
#
#
#13. copying the folder

# shutil.copytree(r'om',r'./thupaki/om')


#14 gets all environment variable data

# res = os.environ
#
# for x,y in res.items():
#    print(x  , "===>" , y)



# 15.

# res = os.getenv('gmailusr')
# print(res)
# res = os.getenv('gmailpwd')
# print(res)


# # 16.
# res = os.system(r'type NUL > C:\Users\prana\Downloads\new')
# res = os.system('pip3 install pandas')
# print(res)

#######################



























