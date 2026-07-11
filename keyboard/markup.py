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





def go_ba_ne(bot , data , call , text , page_number=1 , call_id=None):
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
