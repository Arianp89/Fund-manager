from  keyboard.keyboard import customer_markup
from keyboard.call_back_markup import message_link_family_markup
from database import get_customer_bot_id,get_admin_id_b_access,get_family_data,get_family_link_status,add_customer_bot_id,change_status_use_link_family

class link:

    def __init__(self ,bot):
        self.bot = bot
            
    def get_family_link_ser(self , link_id , chat_id):
        family_data = get_family_data(link_id)
        if family_data is None:
            return False
        if not get_family_link_status(family_data["ID"]):
            return False
        head_id = family_data['HEAD_ID']
        add_customer_bot_id(head_id , chat_id)
        change_status_use_link_family(link_id)
        return True
    

    def family_link(self , message):
        cid = message.chat.id
        try:
            link_id = message.text.split('_')[-1]
        except Exception as e:
            print(e)
            return
        status = self.get_family_link_ser(link_id , cid)
        if not status:
            self.bot.send_message(cid , 'لینک خراب است')
            return
        elif status:
            self.bot.send_message(cid , 'سلام' , customer_markup(cid))
    

    def message_link_family_ser(self , link_id):
        family_data = get_family_data(link_id)
        if not family_data:
            return False
        elif family_data["USE_LINK"] == "true":
            return False
        return family_data



    def message_link_family(self , message , link_id):
        cid = message.chat.id
        status = self.message_link_family_ser(link_id)
        if not status:
            return
        else:
             admin_id = get_admin_id_b_access(2)
             admin_bot_id = get_customer_bot_id(admin_id)
             text = "ok"
             markup = message_link_family_markup(cid , link_id)
             self.bot.send_message(admin_bot_id , text , reply_markup = markup)
