import mysql.connector
from config import db_config,database_name



def get_customer_data_b_fn_ln(full_name):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM CUSTOMER WHERE FULL_NAME=%s;"
    cur.execute(SQL_Query , (full_name ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if not data:
        return False
    return data



def get_customer_bot_id(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT BOT_ID FROM CUSTOMER WHERE ID=%s;"
    cur.execute(SQL_Query , (customer_id , ))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    return data["BOT_ID"]

def get_admin_list():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM ADMIN;"
    cur.execute(SQL_Query)
    data = cur.fetchall()    
    cur.close()
    conn.close()
    return [row['CUSTOMER_ID'] for row in data]


def get_admin_access(chat_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ACCESS_LEVEL FROM ADMIN WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query , (chat_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    return data["ACCESS_LEVEL"]



def get_id_b_admin_bot_id(admin_bot_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    sql_query = "SELECT ID FROM CUSTOMER WHERE BOT_ID = %s"
    cur.execute(sql_query, (admin_bot_id,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    if not data:
        return False
    return data["ID"]


def get_all_customer():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    sql_query = "SELECT * FROM CUSTOMER;"
    cur.execute(sql_query)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def get_admin_id_b_access(access_level):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT CUSTOMER_ID FROM ADMIN WHERE ACCESS_LEVEL=%s;"
    cur.execute(SQL_Query , (access_level ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data["CUSTOMER_ID"]




def get_family_data(family_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM FAMILY WHERE ID=%s;"
    cur.execute(SQL_Query , (family_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    return data

def get_all_family_id():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM FAMILY;"
    cur.execute(SQL_Query)
    data = cur.fetchall()    
    cur.close()
    conn.close()
    return [row['ID'] for row in data]



def check_admin(admin_id):
    bot_id_list = list()
    for customer_id in get_admin_list():
        bot_id = get_customer_bot_id(customer_id)
        bot_id_list.append(bot_id)
    if admin_id not in bot_id_list:
        return "admin"
    return "customer"



def check_is_in_db(chat_id):
    if not get_id_b_admin_bot_id(chat_id):
        return False
    return True
