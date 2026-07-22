from database import get_all_family_data,get_family_link_status,change_status_use_link_family,check_admin,check_is_in_db,get_family_data,add_customer_bot_id,get_all_customer,get_admin_list,get_admin_id_b_access,get_customer_bot_id
from handler.command import *
from keyboard.call_back_markup import go_ba_ne 


def start_ser(chat_id):
    if not check_is_in_db(chat_id):
        return None

    elif check_admin(chat_id) == "admin":
        return True
    return False



def get_family_link_ser(family_id , chat_id):
    family_data = get_family_data(family_id)
    if family_data is  None:
        return None
    if not get_family_link_status(family_id):
        return False
    head_id = family_data['HEAD_ID']
    add_customer_bot_id(head_id , chat_id)
    change_status_use_link_family(family_id)
    return True

def help_ser(chat_id):
    if not check_is_in_db(chat_id):
        return None
    text = 'help \n'
    for com , about in command.items():
        text += f"/{com}     {about} \n"

    return text



def add_admin_access1_ser(bot):
    markup = go_ba_ne(bot , get_all_family_data() , 'add-access1' , "FAMILY_NAME")
    if get_admin_list() != []:
        admin_id = get_admin_id_b_access(1)
        admin_bot_id = get_customer_bot_id(admin_id)
        return [None , admin_bot_id]
    return markup