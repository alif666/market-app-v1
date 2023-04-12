import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "notroot", database = "fposts")  
  
#printing the connection object   
print(myconn)   
  
#creating the cursor object  
cur = myconn.cursor()  
  
print(cur)  


#Show Databases
'''
try:  
    dbs = cur.execute("show databases")  
except:  
    myconn.rollback()  
for x in cur:  
    print(x)
'''
'''

#Create Table
try:  
    #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
    dbs = cur.execute("create table if not exists f_user(f_user_name varchar(20) not null, f_user_id int(20) not null primary key, f_user_url varchar(2083), f_user_post_id int(20))")  
except:  
    myconn.rollback()

try:  
    dbs = cur.execute("select * from fposts.f_user")  
except:  
    myconn.rollback()  
for x in cur:  
    print(x)
    
'''

def_close_db_connection:
    myconn.close()
    


