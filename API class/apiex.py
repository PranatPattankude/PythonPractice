from flask import Flask, jsonify, request
import json
import pymysql as p
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def saninfo():
    if (request.method == 'GET'):
        mobilenum = "9986019197"
        return jsonify({'Mobile Number': mobilenum,
                        'companyname':'CG',
                        'username':'santhoh',
                        'password':'San@123'})


@app.route('/prajwal', methods=['GET','POST'])
def prajwalinfo():
    return jsonify({'name':'Prjwal raj',
                    'married':'no',
                    'age':'25',
                    'email':'prajwal@gmail.com'})


@app.route('/getdbdata', methods=['GET','POST'])
def getcount():
    dbc = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'srinivas')
    mycursor = dbc.cursor()
    q1 = 'select count(*) from users;'
    mycursor.execute(q1)
    res = mycursor.fetchall()
    # print(res)
    count = res[0][0]
    dbc.close()
    return jsonify({'reccount' : count})


@app.route('/getcred/<int:num>', methods=['GET'])
def getcred(num):
    dbc = p.connect(host='localhost', user='root', password='root', db='srinivas')
    mycursor = dbc.cursor()
    q1 = 'select * from users where id = ' + str(num) + ';'
    mycursor.execute(q1)
    res = mycursor.fetchall()
    print(res)
    name = res[0][2]
    password = res[0][3]
    mycred = {'name': name, 'password': password}
    dbc.close()
    return jsonify({
                    'name = ': name,
                    'password = ': password
                    })














if __name__ == '__main__':
    app.run(debug=True)

