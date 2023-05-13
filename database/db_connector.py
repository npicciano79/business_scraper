import mysql.connector
from mysql.connector import errorcode
import config
import csv


"""
---databaseConnect() creates connection to businessdata db as 
---cxn and sets mycursor as cnx.cursor()
---uses try/except clause, tests for password/username error and
---database error 
---returns cxn and database name to db_main.py
"""

def databaseConnect():
    try:
        cnx=mysql.connector.connect(
                host=config.host,
                user=config.user,
                passwd=config.password,
                database=config.database,
        )
    except mysql.connector.Error as E:
        if E.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your username or password.')
        elif E.errno==errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(E)
    else:
        cursor=cnx.cursor()
        dbTest(cursor)
        #tableCreate(cursor)
        #tableInsert(cursor)
        #tableView(cursor)
        #dbTest(cursor)
    cursor.close()






def dbTest(cursor):
    print('db test hit')
    for line in open('./test.sql'):
        cursor.execute(line)
    cursor.close()



def tableCreate(cursor):
    print('creating database tables')
    
    cursor.execute("CREATE TABLE IF NOT EXISTS business_name_category\
                   (business_id SMALLINT PRIMARY KEY AUTO_INCREMENT,\
                   name VARCHAR(100),\
                   category VARCHAR(100)) ")

    cursor.execute("CREATE TABLE IF NOT EXISTS business_data\
                   (business_id SMALLINT PRIMARY KEY AUTO_INCREMENT,\
                   street VARCHAR(200),\
                   city VARCHAR(200),\
                   zipcode SMALLINT,\
                   phone INT,\
                   fax INT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS business_contact\
                   (business_id SMALLINT PRIMARY KEY AUTO_INCREMENT,\
                   website VARCHAR(200),\
                   about VARCHAR(200),\
                   contact VARCHAR(200))")

    print('tables created')


def tableInsert(cursor):

    with open('businessCSV_cleaned.csv','rb')as csvFile:
        reader=csv.reader(csvFile)
        for row in reader:
            col1,col2=row[:2]

            #insert data into mysql table
            insertQuery = "INSERT INTO business_name_category(name,category) VALUES (%s,%s) "
            values=(col1,col2)
            cursor.execute(insertQuery,values)
    print('data inserted')


def tableView(cursor):
    print('table view hit')
    cursor.execute("SELECT * from business_name_category")

    for table in cursor:
        print(table)



    """
    strSQL='INSERT INTO `business_name_category`(name,category)'+\
            "VALUES()

    print("inserting data")
    with open('businessCSV_cleaned.csv', 'r')as f:
        reader=csv.reader(f)
        for row in reader:
            cursor.execute('INSERT INTO business_name_category(name,\
                           category)'\
                           'VALUES()')


    with open('businessCSV.csv','r')as infile:
        reader=csv.reader(infile)
        next(reader,None) #skip header
        with open('businessCSV_cleaned.csv','w',newline='')as outfile:
            writer=csv.writer(outfile,delimiter=',',escapechar='',quoting=csv.QUOTE_NONE)
            for row in reader:
                writer.writerow((row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))

    """




databaseConnect()











#create new database
#mycursor.execute("CREATE DATABASE businessdata")

#creates table business_name_category
#mycursor.execute('CREATE TABLE business_name_category(business_id int UNSIGNED PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), category VARCHAR(200))')

#mycursor.execute("CREATE TABLE IF NOT EXISTS business_id int UNSIGNED PRIMARY KEY AUTO_INCREMENT, business_category VARCHAR(200) ,business_name VARCHAR(100), street VARCHAR(100), city VARCHAR(50), phone")

#command to drop a table
#mycursor.execute('DROP TABLE business_name_category')

#describes table data in business_name_category
"""
mycursor.execute('DESCRIBE business_name_category')
for x in mycursor:
    print(x)
"""








