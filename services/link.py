from  keyboard.keyboard import customer_markup
from database import get_family_data,get_family_link_status,add_customer_bot_id,change_status_use_link_family

class link:

    def __init__(self ,bot):
        self.bot = bot
            
    def get_family_link_ser(self , link_id , chat_id):
        family_data = get_family_data(link_id)
        print(family_data)
        if family_data is None:
            return False
        if not get_family_link_status(link_id):
            return True
        head_id = family_data['HEAD_ID']
        add_customer_bot_id(head_id , chat_id)
        change_status_use_link_family(link_id)
        if get_family_link_status(link_id):
            return False
    

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
        return