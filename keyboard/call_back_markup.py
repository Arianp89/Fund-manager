from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
from database import get_all_customer,get_admin_id_b_access,get_all_family_data

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
    markup.add(InlineKeyboardButton("بعد" , callback_data=f'go_next_{page_number}_{call}') ,
               InlineKeyboardButton("قبل" , callback_data=f'go_back_{page_number}_{call}'))          
            
    if page_number == 0:
        bot.answer_callback_query(call_id , "❌")
        return False

    elif int(data_number) < int((page_number-1) * 5):
        bot.answer_callback_query(call_id , 'نمیتوان رفت به صفحه بعد') 
        return False
    return markup



def add_admin_access2_markup(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_customer() , 'add-admin' , "FULL_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup

def add_admin_access1_markup(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_customer() , 'add-access1' , "FULL_NAME" , page_number ,call_id)
    if not markup:
        return False 
    return markup

def change_admin_access2_markup(bot):
    markup = go_ba_ne(bot , get_all_customer() , 'change-admin' , "FULL_NAME")
    if not markup:
        return False
    return markup


def change_admin_access2_markup_go(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_customer() , 'change-admin' , "FULL_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup


def add_admin_markup(bot):
    if get_admin_id_b_access(2) != False:
        return False
    markup = go_ba_ne(bot , get_all_customer() , 'add-admin' , "FULL_NAME")
    return markup


def send_message_customer_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("به یک نفر" , callback_data = 'chose_customer_to_send'))
    markup.add(InlineKeyboardButton("همه" , callback_data = 'send-message-all-customer'))
    return markup


def chose_customer_to_send_message_markup(bot):
    markup = go_ba_ne(bot , get_all_family_data() , 'send-message-one' , "FAMILY_NAME")
    if not markup:
        return False
    return markup


def chose_customer_to_send_message_markup_go(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_family_data() , 'send-message-one' , "FAMILY_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup