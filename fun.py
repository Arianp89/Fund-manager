from DQL import *
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
import telebot 
import config
import os
from DML import *

#--------------------------------------------------------------------

telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}' 
bot=telebot.TeleBot(config.API_TOKEN)

#___________________________________COMMAND_______________________________

password_get_access1 = "Ad1fWQ89Gg"

commands = {"start" : "شروع" ,
            "help" : "مشاهده دستورات " ,
            "get_backup" : "گرفتن بکآپ" ,
            "get_access1" : "دادن دسترسی به فرد دیگه" ,
            }

#==========================================================================




#___________________________________FUNC__________________________________
def check_is_in_db(chat_id):
    if not get_id_b_admin_bot_id(chat_id):
        return False
    return True
#==================================MARKUPS================================

def customer_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("پرداخت قسط" , "مشاهده اطلاعات وام")
    markup.add("پروفایل")
    markup.add("ارسال پیام" , "راهنمای استفاده")
    return markup

def admin_markup(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_id = get_id_b_admin_bot_id(chat_id)
    admin_access = get_admin_access(admin_id)
    if admin_access == 1:
        markup.add("گرفتن بکآپ")
        markup.add("مشاهده کاربران" , "دریافت لینک")
        if not get_admin_id_b_access(2):
            markup.add("اضافه کردن ادمین")
        else:
            markup.add("تغییر ادمین")
    elif admin_access == 2:
        markup.add("مشاهده کاربران")
        markup.add("مشاهده لیست اقساط")
    return markup

def go_ba_ne(data , call , text , page_number=1):
    markup = InlineKeyboardMarkup()
    if len(data) == 5:
        for da in data:
            markup.add(InlineKeyboardButton(da[text] ,
                                            callback_data=f'{call}_{da["ID"]}'))
        return markup

    for da in data[(page_number -1)*5:page_number*5]:
        markup.add(InlineKeyboardButton(da[text] ,
                                            callback_data=f'{call}_{da["ID"]}'))
    markup.add(InlineKeyboardButton('⏭' , callback_data=f'go_next_{page_number}') ,
               InlineKeyboardButton('🔙' , callback_data=f'go_back_{page_number}'))                  
        
    return markup

def family_link(message , status='get'):
    cid = message.chat.id

    if status == "get":
        if len(message.text.split()) > 1:
            family_id = int(message.text.split('_')[-1])
            family_data = get_family_data(family_id)
            if family_data is  None:
                return
            head_id = family_data['HEAD_ID']
            add_customer_bot_id(head_id , cid)
            bot.send_message(cid , 'سلام')

    else:
        for id in get_all_family_id():
            text = f'کاربر {get_family_data(id)['FAMILY_NAME']} \n'
            text += " کلیک کنید ."+ f" [لینک](https://web.bale.ai/chat?uid={os.environ.get("bot_cid")}&start=family_{id}) " + "لطفا روی "
            bot.send_message(cid , text)

            

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
        


def start_fun(message):
    cid = message.chat.id
    family_link(message)

    if not check_is_in_db(cid):
        return
    if check_admin(cid , 'start'):
        bot.send_message(cid , 'سلام ادمین' , reply_markup=admin_markup(cid))


def help_fun(message):
    cid = message.chat.id
    if not check_is_in_db(cid):
        return
    text = 'help \n'
    for com , about in commands.items():
        text += f"/{com}     {about} \n"
    bot.send_message(cid , text)

def add_admin_access1_fun(message):
    cid = message.chat.id
    markup = go_ba_ne(get_all_customer() , 'add-access1' , "FULL_NAME")
    if get_admin_list() == []:
        bot.send_message(cid , 'انتخاب کنید' , reply_markup=markup)



def get_link_func(message):
    cid = message.chat.id
    family_link(message , 'make_link')



