import mysql.connector
import config

cnx=mysql.connector.connect(
            host=config.host,
            user=config.user,
            passwd=config.password,
            database=config.database,
    )

cursor=cnx.cursor()



DB_NAME='businessdata'

TABLES={}

TABLES['temp1']=(
    "CREATE TABLE IF NOT EXISTS temp1("
    "   business_id int(1000) NOT NULL AUTO_INCREMENT,"
    "   business_name varchar(200) NOT NULL,"
    "   business_category varchar(200) NOT NULL,"
    "   PRIMARY KEY (business_id)"
    ")ENGINE=InnoDB")


TABLES['temp2']=(
    "CREATE TABLE IF NOT EXISTS temp2("
    "   business_id int(1000) NOT NULL AUTO_INCREMENT,"
    "   street varchar(200) NOT NULL,"
    "   city varchar(200) NOT NULL,"
    "   zip int(5),"
    "   phone int(10),"
    "   fax int(10),"
    "   PRIMARY KEY(business_id)"
    ")ENGINE=InnoDB")


TABLES['temp3']=(
    "CREATE TABLE IF NOT EXISTS temp3("
    "   business_id int(1000) NOT NULL AUTO_INCREMENT,"
    "   website varchar(200) NOT NULL,"
    "   about text NOT NULL,"
    "   contact varchar(200) NOT NULL,"
    "   PRIMARY KEY (business_id)"
    ")ENGINE=InnoDB")

for table in TABLES:
    cursor.execute(table)