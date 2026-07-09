# from database.DQL import *
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
import telebot 
import config
import os
import shutil
from database import *
from backup.information_database_improved import DatabaseManager





#--------------------------------------------------------------------
telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}' 
bot=telebot.TeleBot(config.API_TOKEN)

#==========================================================================



def check_is_in_db(chat_id):
    if not get_id_b_admin_bot_id(chat_id):
        return False
    return True




def go_ba_ne(data , call , text , page_number=1 , call_id=None):
    markup = InlineKeyboardMarkup()
    data_number = len(data)
    if data_number == 5:
        for da in data:
            markup.add(InlineKeyboardButton(da[text] ,
                                            callback_data=f'{call}_{da["ID"]}'))
        return markup
    

    for da in data[(page_number -1)*5:page_number*5]:
        markup.add(InlineKeyboardButton(da[text] ,
                                            callback_data=f'{call}_{da["ID"]}'))
    markup.add(InlineKeyboardButton("بعد" , callback_data=f'go_next_{page_number}') ,
               InlineKeyboardButton("قبل" , callback_data=f'go_back_{page_number}'))          
            
    if page_number == 0:
        bot.answer_callback_query(call_id , "❌")
        return False

    elif int(data_number) < int((page_number-1) * 5):
        bot.answer_callback_query(call_id , 'نمیتوان رفت به صفحه بعد') 
        return False
        
    return markup

            

def check_admin(admin_id , for_='all'):
    bot_id_list = list()
    for customer_id in get_admin_list():
        bot_id = get_customer_bot_id(customer_id)
        bot_id_list.append(bot_id)
    if admin_id not in bot_id_list:
        if for_ == 'all':
            text = "✖دستور یافت نشد,دوباره تلاش کنید"
        else:
            text = "سلام کاربر"
        bot.send_message(admin_id , text , reply_markup=customer_markup())
        return False
    return True
        





def get_backup_func(message):
    cid = message.chat.id
    manager = DatabaseManager(db_config , database_name)
    manager.set_language('en')
    manager.export_to_file()
    shutil.make_archive('backup' , 'zip' , 'database_data')
    with open('backup.zip' , 'rb') as f:
        text = "فایل [(backup)](github.com/arianp89/database-data-mover)"
        bot.send_document(cid , f ,caption= text, parse_mode='Markdown')