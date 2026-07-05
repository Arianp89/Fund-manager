from config import API_TOKEN 
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,InlineKeyboardMarkup, InlineKeyboardButton,KeyboardButton 
import telebot 
import logging
from fun import *

#____________________________________LOGG_______________________________________

# logging.basicConfig("level=logging.INFO, filename='project.log', format='%(asctime)s - %(levelname)s - %(message)s")

#____________________________________MAKE-BOT____________________________________

telebot.apihelper.API_URL = 'http://tapi.bale.ai/bot{0}/{1}' 
bot=telebot.TeleBot(API_TOKEN)

#____________________________________COMMAND_____________________________________


@bot.message_handler(commands=['start'])
def start_handler(message):
    start_fun(message)


@bot.message_handler(commands=['help'])
def help_handler(message):
    help_fun(message)

@bot.message_handler(commands=[password_get_access1])
def add_admin_handler(message):
    add_admin_access1_fun(message)


#____________________________________BUTTON______________________________________


@bot.message_handler(func=lambda message: message.text == "گرفتن بکآپ")
def get_backup_handler(message):
    get_backup_func(message)

@bot.message_handler(func=lambda message: message.text == "دریافت لینک")
def get_link_handler(message):
    get_link_func(message)





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
            

#____________________________CALLS_______________________

@bot.callback_query_handler(func=lambda call: True)
def all_callback_query_handler(call):
    call_id = call.id
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data
    print(f'call={call.message.from_user.first_name} [{cid}]:{data}')

    if data.startswith("add-access1"):
        print(data)
        _,customer_id = data.split("_")
        customer_id = int(customer_id)
        add_admin(customer_id)
        add_customer_bot_id(customer_id , int(cid))
        print('ok')


    elif data.startswith("go"):
        print(data.split("_"))
        _,status,page_number=data.split("_")
        page_number = int(page_number)
        if status == "back":
            page_number -=1
        else:
            page_number +=1
        markup = go_ba_ne(get_all_customer() , 'add-access1' , "FULL_NAME" , page_number )
        bot.edit_message_text('انتخاب کنید' , cid , mid , reply_markup=markup)



#________________________________ALL-MESSAGE__________________________
@bot.message_handler(func=lambda message: True)
def all_message_handler(message):
    cid = message.chat.id
    check_admin(cid)


print('code running...') 
logging.info('code running...') 
bot.infinity_polling() 
            
'code write it by:'
'arian panahi  github id : http://github.com/arianp89'  
            