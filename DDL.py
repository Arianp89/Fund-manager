import logging
import mysql.connector
from config import db_config,database_name




def create_database(database_name):
    conn=mysql.connector.connect(**db_config)
    cur=conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {database_name};")
    cur.execute(f"CREATE database {database_name} ;")
    conn.commit()
    cur.close()
    conn.close()
    print(f'database {database_name} created successfully')



def create_table_family(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_config, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE FAMILY(
    `ID`                BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `FAMILY_NAME`       VARCHAR(20) ,
    `HEAD_ID`           BIGINT ,
    `REGISTER_DATE`     DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table FAMILY created successfully')


def create_table_customer(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_config, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE CUSTOMER(
    `ID`                BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `FAMILY_ID`         BIGINT UNSIGNED NOT NULL,
    `BOT_ID`            BIGINT ,
    `FULL_NAME`         VARCHAR(50) NOT NULL ,
    `TOTAL_CAPITAL`     BIGINT ,
    `IS_ACTIVE`         VARCHAR(5) NOT NULL,
    `REGISTER_DATE`     DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (FAMILY_ID) REFERENCES FAMILY(ID)
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table customer created successfully')



def create_table_admin(database_name):
    conn=mysql.connector.connect(**db_config, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE ADMIN(
    `ID`                    BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `CUSTOMER_ID`           BIGINT UNSIGNED NOT NULL ,
    `ACCESS_LEVEL`          INT NOT NULL,
    `REGISTER_DATE`         DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`           DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER(ID)
    );"""
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print('table admin created successfully')


def create_table_setting(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_config, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE SETTING(
    `ADMIN_ID`          BIGINT UNSIGNED NOT NULL ,
    `CART_NUMBER`       BIGINT , 
    `REGISTER_DATE`     DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`       DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (ADMIN_ID) REFERENCES ADMIN(ID)
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table setting created successfully')

def create_table_loan(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_config , database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE LOAN(
    `ID`                                BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `CUSTOMER_ID`                       BIGINT UNSIGNED NOT NULL ,
    `LOAN_AMOUNT`                       BIGINT ,
    `INSTALLMENT_AMOUNT`                BIGINT ,
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



def create_table_installment(database_name):
    conn=mysql.connector.connection.MySQLConnection(**db_config, database=database_name)
    cur=conn.cursor()
    SQL_Query="""
    CREATE TABLE INSTALLMENT(
    `ID`                    BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `LOAN_ID`               BIGINT UNSIGNED NOT NULL ,
    `INSTALLMENT_NUMBER`    INT ,
    `CAPITAL_INCREASE`      BIGINT ,
    `STATUS`                VARCHAR(5) ,
    `REGISTER_DATE`         DATETIME DEFAULT CURRENT_TIMESTAMP ,
    `LAST_UPDATE`           DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ,
    FOREIGN KEY (LOAN_ID) REFERENCES LOAN(ID)
    );
    """
    cur.execute(SQL_Query)
    conn.commit()
    cur.close()
    conn.close()
    print(f'table customer created successfully')





if __name__ == '__main__':
    create_database(database_name)
    create_table_family(database_name)
    create_table_customer(database_name)
    create_table_admin(database_name)
    create_table_setting(database_name)
    create_table_loan(database_name)
    create_table_installment(database_name)
    print('end creat database')