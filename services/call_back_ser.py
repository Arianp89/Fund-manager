from database import *
from keyboard.markup import go_ba_ne


def access_1_ser(customer_id , chat_id):
    add_admin(customer_id)
    add_customer_bot_id(customer_id , int(chat_id))



def add_admin_call(bot , page_number , call_id):
    markup = go_ba_ne(bot , get_all_customer() , 'add-admin' , "FULL_NAME" , page_number , call_id)
    return markup


def add_admin_access2_call(customer_id ):
    add_admin(customer_id , 2)
    bot_id = get_customer_bot_id(customer_id)
    if bot_id is None:
        return [False]
    return [True , bot_id]
