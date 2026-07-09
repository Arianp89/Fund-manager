import mysql.connector
import os
import pickle
from typing import Dict, List, Any, Tuple


class DatabaseManager:
    """
    A comprehensive MySQL database management tool
    ابزار جامع برای مدیریت دیتابیس MySQL
    """
    
    def __init__(self, db_config: Dict, database_name: str):
        """Initialize database configuration"""
        self.db_config = db_config
        self.database_name = database_name
        self.language = "EN"  # Default language: EN or FA
    
    def set_language(self, lang: str):
        """Set language preference (EN or FA)"""
        self.language = lang.upper()
    
    def _get_message(self, key: str, lang: str = None) -> str:
        """Get localized message"""
        if lang is None:
            lang = self.language
        
        messages = {
            "EN": {
                "getting_relations": "🔄 Fetching table relationships...",
                "processing_table": "🔄 Processing table: {}",
                "data_saved": "✅ Data for {} saved successfully",
                "save_complete": "✅ All data has been saved",
                "reading_data": "🔄 Reading database data...",
                "inserting_data": "🔄 Inserting data into database...",
                "table_empty": "⚠️  Table {} is empty",
                "row_added": "✅ One row added to {}",
                "insert_complete": "✅ All data inserted successfully",
                "invalid_table": "❌ Invalid table name: {}",
                "error_relations": "❌ Error fetching relations: {}",
                "error_table_data": "❌ Error fetching table {} data: {}",
                "error_save": "❌ Error saving {}: {}",
                "error_read": "❌ Error reading {}: {}",
                "error_write": "❌ Error inserting data to {}: {}",
                "error_config": "❌ Error: db_config or database_name not defined",
            },
            "FA": {
                "getting_relations": "🔄 در حال دریافت روابط جداول...",
                "processing_table": "🔄 در حال پردازش جدول: {}",
                "data_saved": "✅ داده‌های {} ذخیره شد",
                "save_complete": "✅ تمام داده‌ها ذخیره شدند",
                "reading_data": "🔄 در حال خواندن داده‌های دیتابیس...",
                "inserting_data": "🔄 در حال درج داده‌ها به دیتابیس...",
                "table_empty": "⚠️  جدول {} خالی است",
                "row_added": "✅ یک سطر به {} اضافه شد",
                "insert_complete": "✅ تمام داده‌ها درج شدند",
                "invalid_table": "❌ نام جدول نامعتبر: {}",
                "error_relations": "❌ خطا در دریافت روابط: {}",
                "error_table_data": "❌ خطا در دریافت داده‌های جدول {}: {}",
                "error_save": "❌ خطا در ذخیره‌سازی {}: {}",
                "error_read": "❌ خطا در خواندن {}: {}",
                "error_write": "❌ خطا در درج داده‌ها به {}: {}",
                "error_config": "❌ خطا: متغیرهای db_config یا database_name تعریف نشده‌اند",
            }
        }
        
        return messages.get(lang, messages["EN"]).get(key, key)
    
    def get_relations(self) -> List[Dict]:
        """
        Get all foreign key relationships between tables
        دریافت تمام روابط خارجی بین جداول
        """
        try:
            print(self._get_message("getting_relations"))
            conn = mysql.connector.connect(**self.db_config, database=self.database_name)
            cur = conn.cursor(dictionary=True)
            cur.execute("""
            SELECT
                TABLE_NAME,
                COLUMN_NAME,
                REFERENCED_TABLE_NAME,
                REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = DATABASE()
            """)
            relations = cur.fetchall()
            return relations
        except mysql.connector.Error as err:
            print(self._get_message("error_relations").format(err))
            return []
        finally:
            cur.close()
            conn.close()
    
    def get_list_of_table(self, relations: List[Dict]) -> List[str]:
        """
        Get list of all tables based on relationship count
        دریافت لیست تمام جداول براساس تعداد روابط
        """
        table_count = {}
        
        for rel in relations:
            table_name = rel['TABLE_NAME']
            
            if table_name not in table_count:
                table_count[table_name] = 0
            
            table_count[table_name] += 1
        
        sorted_tables = sorted(table_count.items(), key=lambda x: x[1])
        table_list = [table_name for table_name, _ in sorted_tables]
        
        return table_list
    
    def get_table_data(self, table_name: str) -> List[Dict]:
        """
        Get all data from a table
        دریافت تمام داده‌های یک جدول
        """
        # Validate table name to prevent SQL Injection
        if not table_name.isalnum() and '_' not in table_name:
            print(self._get_message("invalid_table").format(table_name))
            return []
        
        try:
            conn = mysql.connector.connect(**self.db_config, database=self.database_name)
            cur = conn.cursor(dictionary=True)
            
            SQL_Query = f"SELECT * FROM `{table_name}`;"
            cur.execute(SQL_Query)
            data = cur.fetchall()
            return data
        except mysql.connector.Error as err:
            print(self._get_message("error_table_data").format(table_name, err))
            return []
        finally:
            cur.close()
            conn.close()
    
    def add_data_in_file(self, table: str, database_data: Any) -> bool:
        """
        Save database data to Pickle file
        ذخیره‌سازی داده‌های دیتابیس در فایل Pickle
        """
        try:
            os.makedirs('database_data', exist_ok=True)
            with open(os.path.join('database_data', f'{table}.pkl'), 'wb') as f:
                f.write(pickle.dumps(database_data))
            print(self._get_message("data_saved").format(table))
            return True
        except Exception as err:
            print(self._get_message("error_save").format(table, err))
            return False
    
    def read_database_data(self, table: str) -> Any:
        """
        Read stored data from Pickle file
        خواندن داده‌های ذخیره شده از فایل Pickle
        """
        try:
            with open(os.path.join('database_data', f'{table}.pkl'), 'rb') as f:
                read = f.read()
            return pickle.loads(read)
        except Exception as err:
            print(self._get_message("error_read").format(table, err))
            return []
    
    def write_to_database(self, table: str, keys: List[str], values: Tuple) -> bool:
        """
        Insert data into database using Prepared Statements
        درج داده‌ها در دیتابیس
        """
        try:
            conn = mysql.connector.connect(**self.db_config, database=self.database_name)
            cur = conn.cursor()
            
            columns_str = ", ".join([f"`{key}`" for key in keys])
            placeholders = ", ".join(["%s"] * len(values))
            sql = f"INSERT INTO `{table}` ({columns_str}) VALUES ({placeholders});"
            
            cur.execute(sql, values)
            conn.commit()
            print(self._get_message("row_added").format(table))
            return True
        except mysql.connector.Error as err:
            print(self._get_message("error_write").format(table, err))
            return False
        finally:
            cur.close()
            conn.close()
    
    def export_to_file(self) -> bool:
        """
        Read all database data and save to files
        خواندن تمام داده‌های دیتابیس و ذخیره‌سازی در فایل
        """
        print("\n" + "="*60)
        print(self._get_message("reading_data"))
        print("="*60 + "\n")
        
        relations = self.get_relations()
        table_list = self.get_list_of_table(relations)
        
        if not table_list:
            print("⚠️  No tables found in database")
            return False
        
        # Save table list
        self.add_data_in_file('main', table_list)
        
        # Save data for each table
        for table in table_list:
            print(self._get_message("processing_table").format(table))
            data = self.get_table_data(table)
            self.add_data_in_file(table, data)
        
        print("\n" + "="*60)
        print(self._get_message("save_complete"))
        print("="*60 + "\n")
        return True
    
    def import_from_file(self) -> bool:
        """
        Read stored data and re-insert into database
        خواندن داده‌های ذخیره شده و درج مجدد به دیتابیس
        """
        print("\n" + "="*60)
        print(self._get_message("inserting_data"))
        print("="*60 + "\n")
        
        table_list = self.read_database_data('main')
        
        if not table_list:
            print("⚠️  No tables found in main.pkl")
            return False
        
        for table in table_list:
            data_rows = self.read_database_data(table)
            
            if not data_rows:
                print(self._get_message("table_empty").format(table))
                continue
            
            keys = list(data_rows[0].keys())
            
            for row in data_rows:
                values = tuple(row.values())
                self.write_to_database(table, keys, values)
        
        print("\n" + "="*60)
        print(self._get_message("insert_complete"))
        print("="*60 + "\n")
        return True


def get_database_config(language: str = "EN") -> Tuple[Dict, str]:
    """
    Get database configuration from user input with better formatting
    دریافت پیکربندی دیتابیس از ورودی کاربر
    """
    prompts = {
        "EN": {
            "title": "\n" + "="*60 + "\n   DATABASE CONFIGURATION\n" + "="*60,
            "host": "Enter database host (default: localhost): ",
            "user": "Enter database user (default: root): ",
            "password": "Enter database password: ",
            "database": "Enter database name: ",
            "language": "Choose language (EN/FA) [default: EN]: ",
            "config_complete": "\n✅ Configuration complete!\n",
        },
        "FA": {
            "title": "\n" + "="*60 + "\n   پیکربندی دیتابیس\n" + "="*60,
            "host": "آدرس میزبان دیتابیس را وارد کنید (پیشفرض: localhost): ",
            "user": "نام کاربر دیتابیس را وارد کنید (پیشفرض: root): ",
            "password": "رمز عبور دیتابیس را وارد کنید: ",
            "database": "نام دیتابیس را وارد کنید: ",
            "language": "زبان را انتخاب کنید (EN/FA) [پیشفرض: EN]: ",
            "config_complete": "\n✅ پیکربندی کامل شد!\n",
        }
    }
    
    lang = language.upper()
    if lang not in prompts:
        lang = "EN"
    
    print(prompts[lang]["title"])
    
    host = input(prompts[lang]["host"]).strip() or "localhost"
    user = input(prompts[lang]["user"]).strip() or "root"
    password = input(prompts[lang]["password"]).strip()
    database_name = input(prompts[lang]["database"]).strip()
    
    db_config = {
        'host': host,
        'user': user,
        'password': password
    }
    
    print(prompts[lang]["config_complete"])
    
    return db_config, database_name


def display_menu(language: str = "EN") -> str:
    """
    Display main menu with better formatting
    نمایش منوی اصلی
    """
    menus = {
        "EN": {
            "title": "\n" + "="*60 + "\n   MAIN MENU\n" + "="*60,
            "option1": "  1️⃣  Export database data to files",
            "option2": "  2️⃣  Import data from files to database",
            "option3": "  3️⃣  Exit",
            "prompt": "\nSelect an option (1-3): ",
            "invalid": "❌ Invalid option. Please select 1, 2, or 3.",
        },
        "FA": {
            "title": "\n" + "="*60 + "\n   منوی اصلی\n" + "="*60,
            "option1": "  1️⃣  خروجی داده‌های دیتابیس به فایل‌ها",
            "option2": "  2️⃣  درج داده‌ها از فایل‌ها به دیتابیس",
            "option3": "  3️⃣  خروج",
            "prompt": "\nیک گزینه انتخاب کنید (1-3): ",
            "invalid": "❌ گزینه نامعتبر. لطفاً 1 یا 2 یا 3 را انتخاب کنید.",
        }
    }
    
    lang = language.upper()
    if lang not in menus:
        lang = "EN"
    
    print(menus[lang]["title"])
    print(menus[lang]["option1"])
    print(menus[lang]["option2"])
    print(menus[lang]["option3"])
    
    while True:
        choice = input(menus[lang]["prompt"]).strip()
        if choice in ['1', '2', '3']:
            return choice
        print(menus[lang]["invalid"])


def main():
    """
    Main application entry point
    نقطه شروع برنامه
    """
    try:
        print('                       WARNING                            ')
        print('----------------------------------------------------------')
        print('Please read the documentation before using it. \nIf you want to move database information, copy this file and database_data folder and place it on the new device. \n')
        print("============================================================")
        # Get language preference
        lang_prompt = "Choose language (EN/FA) [default: EN]: "
        language = input(lang_prompt).strip().upper() or "EN"
        if language not in ["EN", "FA"]:
            language = "EN"
        
        # Get database configuration
        db_config, database_name = get_database_config(language)
        
        # Create manager instance
        manager = DatabaseManager(db_config, database_name)
        manager.set_language(language)
        
        # Main loop
        while True:
            choice = display_menu(language)
            
            if choice == '1':
                manager.export_to_file()
            elif choice == '2':
                manager.import_from_file()
            elif choice == '3':
                print("\n👋 Thank you for using Database Manager!")
                print("   سپاس از استفاده شما از Database Manager!")
                break
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user")
        print("   برنامه توسط کاربر متوقف شد")
    except Exception as err:
        print(f"❌ An unexpected error occurred: {err}")
        print(f"   خطای غیرمنتظره ای رخ داد: {err}")


if __name__ == "__main__":
    main()