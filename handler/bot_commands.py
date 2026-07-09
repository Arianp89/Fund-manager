from handler.markup import admin_markup , customer_markup
from database import *
from handler.admin_button import *
from handler.fun import *




class commands:

    def __init__(self , bot):
        self.bot = bot

    def start(self , message):
        cid = message.chat.id
        admin_buttons = admin_button(self.bot)
        admin_buttons.family_link(message)

        if not check_is_in_db(cid):
            return
        if check_admin(cid , 'start'):
            self.bot.send_message(cid , 'سلام ادمین' , reply_markup=admin_markup(cid))


    def help(self , message):
        cid = message.chat.id
        if not check_is_in_db(cid):
            return
        text = 'help \n'
        for com , about in commands.items():
            text += f"/{com}     {about} \n"
        self.bot.send_message(cid , text)


    def add_admin_access1(self , message):
        cid = message.chat.id
        markup = go_ba_ne(get_all_customer() , 'add-access1' , "FULL_NAME")
        if get_admin_list() == []:
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
