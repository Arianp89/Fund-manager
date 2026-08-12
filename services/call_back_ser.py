from database import *
from handler.command import pay_installment_data,block_customer_command,capital_amount_data
import config
import datetime
import jdatetime


def change_time(dt):
    return jdatetime.datetime.fromgregorian(datetime=dt)


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
    customer_id = get_admin_id_b_access(2)
    setting_data = get_setting_data(customer_id)
    admin_id =  get_admin_id(customer_id)
    if not setting_data:
        pass
    else:
        delete_setting(admin_id)
    delete_admin(admin_id)
    add_admin(new_admin_id , 2)

def send_message_one_ser(family_id):
    family_data = get_family_data_by_id(family_id)
    head_id = family_data["HEAD_ID"]
    customer_bot_id = get_customer_bot_id(head_id)
    if not customer_bot_id:
        return None
    return customer_bot_id

def get_see_data_text(customer_id):
    customer_data = get_customer_data_by_id(customer_id)
    loan_data = get_loan_data_by_customer_id(customer_id)
    len_installment = len(get_all_installment_data_by_loan_id(loan_data["ID"] , "false"))


    if customer_data["IS_ACTIVE"] == "false":
        is_active = "غیر فعال"
        text = f"کد:{customer_data["ID"]} \n کد خانواده:{customer_data["FAMILY_ID"]} \n نام:{customer_data["FULL_NAME"]} وضعیت اکانت:{is_active}"
        
    else:
        if not loan_data:
            loan_number = "تعلق نگرفته"
            number_installmet_pay = "تعلق نگرفته"
            installment_number = "تعلق نگرفته"

        else:
            loan_number = loan_data["LOAN_AMOUNT"]
            number_installmet_pay = loan_data["NUMBER_REMAINING_INSTALLMENTS"]+len_installment
            installment_number = loan_data["INSTALLMENT_AMOUNT"]

        is_active = "فعال"
        text = f"""کد:{customer_data["ID"]}
کد خانواده:{customer_data["FAMILY_ID"]}
نام:{customer_data["FULL_NAME"]} وضعیت اکانت:{is_active}
سرمایه کل:{customer_data["TOTAL_CAPITAL"]}
مبلغ وام:{loan_number}
مبلغ قسط:{installment_number}
تعداد قسط های باقیمانده:{number_installmet_pay}"""
        
    return text


def see_family_data_admin_text(family_id):
    family_data = get_family_data_by_id(family_id)["HEAD_ID"]
    head_id = family_data["HEAD_ID"]
    pay_time = get_payment_data_by_customer_id(head_id)


def plus_capital_customer(head_id , capital_amount = None , customer_bot_id = None):
    if capital_amount is not None:
        family_id = get_family_data_by_head_id(head_id)["ID"]
        for customer_data in get_all_customer():
            if customer_data["FAMILY_ID"] == family_id:
                customer_id = customer_data["ID"]
                plus_customer_capital(customer_id  , capital_amount)
    else:
        setting_data = get_setting_data(get_admin_id_b_access(2))
        for customer_id in pay_installment_data[customer_bot_id][-1]:
            plus_customer_capital(customer_id , setting_data["CAPITAL_AMOUNT"])


def pay_installment_true_ser(chat_id):
    try:
        chat_id = int(chat_id)
        head_id = get_id_b_admin_bot_id(chat_id)
        loans_data = pay_installment_data[chat_id][0]
        total_amount = pay_installment_data[chat_id][1]
        capital_amount = get_setting_data(get_admin_id_b_access(2))["CAPITAL_AMOUNT"]
        for loan_data in loans_data:
            loan_id = loan_data["LOAN_ID"]
            plus_amount_paid(loan_id)
            change_all_installment_status(loan_id , "true")
            if get_loan_data_by_id(loan_id)["NUMBER_REMAINING_INSTALLMENTS"] == 0:
                change_loan_status(loan_id)
            if chat_id in capital_amount_data:
                capital_amount = capital_amount_data[chat_id]
            add_pay(head_id , total_amount , capital_amount , loan_id  , loan_data["ID"])
        if chat_id in capital_amount_data:
            plus_capital_customer(head_id ,capital_amount)
        plus_capital_customer(head_id , customer_bot_id=chat_id)
    except Exception as e:
        print(e)
    pay_installment_data.pop(chat_id)
    capital_amount_data.pop(chat_id)

def family_link_msg_true_ser(link_id , customer_bot_id):
    for family_data in get_all_family_data():
        family_link_id = family_data["LINK_ID"]
        if family_link_id == link_id:
            if check_is_in_db(customer_bot_id):
                new_family_id = get_customer_data_by_id(get_id_b_admin_bot_id(customer_bot_id))["FAMILY_ID"]
                old_family_id = family_data["ID"]
                change_family_id(old_family_id , new_family_id)
                delete_family(old_family_id)
            else:
                head_id = family_data['HEAD_ID']
                add_customer_bot_id(head_id , customer_bot_id)
                change_status_use_link_family(link_id)
            
def get_customer_bot_id_and_message():
    data = dict()
    for loan_data in get_all_loan_data():
        loan_id = loan_data["ID"]
        for installment in get_all_installment_data_by_id(loan_id):
            print(1)
            if installment["STATUS"] == 'false':
                family_id = get_customer_data_by_id(loan_data["CUSTOMER_ID"])["FAMILY_ID"]
                print(family_id)
                head_id = get_family_data_by_id(family_id)["HEAD_ID"]
                print(head_id)
                customer_bot_id = get_customer_bot_id(head_id)
                print(customer_bot_id)
                if customer_bot_id is None:
                    customer_bot_id = loan_data["CUSTOMER_ID"]
                if str(customer_bot_id)  in data:
                    data[str(customer_bot_id)] += loan_data["INSTALLMENT_AMOUNT"]
                else:
                    data[str(customer_bot_id)] = loan_data["INSTALLMENT_AMOUNT"]
    print(data)
    return data


def block_acount_true_ser(customer_id):
    loan_data = get_loan_data_by_customer_id(customer_id)
    customer_data = get_customer_data_by_id(customer_id)
    head_id = get_family_data_by_id(customer_data["FAMILY_ID"])["HEAD_ID"]
    customer_bot_id = get_customer_bot_id(head_id)
    customer_name = customer_data["FULL_NAME"]
    if not loan_data:
        total = customer_data["TOTAL_CAPITAL"]
        
    else:
        loan_amount = loan_data["LOAN_AMOUNT"]
        print(loan_amount)
        pay_amount = loan_data["AMOUNT_PAID"]
        print(pay_amount)
        noy_pay = loan_amount - pay_amount
        print(noy_pay)
        total_capital = customer_data["TOTAL_CAPITAL"]
        print(total_capital)
        total = total_capital - noy_pay
        print(total)

    if total > 0:
        status = "1"
        admin_text = f"شما باید مبلغ {total} را به کاربر مورد نظر پرداخت کنید و بعد از پرداخت روی تایید کلیک کنید"
        customer_text = f"ادمین درحال بستن اکانت {customer_name} است و باید مبلغ {total} را به شما پرداخت کند"
    else:
        total = - + total
        status = "0"
        admin_text = f"کاربر مورد نظر باید مبلغ {total} را برای شما واریز کنه"
        customer_text = f"ادمین در حال بستن اکانت {customer_name} است و شما برای پرداخت بدهی خود روی دکمه پرداخت بدهی کلیک کنید"
   
    block_customer_command[customer_bot_id] = [total , customer_id]
    return [customer_bot_id , admin_text , customer_text , status]


def block_acount_done_ser(customer_id):
    customer_data = get_customer_data_by_id(customer_id)
    customer_name = customer_data["FULL_NAME"]
    family_id = customer_data["FAMILY_ID"]
    head_id = get_family_data_by_id(family_id)["HEAD_ID"]
    customer_bot_id = get_customer_bot_id(head_id)
    change_customer_status(customer_id )
    loan_id = get_loan_data_by_customer_id(customer_id)
    total_amount , _ = block_customer_command[customer_bot_id]
    if not loan_id:
        add_pay(customer_id , total_amount , 0)
    else:
        loan_id = loan_id["ID"]
        loan_id = int(loan_id)
        change_loan_status_and_number(customer_id)
        change_all_installment_status(loan_id)
        add_pay(customer_id , total_amount , 0 ,loan_id)
    block_customer_command.pop(customer_bot_id)
    return [customer_name , customer_bot_id]


def change_bot_id_ser(customer_id):
    family_id = get_customer_data_by_id(customer_id)["FAMILY_ID"]
    family_data = get_family_data_by_id(family_id)
    head_id = family_data["HEAD_ID"]
    link_id = family_data["LINK_ID"]
    family_name = family_data["FAMILY_NAME"]
    customer_bot_id = get_customer_bot_id(head_id)
    change_status_use_link_family(link_id , "false")
    delete_customer_bot_id(head_id)
    text = f"""خانواده:{family_name}
لطفا برای وارد شدن به اکانت خود روی [لینک](https://web.bale.ai/chat?uid={config.bot_id}&start=family_{link_id}) کلیک کنید"""

    return [customer_bot_id , text]



import datetime

def see_customer_nt_pay_text():
    all_data = {}
    text = ""

    families = get_all_family_data()
    customers = get_all_customer()
    now = change_time(datetime.datetime.now()).strftime("%Y/%m")

    for family_data in families:
        family_id = family_data["ID"]

        for customer_data in customers:
            if customer_data["FAMILY_ID"] != family_id:
                continue

            if str(customer_data["IS_ACTIVE"]).lower() != "true":
                continue

            loan_data = get_loan_data_by_customer_id(customer_data["ID"])
            if not loan_data:
                continue

            pay_data = get_all_installment_data_by_loan_id(loan_data["ID"], "false")
            print("pay_data",pay_data)

            add_customer = False

            if not pay_data or pay_data == []:
                add_customer = False
            else:
                try:
                    for pay_data in pay_data:
                        reg_date_str = pay_data["REGISTER_DATE"]
                        if change_time(reg_date_str).strftime("%Y/%m") == now:
                            add_customer = True
                except Exception as e:
                    print(f"Error processing date for customer {customer_data['ID']}: {e}")
                    add_customer = True

            if add_customer:
                if family_id not in all_data:
                    all_data[family_id] = {
                        "family_name": family_data["FAMILY_NAME"],
                        "customer_data": []
                    }

                all_data[family_id]["customer_data"].append({
                    "id": customer_data["ID"],
                    "name": customer_data["FULL_NAME"]
                })

    if not all_data:
        return "همه پرداخت‌ها طبق برنامه انجام شده است. ✅"


    for family_id, data in all_data.items():
        text += f"کد خانواده: {family_id} | نام خانواده: {data['family_name']}\n"
        for customer in data["customer_data"]:
            text += f"  - کد: {customer['id']} | نام: {customer['name']}\n"
        text += "\n"

    return text



def see_customer_pay_text():
    all_data = {}
    text = ""

    families = get_all_family_data()
    customers = get_all_customer()
    now = change_time(datetime.datetime.now()).strftime("%Y/%m")

    for family_data in families:
        family_id = family_data["ID"]

        for customer_data in customers:
            if customer_data["FAMILY_ID"] != family_id:
                continue

            if str(customer_data["IS_ACTIVE"]).lower() != "true":
                continue

            loan_data = get_loan_data_by_customer_id(customer_data["ID"])
            if not loan_data:
                continue

            pay_data = get_all_installment_data_by_loan_id(loan_data["ID"], "true")
            print("pay_data",pay_data)

            add_customer = False

            if not pay_data or pay_data == []:
                add_customer = False
            else:
                try:
                    for pay_data in pay_data:
                        reg_date_str = pay_data["REGISTER_DATE"]
                        if change_time(reg_date_str).strftime("%Y/%m") == now:
                            add_customer = True
                except Exception as e:
                    print(f"Error processing date for customer {customer_data['ID']}: {e}")
                    add_customer = True

            if add_customer:
                if family_id not in all_data:
                    all_data[family_id] = {
                        "family_name": family_data["FAMILY_NAME"],
                        "customer_data": []
                    }

                all_data[family_id]["customer_data"].append({
                    "id": customer_data["ID"],
                    "name": customer_data["FULL_NAME"]
                })

    if not all_data:
        return "همه پرداخت‌ها طبق برنامه انجام نشده است. ✅"


    for family_id, data in all_data.items():
        text += f"کد خانواده: {family_id} | نام خانواده: {data['family_name']}\n"
        for customer in data["customer_data"]:
            text += f"  - کد: {customer['id']} | نام: {customer['name']}\n"
        text += "\n"

    return text


def block_acount_false_ser(customer_id):
    family_id = get_customer_data_by_id(customer_id)["FAMILY_ID"]
    head_id = get_family_data_by_id(family_id)["HEAD_ID"]
    customer_bot_id = get_customer_bot_id(head_id)
    return customer_bot_id

def capital_text(chat_id):
    _ , total_amount  , customer_number , _= pay_installment_data[chat_id]
    print(total_amount)
    capital_number = capital_amount_data[chat_id]
    print(capital_number)
    setting_data = get_setting_data(get_admin_id_b_access(2))
    cart_number = setting_data["CART_NUMBER"]
    name_cart = setting_data["CART_NAME"]
    total_amount += capital_number
    print(total_amount)
    text = f"""شما باید مبلغ:{total_amount} 
را به شماره {cart_number}   {name_cart}
پرداخت کنید و عکس فیش پرداختی را ارسال کنید
اگر افزایش سرمایه دارید روی دکمه پایین کلیک کنید"""
    capital_number = int(capital_number / customer_number)
    print(capital_number)
    capital_amount_data[chat_id] = capital_number
    return text