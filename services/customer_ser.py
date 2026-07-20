from database import *




def get_profile_text(chat_id):
    customer_id = get_id_b_admin_bot_id(chat_id)
    family_data = get_family_data_by_head_id(customer_id)
    if not family_data:
        return 
    text = f"""کد خانواده:{family_data["ID"]}
نام خانواده:{family_data["FAMILY_NAME"]}"""
    return text