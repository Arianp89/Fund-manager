from database import get_family_data,get_all_family_id,get_all_customer,get_admin_list,get_admin_id_b_access,get_customer_bot_id
from config import bot_id
from database import *
from keyboard.call_back_markup import go_ba_ne
import datetime



def add_family_link_text():
    text_list = list()
    for id in get_all_family_id():
        family_data = get_family_data_by_id(id)
        link_id = family_data['LINK_ID']
        family_name = family_data['FAMILY_NAME']
        text = f"""خانواده:{family_name}
لطفا برای وارد شدن به اکانت خود روی [لینک](https://web.bale.ai/chat?uid={bot_id}&start=family_{link_id}) کلیک کنید"""
        text_list.append(text)

    return text_list



def admin_see_customer_text():
    all_customer_number = 0
    number_customer_active = 0
    number_customer_nt_active = 0
    customer_data = get_all_customer()
    family_number =len( get_all_family_data())
    for data in customer_data:
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
        
def see_loan_list_text():
    total_loan = 0
    total_installment_not_pay = 0
    total_installment_pay = 0
    for loan_data in get_all_loan_data():
        if loan_data["STATUS"] == "false":
            total_loan += 1
            loan_id = loan_data["ID"]
            now = datetime.datetime.now().strftime("%Y/%m")
            for installment_data in get_all_installment_data_by_id(loan_id):
                if installment_data["REGISTER_DATE"].strftime("%Y/%m") == now:
                    if installment_data["STATUS"] == 'true':
                        total_installment_pay += 1
                    else:
                        total_installment_not_pay += 1

    text = f"""تعداد وام ها:{total_loan}
تعداد اقساط پرداخت شده:{total_installment_pay}
تعداد اقساط پرداخت نشده:{total_installment_not_pay}
"""
    return text


