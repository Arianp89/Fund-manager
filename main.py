from config import API_TOKEN 
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
import telebot 
import logging
from handler import bot_commands,admin_button,call_back




telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}' 
bot=telebot.TeleBot(API_TOKEN)



password_get_access1 = "Ad1fWQ89Gg"
bot_command = bot_commands(bot)
admin_buttons = admin_button(bot)

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

@bot.message_handler(func=lambda message:message.text == "تغییر ادمین")
def change_admin_access2(message):
    admin_buttons.change_admin_access2(message)

#____________________________CALLS_______________________

@bot.callback_query_handler(func=lambda call: True)
def all_callback_query_handler(call):
    call_handler = call_back(bot , call)
    data = call.data
    print(f'call={call.message.from_user.first_name} [{call.message.chat.id}]:{data}')

    if data.startswith("add-access1"):
        call_handler.add_access1(data)

    elif data.startswith("add-admin"):
        call_handler.add_admin_access2(data)

    elif data.startswith("change-admin"):
        call_handler.change_admin_access2(data)

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
            