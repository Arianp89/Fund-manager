from  .command_ser import get_family_link_ser
from  keyboard.markup import customer_markup
from database import get_family_data,get_family_link_status,add_customer_bot_id,change_status_use_link_family

class link:

    def __init__(self ,bot):
        self.bot = bot
            
    def get_family_link_ser(family_id , chat_id):
        family_data = get_family_data(family_id)
        if family_data is  None:
            return None
        if not get_family_link_status(family_id):
            return False
        head_id = family_data['HEAD_ID']
        add_customer_bot_id(head_id , chat_id)
        change_status_use_link_family(family_id)
        return True
    

    def family_link(self , message):
        cid = message.chat.id
        try:
            family_id = int(message.text.split('_')[-1])
        except Exception as e:
            print(e)
            return
        status = self.get_family_link_ser(family_id , cid)
        print(status)
        if status is None:
            self.bot.send_message(cid , 'لینک خراب است')
            return
        elif status:
            return
        self.bot.send_message(cid , 'سلام' , customer_markup())
        return