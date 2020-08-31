import mysql.connector
mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Sss@23052000"
                )
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pythonics")
mycursor.execute("USE pythonics")
query = '''CREATE TABLE account_info(
    id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(40) NOT NULL,
    EmailId VARCHAR(30) NOT NULL,
    dob VARCHAR(10),
    gender VARCHAR(6) NOT NULL,
    mobile VARCHAR(13) NOT NULL,
    password VARCHAR(30) NOT NULL)
    '''
mycursor.execute(query)















