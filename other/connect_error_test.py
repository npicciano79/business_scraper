import mysql.connector
from mysql.connector import errorcode







"""
for table_name in TABLES:
    table_description=TABLES[table_name]
    try:
        print("Creating table: {}: ".format(table_name),end='')
        mycursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('table currently exists')
        else:
            print(E.msg)
    else:
        print('OK')

mycursor.close()

"""

