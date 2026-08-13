from database.DML import *
import os
import string
import random


def is_none(arg):
    if arg == '':
        return None
    return int(arg)

class Import_excel:
    number = 0
    family_data = {'family_id':None}
    def __init__(self , line_number):
        self.line_number = line_number
    
    def open_file(self):
        file_datas = list()
        with open(os.path.join("Data" , 'excel.csv') , 'r' , encoding='utf-8-sig') as f:
            for num in range(self.line_number):
                data = f.readline()
                data_list = data.split(',')

                if data_list[0] == 'new_line':
                    file_data = {'full_name':'new_line'}

                elif data_list[0] == 'FALSE':
                    status = 'false'
                    file_data = {'full_name': data_list[-2].replace('\n','') + ' ' + data_list[-1],
                            'loan_amount': None ,
                            'loan_number': None , 
                            'capital_increase': None ,
                            'total_amount': None ,
                            'total_capital': None ,
                            'status':status}
                    
                elif data_list[0] == 'TRUE':
                    status = 'true'
                    file_data = {'full_name': data_list[-2].replace('\n','') + ' ' + data_list[-1],
                                'loan_amount': is_none(data_list[-3]) ,
                                'loan_number': is_none(data_list[-4]), 
                                'capital_increase': is_none(data_list[-5]) ,
                                'total_amount': is_none(data_list[-6]) ,
                                'total_capital': is_none(data_list[-7]) ,
                                'status':status}
                    
                
                file_datas.append(file_data)
        return file_datas
        

    def add_customer_data(self , file_data  ,line_number):
        family_name = file_data['full_name']
        full_name = family_name
        if full_name != 'new_line':
            installment_amount = file_data['loan_amount']
            number_paid_installment = file_data['loan_number']
            amount_paid = file_data['total_amount']
            Capital_increase = file_data['capital_increase']

        if file_data['full_name'] == 'new_line':
            self.number += 1


        elif self.number == 1 or line_number==1:
            requence=string.ascii_lowercase + string.ascii_uppercase + string.digits
            link_id = str(''.join(random.choices(requence,k=6)))
            family_id = add_family(link_id)
            head_id = add_customer(family_id ,
                                    full_name ,
                                    file_data['total_capital'] ,
                                    file_data['status'])
            add_family_data(family_id , int(head_id) , family_name)
            self.family_data['family_id'] = family_id 

            customer_id = head_id
            if  installment_amount :
                loan_amount = 24 * installment_amount
                number_paid_installment = 24 - number_paid_installment

            else:
                loan_amount = None
                number_paid_installment = None

            if number_paid_installment is None:
                pass

            else:
                if number_paid_installment > 0:
                    status = 'false'
                else:
                    status = "true"
                loan_id = add_loan_data(customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid , status)
                add_installment(loan_id , number_paid_installment )
                change_loan_number(loan_id)
                
            
            self.number = 0

        else:
            family_id = self.family_data['family_id']
            customer_id = add_customer(family_id , 
                            full_name, 
                            file_data['total_capital'] , 
                            file_data['status'])
            
            
            if  installment_amount :
                loan_amount = 24 * installment_amount
                number_paid_installment = 24 - number_paid_installment

            else:
                loan_amount = None
                number_paid_installment = None

            Capital_increase = file_data['capital_increase']

            if number_paid_installment is None:
                pass
            else:
                if number_paid_installment > 0:
                    status = 'false'
                else:
                    status = "true"
                loan_id = add_loan_data(customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid , status)
                add_installment(loan_id , number_paid_installment)
            



        



def main():
    num = 0
    line_number = 11
    im = Import_excel(int(line_number))
    file_data = im.open_file()
    for file_data in file_data:
        num += 1
        im.add_customer_data(file_data  , num)

if __name__ == "__main__":
    main()
