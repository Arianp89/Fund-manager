from DQL import *
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
import telebot 
import config
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

admin_step_add_admin = dict()



#___________________________________FUN_______________________________


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
        bot.send_message(admin_id , text)
        return False
    return True
        


def start_fun(message):
    cid = message.chat.id
    if check_admin(cid , 'start'):
        bot.send_message(cid , 'سلام ادمین')


def help_fun(message):
    cid = message.chat.id
    text = 'help \n'
    for com , about in commands.items():
        text += f"/{com}     {about} \n"
    bot.send_message(cid , text)

def add_admin_access1_fun(message):
    cid = message.chat.id
    if get_admin_list() == []:
        admin_step_add_admin[cid] = 'A'
        bot.send_message(cid , 'نام و نام  خانوادگی خود را وارد کنید:')



def add_admin_access1_fun_step_A(message):
    cid = message.chat.id
    data = message.text
    first_name , last_name = data.split()
    admin_data = get_customer_data_b_fn_ln(first_name , last_name)
    if not admin_data:
        bot.send_message(cid , 'همچین کاربری وجود ندارد')
        return
    admin_id = int( admin_data['ID'])
    add_customer_bot_id(admin_id , int(cid))
    add_admin_access1(admin_id)

