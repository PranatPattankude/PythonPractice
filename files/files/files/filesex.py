# r , w  , a

# Reading the data from text file

# flog = open(r'new.txt','r')
# data = flog.read()
# data = flog.readlines()
# flog.close()
#
# print(data)
# print(type(data))


##### Example for read
## using list format
# count = 0
# for x in data:
#     if('error' in x.lower()):
#         count += 1
#
# print("count = ", count)


# using string
# count = data.lower().count('error')
# print(count)


# Ectract the error word using list
#
# errlines = []
# for x in data:
#     if('error' in x.lower()):
#         print(x.
#         errlines.append(x)
#
# print(errlines)

# Writing the data in to text file

# fvar = open(r'samantha.txt', 'w')
#
# var = """
# Samantha is beautiful
# she acts cool
# she dances awesome
# she is bold
# """
# fvar.write(var)
# fvar.close()



# listvar = ['hrithik','ranveer','allu','ranbir','mahesh']
# newlist = []
# for x in listvar:
#     newlist.append(x + '\n')
#
# print(newlist)
# #
# fvar = open(r'actors.txt','w')
# fvar.writelines(newlist)
# fvar.close()



# example for 'a' (append)
# Open a file in 'a' (append) mode
# f = open('example.txt', 'a')
# # Write some data to the file
# f.write('This is some new data.\n')
# f.write('This is another line of new data.\n')
