from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
from database import get_id_b_admin_bot_id,get_admin_access,get_admin_id_b_access


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

