from database import get_id_b_admin_bot_id,get_all_family_data,get_customer_bot_id,get_admin_id_b_access,get_customer_data_by_id
from handler.command import pay_installment_data

def get_all_family_bot_id():
    bot_list = list()
    all_family_data = get_all_family_data()
    print(all_family_data)
    print('okkk')

    for data in all_family_data:
        print(data)
        head_id = data["HEAD_ID"]
        bot_id = get_customer_bot_id(head_id)
        print(bot_id)
        if bot_id is not None:
            bot_list.append(bot_id)

    print(bot_list)
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
    total_pay_number = pay_installment_data[chat_id]
    text = f"""کاربر:{customer_name}
باید مبلغ:{total_pay_number} را واریز میکرد
"""
    return[text , admin_id]