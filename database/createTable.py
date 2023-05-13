import mysql.connector
import config

db=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
    database=config.database,
   
)

mycursor=db.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS business_Name_Category(\
                business_id int NOT NULL AUTO_INCREMENT,\
                business_name varchar(200) NOT NULL,\
                business_category varchar(200) NOT NULL,\
                PRIMARY KEY (business_id)\
                )ENGINE=InnoDB")



mycursor.execute("CREATE TABLE IF NOT EXISTS business_location\
                    (business_id SMALLINT AUTO_INCREMENT,\
                    street VARCHAR(200),\
                    city VARCHAR(200),\
                    zipcode SMALLINT,\
                    phone INT,\
                    fax INT\
                    PRIMARY KEY(business_id)\
                    )ENGINE=InnoDB")

mycursor.execute("CREATE TABLE IF NOT EXISTS business_contact\
                    (business_id SMALLINT PRIMARY KEY AUTO_INCREMENT,\
                    website VARCHAR(200),\
                    about VARCHAR(200),\
                    contact VARCHAR(200)\
                    PRIMARY KEY(business_id)\
                    )ENGINE=InnoDB")