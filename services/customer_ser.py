from database import *
import datetime
from handler.command import pay_installment_step , pay_installment_data 
import jdatetime



def change_time(dt):
    return jdatetime.datetime.fromgregorian(datetime=dt)


def get_profile_text(chat_id):
    customer_id = get_id_b_admin_bot_id(chat_id)
    family_data = get_family_data_by_head_id(customer_id)
    if not family_data:
        return 
    text = f"""کد خانواده:{family_data["ID"]}
نام خانواده:{family_data["FAMILY_NAME"]}"""
    return text


def have_loan(head_id):
    number = 0
    family_id = get_family_data_by_head_id(head_id)["ID"]
    for customer_data in get_all_customer():
        if customer_data["FAMILY_ID"] == family_id:
            customer_id = customer_data["ID"]
            loan_data = get_loan_data_by_customer_id(customer_id)
            if not loan_data:
                pass
            elif loan_data["STATUS"] == "true":
                pass
            else:
                number += 1
    print(number)
    if number == 0:
        return False
    return True


def pay_installment_ser(chat_id):
    data = list()
    customer_list = list()
    customer_number = 0
    total = 0
    head_id = get_id_b_admin_bot_id(chat_id)
    pay_data = get_payment_data_by_customer_id(head_id)
    

    if not have_loan(head_id):
        text = "وامی به خانواده تعلق نگرفته"
        return [False , text]


    elif not pay_data:
        family_id = get_family_data_by_head_id(head_id)["ID"]
        for all_customer in get_all_customer():
            if all_customer["FAMILY_ID"] == family_id:
                customer_id = all_customer["ID"]
                customer_number += 1
                loan_id = get_loan_data_by_customer_id(customer_id)
                if not loan_id or loan_id["STATUS"] == "true":
                    continue
                else:
                    loan_id = loan_id["ID"]
                    installment_data = get_all_installment_data_by_loan_id(loan_id , "false")
                    for installment_data in installment_data:
                        data.append(installment_data)
                        customer_list.append(get_loan_data_by_id(installment_data["LOAN_ID"])["CUSTOMER_ID"])

        pay_installment_step[chat_id] = "A"
        for loan_data in data:
            loan_id = loan_data["LOAN_ID"]
            installment_amount = get_loan_data_by_id(loan_id)["INSTALLMENT_AMOUNT"]
            print("installment_amount",installment_amount)
            total += installment_amount

        for customer_data in get_all_customer():
            if customer_data["FAMILY_ID"] == family_id:
                if customer_data["ID"] not in customer_list:
                    customer_list.append(customer_data["ID"])
        
        print(data)
        setting_data = get_setting_data(get_admin_id_b_access(2))
        cart_number = setting_data["CART_NUMBER"]
        name_cart = setting_data["CART_NAME"]
        capital_amount = setting_data["CAPITAL_AMOUNT"]
        total += len(customer_list)*capital_amount
        pay_installment_data[chat_id] = [data, total , customer_number , customer_list]
        text = f"""شما باید مبلغ:{total} 
را به شماره {cart_number}   {name_cart}
پرداخت کنید و عکس فیش پرداختی را ارسال کنید
اگر افزایش سرمایه دارید روی دکمه پایین کلیک کنید"""
        return [True , text]
        
    elif change_time(pay_data["PAYMENT_DATE"]).strftime("%Y/%m") == change_time(datetime.datetime.now()).strftime("%Y/%m"):
        text = f"""شما این ماه را پرداخت کردی"""
        change_time(pay_data["PAYMENT_DATE"]).strftime("%Y/%m")
        return [False , text]
    

    else:
        family_id = get_family_data_by_head_id(head_id)["ID"]
        for all_customer in get_all_customer():
            if all_customer["FAMILY_ID"] == family_id:
                customer_id = all_customer["ID"]
                customer_number += 1
                loan_id = get_loan_data_by_customer_id(customer_id)
                if not loan_id or loan_id["STATUS"] == "true":
                    continue
                else:
                    loan_id = loan_id["ID"]
                    installment_data = get_all_installment_data_by_loan_id(loan_id , "false")
                    for installment_data in installment_data:
                        data.append(installment_data)
                        customer_list.append(get_loan_data_by_id(installment_data["LOAN_ID"])["CUSTOMER_ID"])

        pay_installment_step[chat_id] = "A"
        for loan_data in data:
            loan_id = loan_data["LOAN_ID"]
            installment_amount = get_loan_data_by_id(loan_id)["INSTALLMENT_AMOUNT"]
            print("installment_amount",installment_amount)
            total += installment_amount

        for customer_data in get_all_customer():
            if customer_data["FAMILY_ID"] == family_id:
                if customer_data["ID"] not in customer_list:
                    customer_list.append(customer_data["ID"])
        
        print(data)
        setting_data = get_setting_data(get_admin_id_b_access(2))
        cart_number = setting_data["CART_NUMBER"]
        name_cart = setting_data["CART_NAME"]
        capital_amount = setting_data["CAPITAL_AMOUNT"]
        total += len(customer_list)*capital_amount
        pay_installment_data[chat_id] = [data, total , customer_number , customer_list]
        text = f"""شما باید مبلغ:{total} 
را به شماره {cart_number}   {name_cart}
پرداخت کنید و عکس فیش پرداختی را ارسال کنید
اگر افزایش سرمایه دارید روی دکمه پایین کلیک کنید"""
        return [True , text]
