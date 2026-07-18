from database import get_all_family_data,get_customer_bot_id


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