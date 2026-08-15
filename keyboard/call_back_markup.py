from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
from database import get_family_id_by_head_id,get_customer_bot_id,get_family_data_by_id,get_customer_data_by_id,get_all_family_data_by_id,get_all_customer,get_admin_id_b_access,get_all_family_data,get_family_data_by_head_id,get_id_b_admin_bot_id
import time
from handler.command import customer_permissions,see_data_step,block_customer_command

def go_ba_ne(bot , data , call , text , page_number=1 , call_id=None):
    markup = InlineKeyboardMarkup()
    data_number = len(data)
    if data_number <= 5:
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
    family_id = get_family_id_by_head_id(head_id)
    if len(get_all_family_data_by_id(family_id)) == 1:
        markup.add(InlineKeyboardButton("مشاهده اطلاعات" , callback_data=f'see-data_{head_id}'))

    else:
        markup.add(InlineKeyboardButton("مشاهده لیست خانواده" , callback_data=f'see-family-data_{family_id}'))
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
    markup.add(InlineKeyboardButton("مشاهده اعضا" , callback_data = "see-customer-list"))
    return markup


def pay_installment_markup(head_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("افزایش سرمایه" , callback_data=f"capital-amount_{head_id}"))
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

def see_loan_list_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("مشاهده افراد پرداخت نکرده" , callback_data="see-customer-nt-pay") ,
              InlineKeyboardButton("مشاهده افراد پرداخت کرده" , callback_data="see-customer-pay")
              )
    markup.add(InlineKeyboardButton("ارسال پیام برای پرداخت" , callback_data='send-message-to-pay'))
    return markup

def see_customer_list_markup(bot):
    markup  = go_ba_ne(bot , get_all_customer() , 'see-data' ,"FULL_NAME")
    if not markup:
        return False
    return markup

def see_customer_list_markup_go(bot , page_number , call_id):
    markup  = go_ba_ne(bot , get_all_customer() , 'see-data' ,"FULL_NAME" , page_number , call_id)
    if not markup:
        return False
    return markup

def back_markup(mark , markup=None):
    if markup is None:
        markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("بازگشت به قبل" , callback_data=f'back.{mark}'))
    return markup
    

def get_customer_data_back(chat_id , customer_id):
    try:
        data = see_data_step[chat_id]
        markup = InlineKeyboardMarkup()
        if data == "see-customer-list":
            customer_data = get_customer_data_by_id(customer_id)
            if customer_data["IS_ACTIVE"] == "true":
                if  not get_customer_bot_id(get_family_data_by_id(customer_data["FAMILY_ID"])["HEAD_ID"]):
                    pass
                else:
                    markup.add(InlineKeyboardButton("غیر فعال کردن اکانت" , callback_data= f'turn-off-acount_{customer_id}') ,
                                InlineKeyboardButton('جا به جا کردن اکانت' , callback_data= f"change-bot-id_{customer_id}"))
            markup = back_markup("see-customer-list" , markup)
            return markup
        elif data.startswith("see-family-data"):
            markup = back_markup(data , markup)
            return markup
    except:
        return None
    


def turn_off_acount_makup(customer_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("تایید" , callback_data=f"block-acount_true_{customer_id}") ,
               InlineKeyboardButton("لغو" , callback_data=f"block-acount_false_{customer_id}"))
    return markup

def block_acount_markup(customer_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("تایید" , callback_data=f"block-acount_done_{customer_id}"))
    return markup

def pay_debt_A_markup(chat_id):
    _ , customer_id= block_customer_command[chat_id]
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("تایید" , callback_data=f"block-acount_done_{customer_id}") ,
               InlineKeyboardButton("لغو" , callback_data=f"block-acount_false_{customer_id}"))
    return markup

def capital_amoount_step_A_markup(cid , us = None):
    markup = InlineKeyboardMarkup()

    if us is not None:
        markup.add(InlineKeyboardButton("همه اعضا" , callback_data="capital_all"))

    return markup