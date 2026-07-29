from database import *
from handler.command import pay_installment_data

def access_1_ser(family_id , chat_id):
    customer_id = get_family_data_by_id(family_id)["HEAD_ID"]
    link_id = get_family_data_by_id(family_id)["LINK_ID"]
    change_status_use_link_family(link_id)
    add_admin(customer_id)
    add_customer_bot_id(customer_id , int(chat_id))



def add_admin_access2_call(family_id ):
    customer_id = get_family_data_by_id(family_id)["HEAD_ID"]
    add_admin(customer_id , 2)
    bot_id = get_customer_bot_id(customer_id)
    if bot_id is None:
        return [False]
    return [True , bot_id]

def change_admin_access2_ser(family_id):
    new_admin_id = get_family_data_by_id(family_id)["HEAD_ID"]
    print(new_admin_id)
    customer_id = get_admin_id_b_access(2)
    setting_data = get_setting_data(customer_id)
    admin_id =  get_admin_id(customer_id)
    if not setting_data:
        pass
    else:
        delete_setting(admin_id)
    delete_admin(admin_id)
    add_admin(new_admin_id , 2)
    return True

def send_message_one_ser(family_id):
    family_data = get_family_data_by_id(family_id)
    head_id = family_data["HEAD_ID"]
    customer_bot_id = get_customer_bot_id(head_id)
    if not customer_bot_id:
        return None
    return customer_bot_id

def get_see_data_text(customer_id):
    print(get_loan_data_by_customer_id(customer_id))
    customer_data = get_customer_data_by_id(customer_id)
    loan_data = get_loan_data_by_customer_id(customer_id)


    if customer_data["IS_ACTIVE"] == "false":
        is_active = "غیر فعال"
        text = f"کد:{customer_data["ID"]} \n نام:{customer_data["FULL_NAME"]} وضعیت اکانت:{is_active}"
        
    else:
        if not loan_data:
            loan_number = "تعلق نگرفته"
            number_installmet_pay = "تعلق نگرفته"

        else:
            loan_number = loan_data["LOAN_AMOUNT"]
            number_installmet_pay = loan_data["NUMBER_REMAINING_INSTALLMENTS"]

        is_active = "فعال"
        text = f"""کد:{customer_data["ID"]}
نام:{customer_data["FULL_NAME"]} سرمایه کل:{customer_data["TOTAL_CAPITAL"]}
وضعیت اکانت:{is_active}
مبلغ وام:{loan_number}
تعداد قسط های باقیمانده:{number_installmet_pay}"""
        
    return text


def see_family_data_admin_text(family_id):
    family_data = get_family_data_by_id(family_id)["HEAD_ID"]
    head_id = family_data["HEAD_ID"]
    pay_time = get_payment_data_by_customer_id(head_id)


def pay_installment_true_ser(chat_id):
    chat_id = int(chat_id)
    head_id = get_id_b_admin_bot_id(chat_id)
    print(pay_installment_data)
    loans_data = pay_installment_data[chat_id]
    for loan_data in loans_data:
        loan_id = loan_data["LOAN_ID"]
        change_loan_number(loan_id)
        add_pay(loan_id , head_id , 5)


def family_link_msg_true_ser(link_id , customer_bot_id):
    for family_data in get_all_family_data():
        family_link_id = family_data["LINK_ID"]
        if family_link_id == link_id:
            add_customer_bot_id(family_data["HEAD_ID"] , customer_bot_id)
            change_status_use_link_family(link_id)
            
def get_customer_bot_id_and_message():
    data = dict()
    for loan_data in get_all_loan_data():
        loan_id = loan_data["ID"]
        for installment in get_all_installment_data_by_id(loan_id):
            if installment["STATUS"] == 'false':
                customer_bot_id = get_customer_bot_id(loan_data["CUSTOMER_ID"])
                if loan_data["CUSTOMER_ID"]  in data:
                    data[str(customer_bot_id)] += loan_data["INSTALLMENT_AMOUNT"]
                else:
                    data[str(customer_bot_id)] = loan_data["INSTALLMENT_AMOUNT"]
    return data
