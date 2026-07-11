from database import *


def access_1_ser(customer_id , chat_id):
    add_admin(customer_id)
    add_customer_bot_id(customer_id , int(chat_id))