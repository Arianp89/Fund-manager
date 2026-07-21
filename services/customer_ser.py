from database import *




def get_profile_text(chat_id):
    customer_id = get_id_b_admin_bot_id(chat_id)
    family_data = get_family_data_by_head_id(customer_id)
    if not family_data:
        return 
    text = f"""کد خانواده:{family_data["ID"]}
نام خانواده:{family_data["FAMILY_NAME"]}"""
    return text


# def see_month_data_text(chat_id):
#     customer_id = get_id_b_admin_bot_id(chat_id)
#     family_id = get_customer_data_by_id(customer_id)["FAMILY_ID"]
#     payment_data = get_payment_data_by_customer_id(customer_id)
#     family_data = get_family_data_by_id(family_id)
#     installment_number = 0
#     for data in family_data:
#         id = data["ID"]
#         loan_id = get_loan_id_by_customer_id(id)
#         installment_number += len(get_all_installment_data_by_loan_id(loan_id))

#     if installment_number == 0:
#         pay_status = "پرداخت شده"
    
#     elif installment_number == 1*len(family_id):
#         pay_status = "پرداخت نشده"
    
#     elif installment_number > 1*len(family_id):
#         pay_status = installment_number/len(family_id) + "قسط پرداخت نشده"

#     text = f"""مبلغ پرداختی:{payment_data["AMOUNT_PAID"]}
# مبلغ افزایش سرمایه کل:{payment_data["CAPITAL_INCREASE"]}
# وضعیت پرداختی:{pay_status}"""
#     if pay_status == "پرداخت شده":
        