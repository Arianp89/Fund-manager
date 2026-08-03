from services.call_back_ser import see_customer_pay_text,see_customer_nt_pay_text,change_bot_id_ser,block_acount_done_ser,block_acount_true_ser,get_customer_bot_id_and_message,family_link_msg_true_ser,pay_installment_true_ser,get_see_data_text,access_1_ser,add_admin_access2_call,change_admin_access2_ser,send_message_one_ser
from keyboard.keyboard import admin_markup
from keyboard.call_back_markup import block_acount_markup,turn_off_acount_makup,get_customer_data_back,back_markup,see_customer_list_markup_go,see_customer_list_markup,get_family_markup,get_family_list_markup_go,see_family_data_markup_go,see_family_markup,chose_customer_to_send_message_markup_go,add_admin_access1_markup,add_admin_access2_markup,change_admin_access2_markup_go,chose_customer_to_send_message_markup
from .command import see_data_step,send_message_one_data,admin_step_send_messsage,customer_step_send_message,customer_data_send_message

class call_back:
    def __init__(self , bot , call):
        self.bot = bot
        self.message = call.message
        self.call_id = call.id
        self.cid = call.message.chat.id
        self.mid = call.message.message_id


    def add_admin_access1(self , data ):
        _,family_id = data.split("_")
        try:
            self.bot.delete_message(self.cid , self.mid)
            family_id = int(family_id)
            access_1_ser(family_id , self.cid)
            self.bot.answer_callback_query(self.call_id , "شما ادمین شدید.")
            self.bot.send_message(self.cid , 'این هم از منوی شما' , reply_markup=admin_markup(self.cid))
            
        except Exception as e:
            self.bot.answer_callback_query(self.call_id , 'دوباره دستور را وارد کنید این پیام منقضی شده است.')
            print(e)


    def add_access1_go(self, data):
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
        _ , family_id = data.split("_")
        try:
            self.bot.delete_message(self.cid , self.mid)
            data = add_admin_access2_call(family_id)
            status = data[0]
            if status:
                chat_id = data[1]
                self.bot.send_message(chat_id , 'شما ادمین شدید' , reply_markup=admin_markup(self.cid))
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
        _ , family_id = data.split("_")
        try:
            self.bot.delete_message(self.cid , self.mid)
            change_admin_access2_ser(family_id)
        except Exception as e:
            print(e)
            self.bot.send_message(self.cid , 'دوباره تلاش کنید')
            return
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


    def send_message_one(self , data):
        _ , family_id = data.split("_")

        customer_bot_id = send_message_one_ser(family_id)
        if customer_bot_id is None:
            self.bot.edit_message_text("کاربر ربات را شروع نکرده" , self.cid , self.mid )
            return
        admin_step_send_messsage[self.cid] = "A"
        send_message_one_data[self.cid] = customer_bot_id
        self.bot.edit_message_text("پیام خود را وارد کنید" , self.cid , self.mid )



    def send_massage_customer_one(self):
        markup = chose_customer_to_send_message_markup(self.bot)
        self.bot.edit_message_text(chat_id = self.cid , text = "انتخاب کنید" , message_id = self.mid , reply_markup = markup)


    def chose_customer_to_send_message_go(self , data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = chose_customer_to_send_message_markup_go(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)


    def send_message_all_customer(self):
        admin_step_send_messsage[self.cid] = "B"
        self.bot.edit_message_text("پیام خود را وارد کنید" , self.cid , self.mid)


    def see_message(self , data):
        _ , customer_id = data.split("_")

        try:
            self.bot.delete_message(self.cid , self.mid)
        except Exception as e:
            self.bot.send_message(self.cid , "پیام منقضی شده")
            return
        self.bot.send_message(customer_id , "پیام شما مشاهده شد")
        self.bot.send_message(self.cid , "پیام مشاهده شدن ارسال شد")


    def not_answer(self):
        try:
            self.bot.delete_message(self.cid , self.mid)
        except Exception as e:
            print(e)
            self.bot.answer_callback_query(self.call_id ,"این پیام منقضی شده")


    def answer_message(self , data):
        _ , customer_id = data.split("_")
        customer_step_send_message[self.cid] = "B"
        customer_data_send_message[self.cid] = customer_id
        self.bot.edit_message_text("پیام خود را وارد کنید" , self.cid ,self.mid)


    def get_customer_data(self , data):
        _ , customer_id = data.split("_")
        text = get_see_data_text(customer_id)
        markup = get_customer_data_back(self.cid , customer_id)
        self.bot.edit_message_text(text , self.cid , self.mid , reply_markup = markup)

    def get_family_member(self , data):
        _ , family_id = data.split("_")
        see_data_step[self.cid] = data
        text = "لیست اعضای خانواده"
        markup = see_family_markup(self.bot , family_id)
        self.bot.edit_message_text(text , self.cid , self.mid , reply_markup = markup)


    def get_family_member_go(self , data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = see_family_data_markup_go(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)


    def get_family_list(self):
        text = "لیست خانواده ها"
        markup = get_family_markup(self.bot)
        self.bot.edit_message_text(chat_id = self.cid , message_id = self.mid , text = text , reply_markup = markup)
    
    
    def get_family_list_go(self , data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = get_family_list_markup_go(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)


    def pay_installment(self , data):
        _ , status , customer_bot_id = data.split("_")
        if status == 'true':
            try:
                self.bot.delete_message(self.cid , self.mid)
                self.bot.answer_callback_query(self.call_id ,  "تایید شد")
                pay_installment_true_ser(customer_bot_id)
                self.bot.send_message(customer_bot_id , "تایید شد")
            except Exception as e:
                print(e)
                self.bot.send_message(self.cid , "این پیام منغضی شده")

        else:
            try:
                self.bot.delete_message(self.cid , self.mid)
                self.bot.answer_callback_query(self.call_id , "لغو شد")
                self.bot.send_message(customer_bot_id , "فیش شما توست ادمین لغو شد برای دانستن اطلاهات بیشتر با ادمین در تماس باشید")
            except Exception as e:
                print(e)
                self.bot.send_message(self.cid , "این پیام منغضی شده")


    def family_link_msg(self , data):
        _ , status , link_id , customer_bot_id = data.split("_")
        if status == "true":
            family_link_msg_true_ser(link_id , customer_bot_id)

    def send_message_to_pay(self):
        for customer_bot_id , text in get_customer_bot_id_and_message().items():
            text = f"شمل باید مبلغ {text} را واریز کنید لطفا انجام دهید"
            try:
                self.bot.send_message(customer_bot_id , text)
            except Exception as e:
                print(e)
                self.bot.send_message(self.cid , f"برای کاربر با کد {customer_bot_id} ارسال نشد")
        self.bot.edit_message_text("با موفقیت انجام شد" , self.cid , self.mid)



    def see_customer_list(self):
        see_data_step[self.cid] = "see-customer-list"
        text = "لیست کابران"
        markup = see_customer_list_markup(self.bot)
        self.bot.edit_message_text(chat_id = self.cid , message_id = self.mid , text = text , reply_markup = markup)


    def see_customer_list_go(self , data):
        _,status,page_number,_=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = see_customer_list_markup_go(self.bot , page_number , self.call_id)
        if not markup:
            return 
        self.bot.edit_message_text('انتخاب کنید' , self.cid , self.mid , reply_markup=markup)
        

    def turn_off_acount(self , data):
        _ , customer_id = data.split("_")
        text = "آیا مطمعن  هستید از این کار"
        markup = turn_off_acount_makup(customer_id)
        self.bot.edit_message_text(text = text , chat_id = self.cid , message_id = self.mid , reply_markup = markup)


    def block_acount(self , data):
        _ , status , customer_id = data.split("_")
        if status == 'true':
            _data = block_acount_true_ser(customer_id)
            customer_bot_id = _data[0]
            admin_text = _data[1]
            customer_text = _data[2]
            status = _data[3]
            if status == "1":
                markup = block_acount_markup(customer_id)
            else:
                markup = None
            self.bot.edit_message_text(admin_text , self.cid , self.mid , reply_markup = markup)
            self.bot.send_message(customer_bot_id , customer_text)

        elif status == "false":
            pass

        elif status == "done":
            customer_name , customer_bot_id = block_acount_done_ser(customer_id)
            try:
                self.bot.delete_message(self.cid , self.mid)
            except Exception as e:
                print(e)
                self.bot.edit_message_reply_markup(self.cid , self.mid)
            self.bot.send_message(customer_bot_id , f"اکانت {customer_name} به صورت کامل بسته شد")
            self.bot.send_message(self.cid , "با موفقیت انجام شد")


    def change_bot_id(self , data):
        _ , customer_id = data.split("_")
        customer_bot_id , text = change_bot_id_ser(customer_id)
        try:
            self.bot.delete_message(self.cid , self.mid)
        except Exception as e:
            self.bot.edit_message_reply_markup(self.cid , self.mid)
            print(e)
        self.bot.send_message(customer_bot_id , text)
        self.bot.send_message(self.cid , "با موفقیت انجام شد")

    
    def see_customer_nt_pay(self):
        text = see_customer_nt_pay_text()
        self.bot.edit_message_text(text , self.cid , self.mid)

    
    def see_customer_pay(self):
        text = see_customer_pay_text()
        self.bot.edit_message_text(text , self.cid , self.mid)
        

    def go(self , data):
        _,_,_,call_name =data.split("_")
        if call_name == "add-access1":
            self.add_access1_go(data)
        
        elif call_name == "add-admin":
            self.add_admin_access2_go(data)

        elif call_name == "change-admin":
            self.change_admin_access2_go(data)

        elif call_name == "send-message-one":
            self.chose_customer_to_send_message_go(data)
        
        elif call_name == "see-family-data":
            self.get_family_member_go(data)
        
        elif call_name == "admin-see-family-data":
            self.get_family_list_go(data)
        
        elif call_name == "see-data":
            self.see_customer_list_go(data)
        

    def back(self , data):
        _ , to  = data.split(".")

        if to == "see-customer-list":
            self.see_customer_list()

        elif to.startswith("see-family-data"):
            self.get_family_member(to)
