from .command import see_data_step
import time
import datetime
from database import *
import jdatetime
def get_ziro():
    while True:
        see_data_step.clear()
        time.sleep(3600*24)

def change_time(dt):
    return jdatetime.datetime.fromgregorian(datetime=dt)

def add_loan_and_installment(bot):
    while True:
        total_amount = 0
        total_pay = 0
        time_data = get_time()
        now = jdatetime.datetime.now()
        if time_data is None or now.day == 21 and now.day != change_time(time_data["TIME"]).day:
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
                        loan_id = add_loan_data(customer_id , loan_amount , loan_amount/installment_number , installment_number , 0 , "false")
                        add_installment(loan_id , installment_number)
                        change_loan_number(loan_id)


                for customer_data in get_all_customer():
                    if customer_data["IS_ACTIVE"] == "false" or not setting_data:
                        continue
                    customer_id = customer_data["ID"]
                    loan_data = get_loan_data_by_customer_id(customer_id)
                    if loan_data["STATUS"] == "false" and loan_data["NUMBER_REMAINING_INSTALLMENTS"] > 0:
                        installment_number = setting_data["INSTALLMENT_NUMBER"]
                        add_installment(loan_data["ID"] , loan_data["NUMBER_REMAINING_INSTALLMENTS"])
                        change_loan_number(loan_data["ID"])

                change_time_status(time_data["ID"])
        time.sleep(3600)

