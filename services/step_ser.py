from database import add_family_data,add_customer,add_family,get_id_b_admin_bot_id,get_all_family_data,get_customer_bot_id,get_admin_id_b_access,get_customer_data_by_id
from handler.command import add_new_customer_data,pay_installment_data,block_customer_command
import random
import string



def get_all_family_bot_id():
    bot_list = list()
    all_family_data = get_all_family_data()


    for data in all_family_data:
        head_id = data["HEAD_ID"]
        bot_id = get_customer_bot_id(head_id)
        if bot_id is not None:
            bot_list.append(bot_id)

    return bot_list






def send_message_admin_ser(chat_id):
    admin_id = get_admin_id_b_access(2)
    admin_bot_id = get_customer_bot_id(admin_id)
    return admin_bot_id


def pay_installment_A_text_and_admin_id(chat_id):
    admin_id = get_admin_id_b_access(2)
    admin_id = get_customer_bot_id(admin_id)
    customer_id = get_id_b_admin_bot_id(chat_id)
    customer_data = get_customer_data_by_id(customer_id)
    customer_name = customer_data["FULL_NAME"]
    total_pay_number = pay_installment_data[chat_id][1]
    text = f"""کاربر:{customer_name}
باید مبلغ:{total_pay_number} را واریز میکرد
"""
    return[text , admin_id]


def add_new_customer_step_B_ser(chat_id):
    try:
        requence=string.ascii_lowercase + string.ascii_uppercase + string.digits
        link_id = str(''.join(random.choices(requence,k=6)))
        family_id = add_family(link_id)
        customer_data = add_new_customer_data[chat_id]
        customer_name =  customer_data["name"]
        customer_amount = customer_data["amount"]
        head_id = add_customer(family_id , customer_name , customer_amount)
        add_family_data(family_id , head_id , customer_name )
    except Exception as e:
        print(e)
        return False
    return link_id


def pay_debt_A_text(customer_bot_id):
    _ , customer_id = block_customer_command[customer_bot_id]
    customer_data = get_customer_data_by_id(customer_id)
    admin_id = get_admin_id_b_access(2)
    admin_bot_id = get_customer_bot_id(admin_id)
    total_amount , customer_id = block_customer_command[customer_bot_id]
    customer_name = customer_data["FULL_NAME"]
    text = f"""کابر {customer_name} 
باید مبلغ {total_amount} را واریز میکرد.
"""
    return [text , admin_bot_id]
    