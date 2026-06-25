from DQL import *
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
import telebot 
import config

#--------------------------------------------------------------------

telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}' 
bot=telebot.TeleBot(config.API_TOKEN)


#___________________________________FUN_______________________________


def check_admin(admin_id , for_='all'):
    if admin_id not in get_admin_list():
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
