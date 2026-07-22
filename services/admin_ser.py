from database import get_family_data,get_all_family_id,get_all_customer,get_admin_list,get_admin_id_b_access,get_customer_bot_id
from config import bot_id
from database import *
from keyboard.call_back_markup import go_ba_ne



def add_family_link_text():
    text_list = list()
    for id in get_all_family_id():
        family_data = get_family_data_by_id(id)
        link_id = family_data['LINK_ID']
        family_name = family_data['FAMILY_NAME']
        text = f'کاربر {family_name} \n'
        text += " کلیک کنید ."+ f" [لینک](https://web.bale.ai/chat?uid={bot_id}&start=family_{link_id}) " + "لطفا روی "
        text_list.append(text)

    return text_list



def admin_see_customer_text():
    all_customer_number = 0
    number_customer_active = 0
    number_customer_nt_active = 0
    customer_data = get_all_customer()
    family_number =len( get_all_family_data())
    for data in customer_data:
        print(data)
        status = data['IS_ACTIVE']
        if status == "true":
            number_customer_active += 1 
        else:
            number_customer_nt_active += 1
        all_customer_number += 1
    
    text = f"""تعداد خانواده ها:{family_number}
تعداد اعضای فعال:{number_customer_active}
تعداد اعضای غیر فعال:{number_customer_nt_active}
تعداد کل اعضای:{all_customer_number}
"""
    return text
        



