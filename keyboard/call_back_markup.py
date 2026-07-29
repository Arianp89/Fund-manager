from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
from database import get_all_family_data_by_id,get_all_customer,get_admin_id_b_access,get_all_family_data,get_family_data_by_head_id,get_id_b_admin_bot_id
import time
from handler.command import customer_permissions
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
    markup = go_ba_ne(bot , get_all_family_data() , 'add-admin' , "FAMILY_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup

def add_admin_access1_markup(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_family_data() , 'add-access1' , "FAMILY_NAME" , page_number ,call_id)
    if not markup:
        return False 
    return markup

def change_admin_access2_markup(bot):
    markup = go_ba_ne(bot , get_all_family_data() , 'change-admin' , "FAMILY_NAME")
    if not markup:
        return False
    return markup


def change_admin_access2_markup_go(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_customer() , 'change-admin' , "FULL_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup


def add_admin_access2_markup(bot):
    if get_admin_id_b_access(2) != False:
        return False
    markup = go_ba_ne(bot , get_all_family_data() , 'add-admin' , "FAMILY_NAME")
    return markup


def send_message_to_customer_markup():
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


def send_message_admin_markup(customer_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("خوانده شده" , callback_data = f'see-message_{customer_id}') ,
               InlineKeyboardButton("نادیده گرفتن" , callback_data=f'not-answer'))
    markup.add(InlineKeyboardButton("پاسخ دادن" , callback_data = f'answer-message_{customer_id}'))
    return markup

def profile_markup(chat_id):
    markup = InlineKeyboardMarkup()
    head_id = get_id_b_admin_bot_id(chat_id)
    family_id = get_family_data_by_head_id(head_id)["ID"]
    if len(get_all_family_data_by_id(family_id)) == 1:
        markup.add(InlineKeyboardButton("مشاهده اطلاعات" , callback_data=f'see-data_{head_id}'))

    else:
        markup.add(InlineKeyboardButton("مشاهده لیست خانواده" , callback_data=f'see-family-data_{family_id}'))
        print("انجام شود")
    # check_time = time.time()-customer_permissions[chat_id]["time"] > 3600*24
    # if customer_permissions[chat_id]["change_bot_id"] == "true" and check_time <= 3600*24:
    #     markup.add(InlineKeyboardButton("تغییر ادرس ربات" , callback_data=f'change-bot-id_{family_id}'))
    return markup

def see_family_markup(bot , family_id):
    markup  = go_ba_ne(bot , get_all_family_data_by_id(family_id) , 'see-data' ,"FULL_NAME" )
    if not markup:
        return False
    return markup
        
def see_family_data_markup_go(bot , family_id , page_number , call_id):
    markup  = go_ba_ne(bot , get_all_family_data_by_id(family_id) , 'see-data' ,"FULL_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup

def get_family_markup(bot):
    markup  = go_ba_ne(bot , get_all_family_data() , 'get-family-member-list' ,"FAMILY_NAME")
    if not markup:
        return False
    return markup

def get_family_list_markup_go(bot , page_number , call_id):
    markup  = go_ba_ne(bot , get_all_family_data() , 'admin-see-family-data' ,"FAMILY_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup

def admin_see_family_list():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("مشاهده لیست خانواده" , callback_data = "admin-see-family-list"))
    return markup


def pay_installment_markup(head_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("افزایش سرمایه" , callback_data=f"amount_{head_id}"))
    return markup


def check_pay_admin_markup(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("تایید" , callback_data=f"pay-installment_true_{chat_id}") ,
               InlineKeyboardButton("لغو" , callback_data=f"pay-installment_false_{chat_id}"))
    return markup


def message_link_family_markup(customer_id , link_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("تایید" , callback_data=f"family-link-msg_true_{link_id}_{customer_id}") ,
               InlineKeyboardButton("لغو" , callback_data=f"family-link-msg_false_{link_id}_{customer_id}"))
    return markup