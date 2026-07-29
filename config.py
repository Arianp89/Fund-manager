import os 

db_config={'host': os.environ.get('db_host'),'user': os.environ.get('db_user'),'password': os.environ.get('password')} 
database_name = os.environ.get('db_name') 


API_TOKEN = os.environ.get('tel_token') 

bot_id = os.environ.get("bot_id")