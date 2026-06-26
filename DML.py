import mysql.connector
import logging
import string
import random
from config import db_config,database_name



def add_customer_bot_id(customer_id , bot_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE CUSTOMER SET BOT_ID=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (bot_id,customer_id ))
    conn.commit()
    cur.close()
    conn.close()



def add_admin_access1(admin_id , access_level=1):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO ADMIN (CUSTOMER_ID,ACCESS_LEVEL) VALUES (%s,%s);"
    cur.execute(SQL_Query, (admin_id , access_level))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid

