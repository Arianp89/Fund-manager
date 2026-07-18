from backup import DatabaseManager
from config import db_config,database_name
from keyboard.keyboard import customer_markup,admin_markup
from keyboard.call_back_markup import add_admin_markup,change_admin_access2_markup,send_message_customer_markup
import shutil
import os
from services.admin_ser import *
import datetime


class admin_button:

    def __init__(self , bot):
        self.bot = bot
    

    def answer_customer(self , chat_id , access_level=2):

        if not check_is_in_db(chat_id):
            return False

        if check_admin(chat_id) == 'customer':
            self.bot.send_message(chat_id , 'دستور وارد شده اشتباه است' , reply_markup = customer_markup(chat_id))
            return False
        
        admin_access = get_admin_access_by_chat_id(chat_id)
        if admin_access == access_level:
            return True
        self.bot.send_message(chat_id , 'دستور وارد شده اشتباه است' , reply_markup = customer_markup(chat_id))
        return False
    


    def go_to_admin_panel(self , message):
        cid = message.chat.id
        customer_id = get_id_b_admin_bot_id(cid)
        access_level = get_admin_access(customer_id)
        if not self.answer_customer(cid , access_level):
            return
        
        self.bot.send_message(cid , "شما وارد پنل ادمین شدید" , reply_markup = admin_markup(cid))



    def go_to_customer_panel(self , message):  
        cid = message.chat.id

        access_level = get_admin_access(cid)
        if not self.answer_customer(cid , access_level):
            return
        
        self.bot.send_message(cid , "شما وارد پنل کاربر شدید" , reply_markup = customer_markup(cid))


    def get_backup(self ,message):
        cid = message.chat.id
        if not self.answer_customer(cid , 1):
            return

        database = DatabaseManager(db_config , database_name)
        database.export_to_file()
        os.makedirs("Data", exist_ok=True)
        folder_path = "database_data"
        backup_path = os.path.join("Data" , "backup")

        shutil.make_archive(
            backup_path,
            "zip",
            folder_path )
        
        now = datetime.datetime.today()
        with open(os.path.join("Data", "backup.zip"), "rb") as f:
            text = f"فایل [backup](github.com/arianp89/database-data-mover) {now}"
            self.bot.send_document(cid, f, caption=text, parse_mode="Markdown")

        
    def make_family_link(self , message):
        cid = message.chat.id
        if not self.answer_customer(cid , 1):
            return
        
        text_list = add_family_link_text()
        for text in text_list:
            self.bot.send_message(cid , text)


    def add_admin_access2(self , message):
        cid = message.chat.id
        if not self.answer_customer(cid , 1):
            return
        
        markup = add_admin_markup(self.bot)
        if not markup:
            self.bot.send_message(cid , "شما ادمین اضافه کردید")
            return
        self.bot.send_message(cid , "کاربر مورد نظر را انتخاب کنید" , reply_markup=markup)


    def change_admin_access2(self , message):
        cid = message.chat.id
        if not self.answer_customer(cid , 1):
            return

        markup = change_admin_access2_markup(self.bot)
        self.bot.send_message(cid , "کاربر مورد نظر را انتهاب کنید" , reply_markup = markup)

    def send_message_to_customer(self , message):
        cid = message.chat.id
        if not self.answer_customer(cid , 2):
            return

        markup = send_message_customer_markup()
        self.bot.send_message(cid , "یکی از گزینه های زیر را انتخاب کنید" , reply_markup = markup)


    


