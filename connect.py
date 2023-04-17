import mysql.connector
#Create the connection object

def open_db_connection():
    myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "notroot", database = "fposts")
    print(myconn)
    return myconn


def close_db_connection():
    myconn.close()
    


