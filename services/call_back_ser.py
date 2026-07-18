from database import *


def access_1_ser(customer_id , chat_id):
    add_admin(customer_id)
    add_customer_bot_id(customer_id , int(chat_id))



def add_admin_access2_call(customer_id ):
    add_admin(customer_id , 2)
    bot_id = get_customer_bot_id(customer_id)
    if bot_id is None:
        return [False]
    return [True , bot_id]

def change_admin_access2_ser(id):
    customer_id = get_admin_id_b_access(2)
    setting_data = get_setting_data(customer_id)
    admin_id =  get_admin_id(customer_id)
    if not setting_data:
        pass
    else:
        delete_setting(admin_id)
    delete_admin(admin_id)
    add_admin(id , 2)
    return True

def send_message_one_ser(family_id):
    family_data = get_family_data_by_id(family_id)
    head_id = family_data["HEAD_ID"]
    customer_bot_id = get_customer_bot_id(head_id)
    if not customer_bot_id:
        return None
    return customer_bot_id