from database import *
from handler.fun import *


class call_back:

    def __init__(self , bot , call):
        self.bot = bot
        self.call_id = call.id
        self.cid = call.message.chat.id
        self.mid = call.message.message_id

    def add_access1(self , data ):
        _,customer_id = data.split("_")

        try:
            self.bot.delete_message(self.cid , self.mid)
            customer_id = int(customer_id)
            add_admin(customer_id)
            add_customer_bot_id(customer_id , int(self.cid))
            self.bot.answer_callback_query(self.call_id , "شما ادمین شدید.")
        except Exception as e:
            self.bot.answer_callback_query(self.call_id , 'دوباره دستور را وارد کنید این پیام منقضی شده است.')
            print(e)


    def go(self , data):
        print(data.split("_"))
        _,status,page_number=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = go_ba_ne(get_all_customer() , 'add-access1' , "FULL_NAME" , page_number ,self.call_id)
        if not markup:
            return 
        bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)