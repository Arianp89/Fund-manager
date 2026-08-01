from database import *
import datetime
from handler.command import pay_installment_step , pay_installment_data 



def get_profile_text(chat_id):
    customer_id = get_id_b_admin_bot_id(chat_id)
    family_data = get_family_data_by_head_id(customer_id)
    if not family_data:
        return 
    text = f"""کد خانواده:{family_data["ID"]}
نام خانواده:{family_data["FAMILY_NAME"]}"""
    return text


def pay_installment_ser(chat_id):
    customer_list = list()
    loan_data = list()
    total = 0
    head_id = get_id_b_admin_bot_id(chat_id)
    pay_data = get_payment_data_by_customer_id(head_id)
    if not pay_data:
        family_id = get_family_data_by_head_id(head_id)["ID"]
        for all_customer in get_all_customer():
            if all_customer["FAMILY_ID"] == family_id:
                customer_id = all_customer["ID"]
                loan_id = get_loan_data_by_customer_id(customer_id)
                if not loan_id:
                    pass
                else:
                     loan_id = loan_id["ID"]
                installment_data = get_all_installment_data_by_loan_id(loan_id , "false")
                if not installment_data:
                    pass
                else:
                    for installment_data in installment_data:
                        loan_data.append(installment_data)

        pay_installment_step[chat_id] = "A"
        pay_installment_data[chat_id] = loan_data
        for loan_data in loan_data:
            loan_id = loan_data["LOAN_ID"]
            installment_amount = get_loan_data_by_id(loan_id)["INSTALLMENT_AMOUNT"]
            total += installment_amount
        cart_number = 0
        name_cart = "ali"
        text = f"""شما باید مبلغ:{total} 
        را به شماره {cart_number}            {name_cart}"""
        return [True , text]
        
    elif pay_data["PAYMENT_DATE"].strftime("%Y/%m") == datetime.datetime.now().strftime("%Y/%m"):
        text = f"""شما این ماه را پرداخت کردی"""
        return [False , text]

    else:
        family_id = get_family_data_by_head_id(head_id)["ID"]
        for all_customer in get_all_customer():
            if all_customer["FAMILY_ID"] == family_id:
                customer_id = all_customer["ID"]
                loan_id = get_loan_data_by_customer_id(customer_id)
                if not loan_id:
                    pass
                else:
                     loan_id = loan_id["ID"]
                installment_data = get_all_installment_data_by_loan_id(loan_id , "false")
                if not installment_data:
                    pass
                else:
                    for installment_data in installment_data:
                        loan_data.append(installment_data)

        pay_installment_step[chat_id] = "A"
        pay_installment_data[chat_id] = loan_data
        for loan_data in loan_data:
            loan_id = loan_data["LOAN_ID"]
            installment_amount = get_loan_data_by_id(loan_id)["INSTALLMENT_AMOUNT"]
            total += installment_amount
            cart_number = 0
            name_cart = "ali"
        text = f"""شما باید مبلغ:{total} 
        را به شماره {cart_number}            {name_cart}"""
        return [True , text]
