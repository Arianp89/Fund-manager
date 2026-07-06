import logging
import mysql.connector
from config import db_config,database_name



class make_database:

    def __init__(self , db_config , db_name):
        self.db_config = db_config
        self.db_name = db_name


    def create_database(self):
        conn=mysql.connector.connect(**self.db_config)
        cur=conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {database_name};")
        cur.execute(f"CREATE database {database_name} ;")
        conn.commit()
        cur.close()
        conn.close()
        print(f'database {database_name} created successfully')



    def create_table_family(self):
        conn=mysql.connector.connection.MySQLConnection(**self.db_config, database=self.db_name)
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


    def create_table_customer(self):
        conn=mysql.connector.connection.MySQLConnection(**self.db_config, database=self.db_name)
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



    def create_table_admin(self):
        conn=mysql.connector.connection.MySQLConnection(**self.db_config, database=self.db_name)
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


    def create_table_setting(self):
        conn=mysql.connector.connection.MySQLConnection(**self.db_config, database=self.db_name)
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

    def create_table_loan(self):
        conn=mysql.connector.connection.MySQLConnection(**self.db_config, database=self.db_name)
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



    def create_table_installment(self):
        conn=mysql.connector.connection.MySQLConnection(**self.db_config, database=self.db_name)
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
    db = make_database(db_config , database_name)
    db.create_database()
    db.create_table_family()
    db.create_table_customer()
    db.create_table_admin()
    db.create_table_setting()
    db.create_table_loan()
    db.create_table_installment()
    print('end creat database')