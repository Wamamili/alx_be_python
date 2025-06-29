import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL
    connection = mysql.connector.connect(
        host="127.0.0.1",    
        #port="3306",            
        user="root",
        password="890532488",
        database="md_water_services"
    )

    if connection.is_connected():
        print("✅ Connected to MySQL Server")
        db_Info = connection.get_server_info()
        print("MySQL Server version:", db_Info)

except Error as e:
    print("❌ Error while connecting to MySQL:", e)


