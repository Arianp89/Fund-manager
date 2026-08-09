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
    if data is None:
        return False
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
    if data is None:
        return False
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




def get_family_data(link_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM FAMILY WHERE LINK_ID=%s;"
    cur.execute(SQL_Query , (link_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    return data


def get_family_data_by_id(family_id):
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
        return "customer"
    return "admin"



def check_is_in_db(chat_id):
    if not get_id_b_admin_bot_id(chat_id):
        return False
    return True


def get_family_link_status(family_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT USE_LINK FROM FAMILY WHERE ID=%s;"
    cur.execute(SQL_Query , (family_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    data = data["USE_LINK"]
    if data == "true":
        return False
    return True


def get_setting_data(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM ADMIN WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query , (customer_id ,))
    admin_id = cur.fetchone()
    if admin_id is None:
        return False
    SQL_Query = "SELECT * FROM SETTING WHERE ADMIN_ID=%s;"
    cur.execute(SQL_Query , (admin_id["ID"] ,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    if data is None:
        return False
    return data



def get_admin_id(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT ID FROM ADMIN WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query , (customer_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data["ID"]


def get_admin_access_by_chat_id(chat_id):
    admin_id = get_id_b_admin_bot_id(chat_id)
    admin_access = get_admin_access(admin_id)
    return admin_access


def get_all_family_data():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM FAMILY;"
    cur.execute(SQL_Query)
    data = cur.fetchall()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data


def get_family_data_by_head_id(head_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM FAMILY WHERE HEAD_ID=%s;"
    cur.execute(SQL_Query , (head_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data


def get_all_family_data_by_id(family_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM CUSTOMER WHERE FAMILY_ID=%s;"
    cur.execute(SQL_Query , (family_id ,))
    data = cur.fetchall()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data




def get_customer_data_by_id(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT * FROM CUSTOMER WHERE ID=%s;"
    cur.execute(SQL_Query , (customer_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data

def get_loan_data_by_customer_id(customer_id ):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT * FROM LOAN WHERE CUSTOMER_ID = %s  ORDER BY id DESC LIMIT 1"
    cur.execute(SQL_Query , (customer_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data


def get_payment_data_by_customer_id(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT * FROM PAYMENT WHERE CUSTOMER_ID = %s ORDER BY id DESC LIMIT 1"
    cur.execute(SQL_Query , (customer_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data


def get_loan_id_by_customer_id(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT ID FROM LOAN WHERE CUSTOMER_ID = %s ORDER BY id DESC LIMIT 1"
    cur.execute(SQL_Query , (customer_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data["ID"]



def get_all_installment_data_by_loan_id(loan_id , status="true"):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT * FROM INSTALLMENT WHERE LOAN_ID = %s and STATUS = %s"
    cur.execute(SQL_Query , (loan_id , status))
    data = cur.fetchall()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data

def get_loan_data_by_id(loan_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT * FROM LOAN WHERE ID =%s"
    cur.execute(SQL_Query , (loan_id ,))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data


def get_all_loan_data():
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT * FROM LOAN;"
    cur.execute(SQL_Query)
    data = cur.fetchall()    
    cur.close()
    conn.close()
    return data

def get_all_installment_data_by_id(loan_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT * FROM INSTALLMENT WHERE LOAN_ID =%s;"
    cur.execute(SQL_Query , (loan_id ,))
    data = cur.fetchall()    
    cur.close()
    conn.close()
    return data


def get_admin_id_by_customer_id(customer_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query =  "SELECT ID FROM ADMIN WHERE CUSTOMER_ID =%s;"
    cur.execute(SQL_Query , (customer_id, ))
    data = cur.fetchone()    
    cur.close()
    conn.close()
    if data is None:
        return False
    return data["ID"]
