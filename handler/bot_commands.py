from keyboard.keyboard import admin_markup , customer_markup
from services.command_ser import *
from handler.command import *
from services.link import link





class bot_commands:

    def __init__(self , bot):
        self.bot = bot

    def start(self , message):
        cid = message.chat.id

        if len(message.text.split()) > 1:
            links = link(self.bot)
            link_name = message.text.split()[1]
            if link_name.startswith("family"):
                links.family_link(message)
                return

        status = start_ser(cid)
        if status is None:
            return
        elif status:
            self.bot.send_message(cid , "سلام به ربات ما خوش آمدید" , reply_markup=admin_markup(cid))
        elif not status:
            self.bot.send_message(cid , "سلام به ربات ما خوش آمدید" , reply_markup=customer_markup(cid))

    def help(self , message):
        cid = message.chat.id
        text = help_ser(cid)
        if text is None:
            return
        self.bot.send_message(cid , text)


    def add_admin_access1(self , message):
        cid = message.chat.id
        datas = add_admin_access1_ser(self.bot)
        try:
            markup = datas[0]
            admin_id = datas[1]
        except Exception as e:
            markup = datas
        if markup is None:
            self.bot.send_message(admin_id , f'کابر @{message.chat.username}\n دسرسی سطح یک')
            return
        self.bot.send_message(cid , "لطفا کاربر مورد نظر خود را انتخاب کنید" , reply_markup=markup)


    def cancel(self , message):
        cid = message.chat.id
        if cid in customer_step_send_message:
            customer_step_send_message.pop(cid)

        if check_admin(cid) == 'admin':
            markup = admin_markup(cid)
        else:
            markup = customer_markup(cid)

        self.bot.send_message(cid , "شما خارج شدید" , reply_markup = markup)
    

    def all_message(self , message):
        cid = message.chat.id
        text = message.text
        try:
            link_name = text.split("start=")[-1].split(")")[0]
            links = link(self.bot)
            if link_name.startswith("family"):
                links.message_link_family(message , link_name.split("_")[1])
                return
        except:
            pass

        if not check_is_in_db(cid):
            return
        
        if  check_admin(cid) == "admin":
            markup = admin_markup(cid)
        else:
            markup = customer_markup(cid)
        self.bot.send_message(cid , 'دستور یافت نشد' , reply_markup = markup)
