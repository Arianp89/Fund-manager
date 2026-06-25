import mysql.connector
from config import db_config,database_name


def get_admin_list():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM ADMIN;"
    cur.execute(SQL_Query)
    data = cur.fetchall()    
    cur.close()
    conn.close()
    return [row['ID'] for row in data]
