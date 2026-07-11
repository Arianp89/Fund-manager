from database import get_family_data,add_customer_bot_id,get_all_family_id
from config import bot_id




def make_family_link_ser():
    text_list = list()
    for id in get_all_family_id():
        text = f'کاربر {get_family_data(id)['FAMILY_NAME']} \n'
        text += " کلیک کنید ."+ f" [لینک](https://web.bale.ai/chat?uid={bot_id}&start=family_{id}) " + "لطفا روی "
        text_list.append(text)

    return text_list

