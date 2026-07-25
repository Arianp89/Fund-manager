from backup.information_database_improved import DatabaseManager
from keyboard.keyboard import customer_markup
from keyboard.call_back_markup import profile_markup,pay_installment_markup
from services.admin_ser import check_admin,get_admin_access_by_chat_id,get_admin_access,check_is_in_db
from .command import customer_step_send_message
from services.admin_ser import *
from services.customer_ser import *





class customer_button:

    def __init__(self , bot):
        self.bot = bot
    

    def answer_customer(self , chat_id):
        if not check_is_in_db(chat_id):
            return False
        return True
    

    def go_customer_panel(self , message):  
        cid = message.chat.id
        if not self.answer_customer(cid):
            return

        access_level = get_admin_access(cid)
        if check_admin(cid) == 'customer':
            self.bot.send_message(cid , 'دستور وارد شده اشتباه است' , reply_markup = customer_markup(cid))
            return False
        
        if access_level is not None:
            admin_access = get_admin_access_by_chat_id(cid)
            if admin_access == access_level:
                return True
        self.bot.send_message(cid , "شما وارد پنل کاربر شدید" , reply_markup = customer_markup(cid))


    def send_message_to_admin(self , message):
        cid = message.chat.id
        if self.answer_customer(cid) == False:
            return
        
        customer_step_send_message[cid] = "A"
        self.bot.send_message(cid , "پیام خود را وارد کنید برای خروچ /cancel را بزنید")


    def profile(self , message):
        cid = message.chat.id
        if not self.answer_customer(cid):
            return
        
        text = get_profile_text(cid)
        markup = profile_markup(cid)
        self.bot.send_message(cid , text , reply_markup = markup)

    def pay_installment(self , message):
        cid = message.chat.id
        if not self.answer_customer(cid):
            return
        
        text = pay_installment_ser(cid)
        print(text)
        if not text[0]:
            self.bot.send_message(cid , text[1])
            return
        markup = pay_installment_markup(message)
        self.bot.send_message(cid , text[1] , reply_markup = markup)
