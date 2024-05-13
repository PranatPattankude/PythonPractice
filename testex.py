# Step 1: import module
import pymysql as p

class dbfuncs:

    def __init__(self, host, user, password, db, dbtype, query):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.dbtype = dbtype
        self.query = query
        print("Init for ", self.dbtype)

    def checkconnection(self):
        dbc = p.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        print("connected successfully for ", self.dbtype)
        return dbc

    def executequery(self):
        dbc = self.checkconnection()
        mycursor = dbc.cursor()
        op = []
        for q in self.query:
            mycursor.execute(q)
            res = mycursor.fetchall()
            op.append(res)
        return op

    def createtable(self):
        dbc = self.checkconnection()
        mycursor = dbc.cursor()

        op = []

        for q in self.query:
            try:
                mycursor.execute(q)
                print('Database created successfully')
            except Exception as err:
                print("error is: ",err)
            res = dbc.commit()
            op.append(res)


        return op

santhoshdb = dbfuncs('localhost', 'root', 'root', 'santhosh', 'santhosh database', ['select count(*) from login;', 'select * from login where name = "santhosh";'])
sanjaydb = dbfuncs('localhost', 'root', 'root', 'santhosh', 'sanjay database', ['desc testtable;'])
sysdb = dbfuncs('localhost', 'root', 'root', 'srinivas', 'srinivas database', [ 'CREATE TABLE empdetail(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), number VARCHAR(10), email VARCHAR(255), address VARCHAR(255));'])

output = dbfuncs.createtable(sysdb)
output = dbfuncs.executequery(sysdb)



for x in output:
    print(x)

