from .command import see_data_step
from .command import *
from database import *
import jdatetime
import logging
import time

def get_ziro():
    while True:
        customer_step_send_message.clear()
        customer_data_send_message.clear()
        admin_step_send_messsage.clear()
        block_customer_command.clear()
        add_new_customer_step.clear()
        add_new_customer_data.clear()
        send_message_one_data.clear()
        customer_permissions.clear()
        pay_installment_step.clear()
        pay_installment_data.clear()
        capital_amount_data.clear()
        see_data_step.clear()
        pay_debt_step.clear()
        setting_step.clear()
        setting_data.clear()
        logging.info("run get_ziro")
        time.sleep(3600*24)

def change_time(dt):
    return jdatetime.datetime.fromgregorian(datetime=dt)

def add_loan_and_installment(bot):
    while True:
        total_amount = 0
        total_pay = 0
        time_data = get_time()
        now = jdatetime.datetime.now()
        if time_data is None:
            add_time("true")
            time_data = get_time()
        if now.day == 22 and change_time(time_data["TIME"]).strftime("%Y/%m") != now.strftime("%Y/%m"):
            add_time()
            time_data = get_time()

        if change_time(time_data["TIME"]).strftime("%Y/%m") == now.strftime("%Y/%m"):
            setting_data = get_setting_data(get_admin_id_b_access(2))
            if time_data["USE_TIME"] == "false":
                for customer_data in get_all_customer():
                    if customer_data["IS_ACTIVE"] == "true": 
                        total_amount += customer_data["TOTAL_CAPITAL"] 


                for customer_data in get_all_customer():
                    if customer_data["IS_ACTIVE"] == "false":
                        continue
                    customer_id = customer_data["ID"]
                    loan_data = get_loan_data_by_customer_id(customer_id)
                    if not loan_data or loan_data["STATUS"] == "true":
                        loan_amount = customer_data["TOTAL_CAPITAL"]*2.5
                        if loan_amount > 300000000:
                            loan_amount = 300000000
                        total_pay += loan_amount
                        if total_amount < total_pay or not setting_data:
                            break
                        installment_number = setting_data["INSTALLMENT_NUMBER"]
                        add_loan_data(customer_id , loan_amount , loan_amount/installment_number , installment_number , 0 , "false")
                        family_name = get_family_data_by_id(customer_data["FAMILY_ID"])["FAMILY_NAME"]
                        bot.send_message(get_customer_bot_id(get_admin_id_b_access(2)) , f"شما باید مبلغ {loan_amount} را به خانواده {family_name} پرداخت کنید")



                for customer_data in get_all_customer():
                    if customer_data["IS_ACTIVE"] == "false" or not setting_data:
                        continue
                    customer_id = customer_data["ID"]
                    loan_data = get_loan_data_by_customer_id(customer_id)
                    if loan_data["STATUS"] == "false" and loan_data["NUMBER_REMAINING_INSTALLMENTS"] != 0:
                        installment_number = setting_data["INSTALLMENT_NUMBER"]
                        add_installment(loan_data["ID"] , loan_data["NUMBER_REMAINING_INSTALLMENTS"])
                        change_loan_number(loan_data["ID"])

                logging.info("add loan and installment is runnig")
                change_time_status(time_data["ID"])
        time.sleep(3600)

