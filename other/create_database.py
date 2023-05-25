from db_connector import mycursor,cnx

def create_database(mycursor):
    try:
        mycursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'UTF8'".format(BD_NAME)
        )