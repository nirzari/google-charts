import json
import sys
import bottle
from bottle import route, request, response, template, get, run, HTTPResponse
from bottle import static_file
import MySQLdb
import io
import os
import random
from random import randint
import subprocess

#bottle = Bottle()

p1 = subprocess.Popen(['ip','addr','show','eth0'],stdout=subprocess.PIPE)
p2 = subprocess.Popen(['sed','-rn',r's/\s*inet\s(([0-9]{1,3}\.){3}[0-9]{1,3}).*/\1/p'],stdin=p1.stdout,stdout=subprocess.PIPE)
p1.stdout.close()
ip_addr = p2.communicate()[0].strip()
p1.wait()
app = bottle.app()

#Establish connection with database
connobj = MySQLdb.connect(host="awsdb.crtq9f6w5zvu.us-west-2.rds.amazonaws.com", user="nizi", passwd="Niziapp18!", db="aws_db")
#Create cursor
c = connobj.cursor()

@bottle.route('/')
def piechart():   
    return template('index')

@bottle.route('/pie_chart')
def pie_chart():   
    return template('index1')

@bottle.route('/pie', method = 'POST')
def pie():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        dict_data = request.forms.dict
        # getting the value of user parameter
        sid = dict_data['sid'][0]
        #create_table()
        data = get_data(sid)
        data = json.dumps(data)
        resp = HTTPResponse(body=data,status=200)
        return resp
    
    else:
        return 'This is a normal request'

def get_data(sid):
    try:
        # initializing list
        data = []
        query = "SELECT maths, science, english, computer, social_sci from marks WHERE id = " + str(sid)
        c.execute(query)
        # fetching all query result
        ans = c.fetchall()
        title = ['subject', 'marks']
        maths = ['maths',ans[0][0]]
        science = ['science',ans[0][1]]
        english = ['english',ans[0][2]]
        computer = ['computer',ans[0][3]]
        social_sci = ['social_sci',ans[0][4]]
        data.append(title)
        data.append(maths)
        data.append(science)
        data.append(english)
        data.append(computer)
        data.append(social_sci)
        print "Here is data: "
        print data
        return data
                    
    except Exception as e:
        print "Can not extract data: " + str(e)
        
# have commented create and insertion code since once it is done

"""def create_table():
    try:        
        #use database aws_db
        connectdb = 'USE aws_db'
        #connect with the database aws_db
        c.execute(connectdb)
        print "db changed"
        #Drop table if already existed earlier
        c.execute("DROP TABLE marks")
        print "table dropped"
        #create table named data
        table = 'CREATE TABLE IF NOT EXISTS marks '\
                '(id INT NOT NULL AUTO_INCREMENT,'\
                'sname varchar(100),'\
                'maths INT(5),'\
                'science INT(5),'\
                'english INT(5),'\
                'computer INT(5),'\
                'social_sci INT(5),PRIMARY KEY(id))'
        c.execute(table)
        insert_table()
   
    except Exception as e:
            print "Database creation/insertion problem: " + str(e)

def insert_table():            
    try:
        print "Insert called: "
        for i in range(1,51):
            sname = "nizi" + str(i)
            print sname
            maths = randint(0,100)
            print maths
            science = randint(0,100)
            english = randint(0,100)
            computer = randint(0,100)
            social_sci = randint(0,100) 
            insert = "INSERT INTO marks (sname, maths, science, english, computer, social_sci) values('"+ sname + "'," + str(maths) + "," + str(science) + "," \
                + str(english) + "," + str(computer) + "," + str(social_sci) + ")"
            c.execute(insert)
    
    except Exception as e:
        print "Data can't be inserted" + str(e)"""

connobj.commit()


if __name__=='__main__':
    bottle.debug(True)
    bottle.run(app=app,host='localhost',port=8080)
#run(host='0.0.0.0', port=8080)    

#end_All
