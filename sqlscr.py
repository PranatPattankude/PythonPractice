# # Step 1 : import module
# import pymysql as p
# # #cx_Oracle
# #
# # # Step 2 : connect to database
# santhoshdb = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'santhosh')
# print("connected successfully")
#
#
# #
# # # Step3  : create cursor
# mycursor = santhoshdb.cursor()
#
#
# # # # # #### selelect query ....
# # # # Step 4 : Prepare the query
# q1 = [
#         'select * from login;',
#         'select count(*) from login;',
#         'select email,password from login where name = "sandy";',
#         'select * from login where name = "santhosh";'
#       ]
#
# for query in q1:
#
#     # Step 5 : execute the query
#     mycursor.execute(query)
#
#     # Step 6 : fetch all result
#     res = mycursor.fetchall()
#     print(res)
#
#
# # Step7 : close DB
# santhoshdb.close()














#### dml statements




#
# #step 1
import pymysql as p


# Step 2 : connect to database
db = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'santhosh')

print("connected successfully")


# Step3  : create cursor
mycursor = db.cursor()



##### insert query

# Step 4 : insert the data
# q1 = [
#     "INSERT INTO login (id, name, email, password) VALUES (11, 'Venkat','venkat@gmail.com','venkat@987');",
#     "INSERT INTO login (id, name, email, password) VALUES (12, 'gokul','gokul@gmail.com','gukul@880');",
# ]



q1 = [
   """
CREATE TABLE Ashwini (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
""",
"""
CREATE TABLE Ameen (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
"""
     ]

# Step 5 : execute the query
for x in q1:
    try:
        mycursor.execute(x)
    except Exception as err:
        print("error msg was = ", err)

# Step 6 : commit
db.commit()

# Step 7 : Close DB
db.close()

print("successfully inserted ")


