from .command import send_message_one_data , admin_step_send_messsage
from services.step_ser import get_all_family_bot_id

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
        for head_id in get_all_family_bot_id():
            print(head_id)
            try:
                self.bot.send_message(head_id , text)
            except:
                self.bot.send_message(cid , f"ارسال نشد:{head_id}")
            admin_step_send_messsage.pop(cid)
            return
        self.bot.send_message(cid , "با موفقیت ارسال شد")




