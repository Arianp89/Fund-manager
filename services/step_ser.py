from database import get_all_family_data,get_customer_bot_id,get_admin_id_b_access


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

    return bot_list






def send_message_admin_ser(chat_id):
    admin_id = get_admin_id_b_access(2)
    admin_bot_id = get_customer_bot_id(admin_id)
    return admin_bot_id
