from keyboard.markup import admin_markup , customer_markup
from services.command_ser import *
from handler.command import *





class bot_commands:

    def __init__(self , bot):
        self.bot = bot

    def start(self , message):
        cid = message.chat.id
        if len(message.text.split()) > 1:
            family_id = int(message.text.split('_')[-1])
            status = get_family_link_ser(family_id , cid)
            if status is None:
                self.bot.send_message(cid , 'لینک خراب است')
                return
            self.bot.send_message(cid , 'سلام' , customer_markup())
            return
        status = start_ser(cid)
        if status is None:
            return
        elif status:
            self.bot.send_message(cid , 'سلام ادمین' , reply_markup=admin_markup(cid))
        elif not status:
            self.bot.send_message(cid , 'سلام کاربر' , reply_markup=customer_markup())

    def help(self , message):
        cid = message.chat.id
        text = help_ser(cid)
        if text is None:
            return
        self.bot.send_message(cid , text)


    def add_admin_access1(self , message):
        cid = message.chat.id
        data = add_admin_access1_ser()
        markup = data[0]
        admin_id = data[1]
        if markup is None:
            bot.send_message(admin_id , f'کابر @{message.chat.username}\n دسرسی سطح یک')
            return
        self.bot.send_message(cid , "لطفا کاربر مورد نظر خود را انتخاب کنید" , reply_markup=markup)

    def all_message(self , message):
        cid = message.chat.id
        if not check_is_in_db(cid):
            return
        if  check_admin(cid):
            markup = customer_markup()
        else:
            markup = admin_markup(cid)
        self.bot.send_message(cid , 'دستور یافت نشد' , reply_markup = markup)
