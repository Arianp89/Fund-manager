import logging
import mysql.connector
from config import *




def create_database(database_name):
    conn=mysql.connector.connect(**db_confing)
    cur=conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {database_name};")
    cur.execute(f"CREATE database {database_name} ;")
    conn.commit()
    cur.close()
    conn.close()
    print(f'database {database_name} created successfully')



def create_table_customer(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_confing, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE CUSTOMER(
    `ID`                BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `BOT_ID`            BIGINT ,
    `FIRST_NAME`        VARCHAR(15) ,
    `LAST_NAME`         VARCHAR(15) ,
    `TOTAL_CAPITAL`     BIGINT NOT NULL ,
    `REGISTER_DATE`     DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table customer created successfully')



def create_table_admin(database_name):
    conn=mysql.connector.connect(**db_confing, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE ADMIN(
    `CUSTOMER_ID`           BIGINT UNSIGNED NOT NULL ,
    `ACCESS_LEVEL`          INT ,
    `REGISTER_DATE`         DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`           DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(ID)
    );"""
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print('table admin created successfully')



def create_table_supervisor(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_confing , database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE SUPERVISOR(
    `CUSTOMER_ID`       BIGINT UNSIGNED NOT NULL ,
    `LIST_SUPERVISOR`   TEXT ,
    `REGEITER_DATE`     DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(ID)
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table supervisor created successfully')



def create_table_loan(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_confing , database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE LOAN(
    `CUSTOMER_ID`                       BIGINT UNSIGNED NOT NULL ,
    `LOAN_AMOUNT`                       BIGINT NOT NULL ,
    `NUMBER_REMAINING_INSTALLMENTS`     INT , 
    `AMOUNT_PAID`                       BIGINT ,
    `REGISTER_DATE`                     DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`                       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (CUSTOMER_ID)           REFERENCES CUSTOMER(ID)
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table loan created successfully')





if __name__ == '__main__':
    create_database(database_name)
    create_table_customer(database_name)
    create_table_admin(database_name)
    create_table_supervisor(database_name)
    create_table_loan(database_name)
    print('end creat database')