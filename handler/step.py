from .command import capital_amount_data,setting_step,setting_data,pay_installment_step,pay_debt_step,add_new_customer_step,add_new_customer_data,send_message_one_data , admin_step_send_messsage,customer_step_send_message,customer_data_send_message
from services.step_ser import setting_step_ser,pay_debt_A_text,add_new_customer_step_B_ser,pay_installment_A_text_and_admin_id,get_all_family_bot_id,send_message_admin_ser
from keyboard.call_back_markup import capital_amoount_step_A_markup,send_message_admin_markup,check_pay_admin_markup,pay_debt_A_markup
from config import bot_id
from keyboard.keyboard import customer_markup
class admin_step:

    def __init__(self , bot):
        self.bot = bot

    def send_message_one_step_A(self , message):
        cid = message.chat.id
        text = "پیام ادمین \n"
        text += message.text

        customer_bot_id = send_message_one_data[cid]
        try:
            self.bot.send_message(customer_bot_id , text)
        except:
            self.bot.send_message(cid , "ارسال نشد")
            admin_step_send_messsage.pop(cid)
            send_message_one_data.pop(cid)
            return
        self.bot.send_message(cid , "با موفقیت ارسال شد")
        admin_step_send_messsage.pop(cid)
        send_message_one_data.pop(cid)

    def send_message_one_step_B(self , message):
        cid = message.chat.id
        text = "پیام ادمین \n"
        text += message.text
        for customer_bot_id in get_all_family_bot_id():
            try:
                self.bot.send_message(customer_bot_id , text)
            except:
                self.bot.send_message(cid , f"ارسال نشد برای:[کاربر](https://web.bale.ai/chat?uid={customer_bot_id})")
        admin_step_send_messsage.pop(cid)
        self.bot.send_message(cid , "با موفقیت ارسال شد")

    def add_new_customer_step_A(self , message):
        cid = message.chat.id
        customer_name = message.text
        add_new_customer_data[cid] = {"name":customer_name , "amount":None}
        add_new_customer_step[cid] = "B"
        text = "مبلغ سرمایه را به عدد وارد کنید:"
        self.bot.send_message(cid , text)

    def add_new_customer_step_B(self , message):
        cid = message.chat.id
        customer_amount = message.text
        try:
            customer_amount = int(customer_amount)
            add_new_customer_data[cid]["amount"] = customer_amount

        except:
            self.bot.send_message(cid , "لطفا سرمایه را به عدد وارد کنید")
            return
        
        link_id = add_new_customer_step_B_ser(cid)
        text = "لطفا برای وارد شدن به اکانت خود روی" +f" [لینک](https://web.bale.ai/chat?uid={bot_id}&start=family_{link_id})" + "کلیک کنید"
        self.bot.send_message(cid , text)
        self.bot.send_message(cid , "لطفا لینک بالا را برای کاربر ارسال کنید")
        add_new_customer_data.pop(cid) 
        add_new_customer_step.pop(cid)


    def setting_step_A(self , message):
        cid = message.chat.id
        cart_number = message.text
        len_cart_number = len(cart_number)
        try:
            cart_number = int(cart_number)
        except Exception as e:
            print(e)
            self.bot.send_message(cid , "به عدد وارد کنید")
            return

        if len_cart_number != 16:
            self.bot.send_message(cid , "شماره کارت خود را درست وارد کنید")
            return
        
        self.bot.send_message(cid , "نام دارنده کارت را وارد کنید")
        setting_data[cid] = {"cart_number":cart_number , "cart_name":None ,
                             "installment_number":None , "capital_amount":None}
        setting_step[cid] = "B"


    def setting_step_B(self , message):
        cid = message.chat.id
        cart_name = message.text
        setting_data[cid]["cart_name"] = cart_name
        self.bot.send_message(cid , "تعداد اقساط را وارد کنید")
        setting_step[cid] = "C"
    

    def setting_step_C(self , message):
        cid = message.chat.id
        installment_number = message.text
        try:
            installment_number = int(installment_number)
        except Exception as e:
            print(e)
            self.bot.send_message(cid , "به عدد وارد کنید")
            return
        setting_data[cid]["installment_number"] = installment_number
        self.bot.send_message(cid , "مبلغ افزایش سرمایه را به ریال وارد کنید")
        setting_step[cid] = "D"

        

    def setting_step_D(self , message):
        cid = message.chat.id
        capital_amount = message.text
        setting_data[cid]["capital_amount"] = capital_amount
        data = setting_data[cid]
        setting_step_ser(cid , data)
        self.bot.send_message(cid , "تمام شد")
        setting_step.pop(cid)


        




class customer_step:

    def __init__(self , bot):
        self.bot = bot


    def send_message_admin_step_A(self , message):
        cid = message.chat.id
        text = "پیام کاربر \n"
        text += message.text
        admin_bot_id = send_message_admin_ser(cid)
        markup = send_message_admin_markup(cid)
        try:
            self.bot.send_message(admin_bot_id , text , reply_markup = markup)
        except Exception as e:
            print(e)
        self.bot.send_message(cid , "پیام با موفقیت ارسال شد")
        customer_step_send_message.pop(cid)

    def send_message_admin_step_B(self , message):
        cid = message.chat.id
        text = "پاسخ ادمین \n"
        text += message.text
        customer_bot_id = customer_data_send_message[cid]
        try:
            self.bot.send_message(customer_bot_id , text)
        except Exception as e:
            print(e)
            self.bot.send_message(cid , "پیام ارسال نشد")
            customer_data_send_message.pop(cid)
            customer_step_send_message.pop(cid)
            return
        
        self.bot.send_message(cid , "پیام با موفقیت ارسال شد")
        customer_data_send_message.pop(cid)
        customer_step_send_message.pop(cid)

    def pay_installment_A(self , message):
        cid = message.chat.id
        photo_id = message.photo[-1].file_id
        text = pay_installment_A_text_and_admin_id(cid)
        markup = check_pay_admin_markup(cid)
        admin_id  = text[1]
        text = text[0]
        self.bot.send_photo(admin_id , photo_id , text , reply_markup=markup)
        self.bot.send_message(cid , "پیام برای ادمین ارسال شد")
        pay_installment_step.pop(cid)
        
    def pay_debt_A(self , message):
        cid = message.chat.id
        file_id = message.photo[-1].file_id
        text , admin_bot_id = pay_debt_A_text(cid)
        markup = pay_debt_A_markup(cid)
        self.bot.send_photo(admin_bot_id , file_id , text , reply_markup=markup)
        self.bot.send_message(cid , "فیش شما برای ادمین ارسال شد" , reply_markup = customer_markup(cid))
        pay_debt_step.pop(cid)

    def pay_installment_step_B(self , message):
        cid = message.chat.id
        capital_amount = message.text
        try:
            capital_amount = int(capital_amount)
        except Exception as e:
            print(e)
            self.bot.send_message(cid , "به عدد وارد کنید")
            return

        capital_amount_data[cid] = capital_amount
        markup = capital_amoount_step_A_markup(cid , "us")
        self.bot.send_message(cid , "برای چه کسی افزایش داده اید" , reply_markup = markup)
              
