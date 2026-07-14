from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
# from database import get_id_b_admin_bot_id,get_admin_access,get_admin_id_b_access
from database import *



def customer_markup(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("پرداخت قسط" , "مشاهده اطلاعات وام")
    markup.add("پروفایل")
    markup.add("ارسال پیام" , "راهنمای استفاده")
    if check_admin(chat_id) == 'admin':
        markup.add("وارد شدن به پنل ادمین")
    return markup


def admin_markup(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_id = get_id_b_admin_bot_id(chat_id)
    admin_access = get_admin_access(admin_id)
    if admin_access == 1:
        markup.add("گرفتن بکآپ")
        if not get_admin_id_b_access(2):
            markup.add("اضافه کردن ادمین" , "دریافت لینک")
        else:
            markup.add("تغییر ادمین" , "دریافت لینک")
    elif admin_access == 2:
        markup.add("مشاهده کاربران")
        markup.add("مشاهده لیست اقساط")

    markup.add("وارد شدن به پنل کاربر")
    return markup

