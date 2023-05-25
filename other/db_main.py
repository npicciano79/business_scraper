import db_connector
import business_tables_create 



mycursor, databaseName=db_connector.databaseConnect()
#business_tables_create.tableCreate(mycursor)




print(mycursor)
print(databaseName)