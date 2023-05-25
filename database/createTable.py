import mysql.connector
import config

db=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
    database=config.database,
   
)

mycursor=db.cursor()


"""
mycursor.execute("CREATE TABLE IF NOT EXISTS business_name_category\
                    (business_id SMALLINT AUTO_INCREMENT NOT NULL,\
                     business_category varchar(200) NOT NULL,\
                     business_name varchar(200) NOT NULL,\
                     PRIMARY KEY(business_id)\
                    )ENGINE=InnoDB")



mycursor.execute("CREATE TABLE IF NOT EXISTS business_location\
                    (business_id SMALLINT AUTO_INCREMENT NOT NULL,\
                    street VARCHAR(200),\
                    city VARCHAR(200),\
                    zipcode VARCHAR(200),\
                    phone VARCHAR(200),\
                    fax VARCHAR(200),\
                    PRIMARY KEY(business_id)\
                    )ENGINE=InnoDB")
"""
mycursor.execute("CREATE TABLE IF NOT EXISTS business_contact\
                    (business_id SMALLINT AUTO_INCREMENT NOT NULL,\
                    website VARCHAR(200),\
                    about VARCHAR(1000),\
                    contact VARCHAR(1000),\
                    PRIMARY KEY(business_id)\
                    )ENGINE=InnoDB")


"""
mycursor.execute("CREATE TABLE IF NOT EXISTS business_full\
                    (business_id SMALLINT AUTO_INCREMENT NOT NULL,\
                    business_category varchar(200) NOT NULL,\
                    business_name varchar(200) NOT NULL,\
                    street VARCHAR(200),\
                    city VARCHAR(200),\
                    zipcode SMALLINT,\
                    phone VARCHAR(200),\
                    fax VARCHAR(200),\
                    website VARCHAR(200),\
                    about VARCHAR(200),\
                    contact VARCHAR(200),\
                    PRIMARY KEY(business_id)\
                    )ENGINE=InnoDB")
"""