import mysql.connector
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
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO CUSTOMER (FAMILY_ID,FULL_NAME,TOTAL_CAPITAL,IS_ACTIVE) VALUES (%s,%s,%s,%s);"
    cur.execute(SQL_Query, (family_id , full_name , amount ,is_active))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid


def add_family(link_id , use_link='false'):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO FAMILY (LINK_ID , USE_LINK) VALUES (%s,%s);"
    cur.execute(SQL_Query , (link_id , use_link))
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


def add_loan_data(customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid , status):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO LOAN (CUSTOMER_ID,LOAN_AMOUNT,INSTALLMENT_AMOUNT,NUMBER_REMAINING_INSTALLMENTS,AMOUNT_PAID,STATUS) VALUES (%s,%s,%s,%s,%s,%s);"
    cur.execute(SQL_Query , (customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid , status))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid 


def add_installment(loan_id , NUMBER_PAID , status="false"):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO INSTALLMENT (LOAN_ID,INSTALLMENT_NUMBER , STATUS) VALUES (%s,%s,%s);"
    cur.execute(SQL_Query , (loan_id , NUMBER_PAID , status ))
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


def change_loan_number(loan_id , new_number = -1):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT NUMBER_REMAINING_INSTALLMENTS FROM LOAN WHERE ID=%s;"
    cur.execute(SQL_Query , (loan_id ,))
    number = cur.fetchone()   
    if number is None:
        return False
    number = number["NUMBER_REMAINING_INSTALLMENTS"]
    SQL_Query = "UPDATE LOAN SET NUMBER_REMAINING_INSTALLMENTS=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (number+new_number , loan_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid  


def add_pay(head_id , amount_paid , capital_increase , loan_id=None , installment_id = None):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO PAYMENT ( CUSTOMER_ID , AMOUNT_PAID , CAPITAL_INCREASE , LOAN_ID ,INSTALLMENT_ID ) VALUES (%s,%s,%s,%s,%s);"
    cur.execute(SQL_Query , (head_id , amount_paid , capital_increase , loan_id , installment_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid 

def change_customer_status(customer_id , total_capital = None , status = "false"):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE CUSTOMER SET IS_ACTIVE=%s , TOTAL_CAPITAL=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (status , total_capital , customer_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid   


def change_loan_status(customer_id , number = 0 , status="true"):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT LOAN_AMOUNT FROM LOAN WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query , (customer_id ,))
    amount_paid = cur.fetchone()   
    if amount_paid is None:
        return False
    amount_paid = amount_paid["LOAN_AMOUNT"]
    SQL_Query = "UPDATE LOAN SET STATUS=%s,NUMBER_REMAINING_INSTALLMENTS=%s,AMOUNT_PAID=%s WHERE CUSTOMER_ID=%s;"
    cur.execute(SQL_Query, (status , number , amount_paid , customer_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid

def change_all_installment_status(loan_id , status="true"):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE INSTALLMENT SET STATUS=%s WHERE LOAN_ID=%s;"
    cur.execute(SQL_Query, (status , loan_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid   


def delete_customer_bot_id(head_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "UPDATE CUSTOMER SET BOT_ID=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (None , head_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid  


def plus_amount_paid(loan_id):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT INSTALLMENT_AMOUNT,AMOUNT_PAID FROM LOAN WHERE ID=%s;"
    cur.execute(SQL_Query , (loan_id, ))
    install_amount = cur.fetchone()   
    if install_amount is None:
        return False
    amount_paid = install_amount["INSTALLMENT_AMOUNT"]+install_amount["AMOUNT_PAID"]
    SQL_Query = "UPDATE LOAN SET AMOUNT_PAID=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (amount_paid , loan_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid


def add_setting_data(admin_id , cart_number , cart_name , installment_number , capital_amount):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor()
    SQL_Query = "INSERT INTO SETTING ( ADMIN_ID , CART_NUMBER , CART_NAME , INSTALLMENT_NUMBER , CAPITAL_AMOUNT ) VALUES (%s,%s,%s,%s,%s);"
    cur.execute(SQL_Query , (admin_id , cart_number , cart_name , installment_number , capital_amount))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid 


def plus_customer_capital(customer_id , capital_amount):
    conn = mysql.connector.connect(**db_config, database=database_name)
    cur = conn.cursor(dictionary=True)
    SQL_Query = "SELECT TOTAL_CAPITAL FROM CUSTOMER WHERE ID=%s;"
    cur.execute(SQL_Query , (customer_id, ))
    total_capital = cur.fetchone()   
    if total_capital is None:
        return False
    amount_paid = total_capital["TOTAL_CAPITAL"] + capital_amount
    SQL_Query = "UPDATE CUSTOMER SET TOTAL_CAPITAL=%s WHERE ID=%s;"
    cur.execute(SQL_Query, (amount_paid , customer_id))
    conn.commit()
    cur.close()
    conn.close()
    return  cur.lastrowid