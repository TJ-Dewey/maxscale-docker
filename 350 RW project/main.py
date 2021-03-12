# CNA 350 W21
# Real World Project Zachary Rubin, zrubin@rtc.edu
# T.J. Dewey, tjdewey@student.rtc.edu

# With multi-cursor hint from Luma Naser

import mysql.connector

def connect_zip1():
    # correct address/ port?
    # previously used: passwd='maxpwd'
    conn1 = mysql.connector.connect(host='192.168.1.33',
                                    user='maxuser',
                                    password='maxpwd',
                                    database='zipcodes_one')
    return conn1



def connect_zip2():
    # previously used: passwd='maxpwd'
    conn2 = mysql.connector.connect(host='192.168.1.33',
                                    user='maxuser',
                                    password='maxpwd',
                                    database='zipcodes_two')
    return conn2

#### the 4 questions ####

def question_one(cursor, conn):
## query tips from stackoveflow.com
    query = ("SELECT Zipcode FROM zipcodes_one LIMIT 10 OFFSET N-10")
    cursor.execute(query)
    conn.commit()
    print(cursor)
    return cursor

def question_two(cursor, conn):
    ## query tips from stackoveflow.com
    query = ("SELECT Zipcode FROM zipcodes_two LIMIT 10")
    cursor.execute(query)
    conn.commit()
    print(cursor)
    return cursor

def question_three(cursor, conn):
    query = ("SELECT MAX(Zipcode) FROM zipcodes_one")
    cursor.execute(query)
    conn.commit()
    print(cursor)
    return cursor

def question_four(cursor, conn):
    query = ("SELECT MIN(Zipcode) FROM zipcodes_two")
    cursor.execute(query)
    conn.commit()
    print(cursor)
    return cursor

def main():
# connections
    conn1 = connect_zip1()
    conn2 = connect_zip2()
    curs1 = conn1.cursor()
    curs2 = conn2.cursor()
# queries
    question_one(curs1, conn1)
    question_two(curs2, conn2)
    question_three(curs1, conn1)
    question_four(curs2, conn2)
#disconnect
    conn1.close()
    conn2.close()

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
