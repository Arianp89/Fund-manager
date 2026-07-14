from services.call_back_ser import access_1_ser,add_admin_access2_call,change_admin_access2_ser
from keyboard.keyboard import admin_markup
from keyboard.call_back_markup import add_admin_access1_markup,add_admin_access2_markup,change_admin_access2_markup_go


class call_back:

    def __init__(self , bot , call):
        self.bot = bot
        self.call_id = call.id
        self.cid = call.message.chat.id
        self.mid = call.message.message_id

    def add_access1(self , data ):
        _,admin_id = data.split("_")
        try:
            self.bot.delete_message(self.cid , self.mid)
            admin_id = int(admin_id)
            access_1_ser(admin_id , self.cid)
            self.bot.answer_callback_query(self.call_id , "شما ادمین شدید.")
            self.bot.send_message(self.cid , 'این هم از منوی شما' , reply_markup=admin_markup(self.cid))
            
        except Exception as e:
            self.bot.answer_callback_query(self.call_id , 'دوباره دستور را وارد کنید این پیام منقضی شده است.')
            print(e)


    def go_add_access1_go(self, data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = add_admin_access1_markup(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)


    def add_admin_access2(self , data):
        _ , customer_id = data.split("_")
        try:
            self.bot.delete_message(self.cid , self.mid)
            data = add_admin_access2_call(customer_id)
            status = data[0]
            if status:
                chat_id = data[1]
                self.bot.send_message(chat_id , 'شما ادمین شدید دکمه جا به جایی رو بزنید' , reply_markup=admin_markup())
            else:
                self.bot.answer_callback_query(self.call_id , 'ربات را استارت نزده')
            self.bot.send_message(self.cid , 'با موفقیت اضافه شد' , reply_markup = admin_markup(self.cid))
        except Exception as e:
            print(e)


    def add_admin_access2_go(self , data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = add_admin_access2_markup(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)



    def change_admin_access2(self , data):
        _ , customer_id = data.split("_")
        try:
            self.bot.delete_message(self.cid , self.mid)
            change_admin_access2_ser(customer_id)
        except Exception as e:
            print(e)
            self.bot.send_message(self.cid , 'دوباره تلاش کنید')
        self.bot.send_message(self.cid , 'ادمین با موفقیت تغییر کرد')




    def change_admin_access2_go(self , data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = change_admin_access2_markup_go(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)






    def go(self , data):
        _,_,_,call_name =data.split("_")
        if call_name == "add-access1":
            self.go_add_access1_go(data)
        
        elif call_name == "add-admin":
            self.add_admin_access2_go(data)

        elif call_name == "change-admin":
            self.change_admin_access2_go(data)


        