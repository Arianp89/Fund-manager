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



