from DML import *
import csv
class Import_excel:
    number = 0
    family_data = {'family_id':None}
    def __init__(self , line_number):
        self.line_number = line_number
    
    def open_file(self):
        file_datas = list()
        with open('excel.csv' , 'r' , encoding='utf-8-sig') as f:
            for num in range(self.line_number):
                data = f.readline()
                data_list = data.split(',')
                # print(data_list)

                if data_list[0] == 'new_line':
                    file_data = {'full_name':'new_line'}
                    # print(1)


                elif data_list[0] == 'FALSE':
                    status = 'false'
                    # print(2)
                    file_data = {'full_name': data_list[-2].replace('\n','') + ' ' + data_list[-1],
                            'loan_amount': None ,
                            'loan_number': None , 
                            'capital_increase': None ,
                            'total_amount': None ,
                            'total_capital': None ,
                            'status':status}
                    
                elif data_list[0] == 'TRUE':
                    status = 'true'
                    # print(3)
                    file_data = {'full_name': data_list[-2].replace('\n','') + ' ' + data_list[-1],
                                'loan_amount': int(data_list[-3]) ,
                                'loan_number': int(data_list[-4]), 
                                'capital_increase': int(data_list[-5]) ,
                                'total_amount': int(data_list[-6]) ,
                                'total_capital': int(data_list[-7]) ,
                                'status':status}
                    
                

                file_datas.append(file_data)
        return file_datas
        

    def add_customer_data(self , file_data  ,line_number):
        # print(file_data)
        # print(line_number)

        if file_data['full_name'] == 'new_line':
            # print(4,file_data['full_name'])
            self.number += 1

        elif self.number == 1 or line_number==1:
            # print(5,file_data['full_name'])
            family_id = add_family()
            head_id = add_customer(family_id ,
                                    file_data['full_name'] ,
                                    file_data['total_capital'] ,
                                    file_data['status'])
            family_name = file_data['full_name']
            add_family_data(family_id , int(head_id) , family_name)
            self.family_data['family_id'] = family_id 
            customer_id = head_id
            installment_amount = file_data['loan_amount']
            number_paid_installment = file_data['loan_number']
            if  installment_amount :
                loan_amount = 24 * installment_amount
                number_paid_installment = 24-number_paid_installment
            else:
                loan_amount = None
                number_paid_installment = None
            amount_paid = file_data['total_amount']
            Capital_increase = file_data['capital_increase']
            if number_paid_installment is None:
                pass
            else:
                loan_id = add_loan_data(customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid)
                add_installment(loan_id , number_paid_installment , Capital_increase)
            self.number = 0
        else:
            # print(6,file_data['full_name'])
            family_id = self.family_data['family_id']
            customer_id = add_customer(family_id , 
                            file_data['full_name'] , 
                            file_data['total_capital'] , 
                            file_data['status'])
            
            installment_amount = file_data['loan_amount']
            number_paid_installment = file_data['loan_number']
            if  installment_amount :
                loan_amount = 24 * installment_amount
                number_paid_installment = 24 - number_paid_installment
            else:
                loan_amount = None
                number_paid_installment = None
            number_paid_installment = file_data['loan_number']
            amount_paid = file_data['total_amount']
            Capital_increase = file_data['capital_increase']
            print('number_paid_installment',number_paid_installment)
            if number_paid_installment is None:
                pass
            else:
                loan_id = add_loan_data(customer_id  , loan_amount , installment_amount , number_paid_installment , amount_paid)
                add_installment(loan_id , number_paid_installment , Capital_increase)
            # print('ook')
            



        



def main():
    num = 0
    im = Import_excel(11)
    file_data = im.open_file()
    # print(file_data)
    for file_data in file_data:
        num += 1
        im.add_customer_data(file_data  , num)

if __name__ == "__main__":
    main()
