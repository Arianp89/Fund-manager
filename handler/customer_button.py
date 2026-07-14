from backup.information_database_improved import DatabaseManager
from keyboard.keyboard import customer_markup
from services.admin_ser import check_admin,get_admin_access_by_chat_id,get_admin_access





class customer_button:

    def __init__(self , bot):
        self.bot = bot
    

    def answer_customer(self , chat_id , access_level=2):
        if check_admin(chat_id) == 'customer':
            self.bot.send_message(chat_id , 'دستور وارد شده اشتباه است' , reply_markup = customer_markup())
            return False
        
      
        admin_access = get_admin_access_by_chat_id(chat_id)
        if admin_access == access_level:
            return True
        self.bot.send_message(chat_id , 'دستور وارد شده اشتباه است' , reply_markup = customer_markup())
        return False
    

    def go_to_customer_panel(self , message):  
        cid = message.chat.id

        access_level = get_admin_access(cid)
        if not self.answer_customer(cid , access_level):
            return
        
        self.bot.send_message(cid , "شما وارد پنل کاربر شدید" , reply_markup = customer_markup(cid))