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
    return  cur.lastrowid



def add_admin(admin_id , access_level=1):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO ADMIN (CUSTOMER_ID,ACCESS_LEVEL) VALUES (%s,%s);"
    cur.execute(SQL_Query, (admin_id , access_level))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid

def add_customer(family_id , full_name , amount ,is_active='true'):
    print(full_name)
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO CUSTOMER (FAMILY_ID,FULL_NAME,TOTAL_CAPITAL,IS_ACTIVE) VALUES (%s,%s,%s,%s);"
    cur.execute(SQL_Query, (family_id , full_name , amount ,is_active))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid


def add_family(link_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO FAMILY (LINK_ID) VALUES (%s);"
    cur.execute(SQL_Query , (link_id ,))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid



def add_family_data(family_id , head_id , family_name):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE FAMILY SET HEAD_ID=%s,FAMILY_NAME=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (head_id , family_name , family_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid            


def add_loan_data(customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO LOAN (CUSTOMER_ID,LOAN_AMOUNT,INSTALLMENT_AMOUNT,NUMBER_REMAINING_INSTALLMENTS,AMOUNT_PAID) VALUES (%s,%s,%s,%s,%s);"
    cur.execute(SQL_Query , (customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid 


def add_installment(loan_id , NUMBER_PAID , Capital_increase):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO INSTALLMENT (LOAN_ID,INSTALLMENT_NUMBER,CAPITAL_INCREASE) VALUES (%s,%s,%s);"
    cur.execute(SQL_Query , (loan_id , NUMBER_PAID , Capital_increase))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid



def change_status_use_link_family(link_id , status='true'):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE FAMILY SET USE_LINK=%s WHERE LINK_ID=%s;"
    cur.execute(SQL_Query, (status , link_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid   


def delete_setting(admin_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "DELETE FROM SETTING WHERE ADMIN_ID=%s;"
    cur.execute(SQL_Query, (admin_id ,))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid  


def delete_admin(admin_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "DELETE FROM ADMIN WHERE ID=%s;"
    cur.execute(SQL_Query, (admin_id ,))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid  