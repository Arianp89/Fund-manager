from handler import bot_commands,admin_button,call_back,admin_step_send_messsage,admin_step,customer_button,customer_step
from handler.command import customer_step_send_message,pay_installment_step
from config import API_TOKEN
import telebot
import logging




telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}'
bot=telebot.TeleBot(API_TOKEN)


password_get_access1 = "Ad1fWQ89Gg"
bot_command = bot_commands(bot)
admin_buttons = admin_button(bot)
customer_buttons = customer_button(bot)
admins_step = admin_step(bot)
customers_step =customer_step(bot)

#____________________________________LOGG_______________________________________

# logging.basicConfig("level=logging.INFO, filename='project.log', format='%(asctime)s - %(levelname)s - %(message)s")

#____________________________________LISENER_____________________________________


def listener(messages):
    for m in messages:
        # print(m)
        if m.content_type == "text":
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: {m.text}")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: {m.text}")
        elif m.content_type == "photo":
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New photo recieved")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: New photo recieved")
        elif m.content_type == "document":
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New document recieved")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: New document recieved")
        elif m.content_type == "voice":
            print(f"{m.chat.first_name} [{str(m.chat.id)}]: New voice recieved")
            logging.info(f"{m.chat.first_name} [{str(m.chat.id)}]: New voice recieved")
bot.set_update_listener(listener)
            

#____________________________________MAKE-BOT____________________________________


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot_command.start(message)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot_command.help(message)

@bot.message_handler(commands=[password_get_access1])
def add_admin_handler(message):
    bot_command.add_admin_access1(message)

@bot.message_handler(commands=['cancel'])
def cancel_handler(message):
    bot_command.cancel(message)


#____________________________________BUTTON______________________________________

#____________________________________ADMIN-ACCESS1________________________________

@bot.message_handler(func=lambda message: message.text == "گرفتن بکآپ")
def get_backup_handler(message):
    admin_buttons.get_backup(message)

@bot.message_handler(func=lambda message: message.text == "دریافت لینک")
def get_link_handler(message):
    admin_buttons.make_family_link(message)

@bot.message_handler(func=lambda message: message.text == "اضافه کردن ادمین")
def add_admin_access2_handler(message):
    admin_buttons.add_admin_access2(message)

@bot.message_handler(func=lambda message: message.text == "تغییر ادمین")
def change_admin_access2(message):
    admin_buttons.change_admin_access2(message)

@bot.message_handler(func=lambda message: message.text == "وارد شدن به پنل ادمین")
def go_admin_panel_handler(message):
    admin_buttons.go_admin_panel(message)

#____________________________________ADMIN-ACCESS2________________________________

@bot.message_handler(func=lambda message: message.text == "پرداخت قسط")
def pay_installment_handler(message):
    customer_buttons.pay_installment(message)

@bot.message_handler(func=lambda message: pay_installment_step.get(message.chat.id) == "A" , content_types=["photo"])
def pay_installment_step_A_handler(message):
    customers_step.pay_installment_A(message)


@bot.message_handler(func=lambda message: message.text == "مشاهده کاربران")
def see_customer_handler(message):
    admin_buttons.see_customer(message)

@bot.message_handler(func=lambda message: message.text == "ارسال پیام به کاربران")
def send_message_to_customer_handler(message):
    admin_buttons.send_message_to_customer(message)


@bot.message_handler(func=lambda message: admin_step_send_messsage.get(message.chat.id) == "A")
def send_message_one_handler_A(message):
    admins_step.send_message_one_step_A(message)

@bot.message_handler(func=lambda message: admin_step_send_messsage.get(message.chat.id) == "B")
def send_message_one_handler_B(message):
    admins_step.send_message_one_step_B(message)





#_______________________________CUSTOMER_______________________________


@bot.message_handler(func=lambda message: message.text == "پروفایل")
def profile_handler(message):
    customer_buttons.profile(message)


@bot.message_handler(func=lambda message: message.text =="ارسال پیام")
def send_message_to_admin_handler(message):
    customer_buttons.send_message_to_admin(message)

@bot.message_handler(func=lambda message: customer_step_send_message.get(message.chat.id) == "A")
def send_message_to_admin_handler_A(message):
    customers_step.send_message_admin_step_A(message)

@bot.message_handler(func=lambda message: customer_step_send_message.get(message.chat.id) == "B")
def send_message_to_admin_handler_B(message):
    customers_step.send_message_admin_step_B(message)

@bot.message_handler(func=lambda message:message.text == "وارد شدن به پنل کاربر")
def go_customer_panel_handler(message):
    customer_buttons.go_customer_panel(message)



#____________________________CALLS_______________________

@bot.callback_query_handler(func=lambda call: True)
def all_callback_query_handler(call):
    call_handler = call_back(bot , call)
    data = call.data
    print(f'call={call.message.from_user.first_name} [{call.message.chat.id}]:{data}')

    if data.startswith("add-access1"):
        call_handler.add_admin_access1(data)

    elif data.startswith("add-admin"):
        call_handler.add_admin_access2(data)

    elif data.startswith("change-admin"):
        call_handler.change_admin_access2(data)

    elif data == "chose_customer_to_send":
        call_handler.send_massage_customer_one()

    elif data.startswith("send-message-one"):
        call_handler.send_message_one(data)

    elif data.startswith("send-message-all-customer"):
        call_handler.send_message_all_customer()

    elif data.startswith("see-message"):
        call_handler.see_message(data)
        
    elif data == "not-answer":
        call_handler.not_answer()

    elif data.startswith("answer-message"):
        call_handler.answer_message(data)

    elif data.startswith("see-data"):
        call_handler.get_customer_data(data)
    
    elif data.startswith("see-family-data"):
        call_handler.get_family_member(data)

    elif data.startswith("admin-see-family-list"):
        call_handler.get_family_list()

    elif data.startswith("get-family-member-list"):
        call_handler.get_family_member(data)

    elif data.startswith("pay-installment"):
        call_handler.pay_installment(data)

    elif data.startswith("family-link-msg"):
        call_handler.family_link_msg(data)

    elif data.startswith("go"):
        call_handler.go(data)


#________________________________ALL-MESSAGE__________________________
@bot.message_handler(func=lambda message: True)
def all_message_handler(message):
    bot_command.all_message(message)


print('code running...')
logging.info('code running...')
bot.infinity_polling()
            
'code write it by:'
'arian panahi  github adrress : https://github.com/arianp89'
            