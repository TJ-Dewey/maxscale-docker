# CNA 350 W21
# Real World Project Zachary Rubin, zrubin@rtc.edu
# T.J. Dewey, tjdewey@student.rtc.edu

import mysql.connector

def connect():
    # correct address/ port?
    # previously used: passwd='maxpwd'
    conn = mysql.connector.connect(host='192.168.1.35',
                                    user='maxuser',
                                    password='maxpwd',
                                    port='4000')
    return conn

#### the 4 questions ####
# reminder: commits are for writing


def question_one(cursor):
## query tips from stackoverflow.com
## cursor tips from https://stackoverflow.com/questions/50596062/how-to-read-all-data-from-cursor-execute-in-python
    query = "SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 10;"
    cursor.execute(query)
    data = cursor.fetchall()
    print ('Last 10 of zipcodes 1')
    for row in data:
        print (row)
    return

def question_two(cursor):
    query = "SELECT Zipcode FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 10;"
    cursor.execute(query)
    data = cursor.fetchall()
    print ('First 10 of zipcodes 2')
    for row in data:
        print (row)
    return

def question_three(cursor):
    query = "SELECT MAX(DISTINCT Zipcode) FROM zipcodes_one.zipcodes_one;"
    cursor.execute(query)
    data = cursor.fetchall()
    print ('Largest in Zipcodes 1')
    print (data)
    return

def question_four(cursor):
    query = "SELECT MIN(DISTINCT Zipcode) FROM zipcodes_two.zipcodes_two;"
    cursor.execute(query)
    data = cursor.fetchall()
    print ('Smallest in Zipcodes 2')
    print (data)
    return

def main():
    conn = connect()
    curs = conn.cursor()
# queries
    question_one(curs)
    question_two(curs)
    question_three(curs)
    question_four(curs)
#disconnect
    conn.close()

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

