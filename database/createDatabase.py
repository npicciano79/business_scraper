import mysql.connector
import config
#check to see if businessdatabase exists
#if it does not exist, businessdatabase is created


db=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
   
)

mycursor=db.cursor()

mycursor.execute('SHOW DATABASES')
databases=mycursor.fetchall()
databases_names=[database[0] for database in databases]

#print(databases_names)
#print(config.database)


if config.database in databases_names:
    print('{} exists.'.format(config.database))
else:
    print('Creating database {}'.format(config.database))
    mycursor.execute("CREATE DATABASE {config.database}")



