from backup.information_database_improved import DatabaseManager
from config import *
import shutil
import os
from database import *


class admin_button:

    def __init__(self , bot):
        self.bot = bot
    
    def get_backup(self ,message):
        cid = message.chat.id
        database = DatabaseManager(db_config , database_name)
        database.export_to_file()
        os.makedirs("Data", exist_ok=True)
        folder_path = "database_data"
        backup_path = os.path.join("Data" , "backup")

        shutil.make_archive(
            backup_path,
            "zip",
            folder_path
)

        with open(os.path.join("Data", "backup.zip"), "rb") as f:
            text = "فایل [backup](github.com/arianp89/database-data-mover)"
            self.bot.send_document(cid, f, caption=text, parse_mode="Markdown")

        
    def family_link(self , message , status='get'):
        cid = message.chat.id

        if status == "get":
            if len(message.text.split()) > 1:
                family_id = int(message.text.split('_')[-1])
                family_data = get_family_data(family_id)
                if family_data is  None:
                    return
                head_id = family_data['HEAD_ID']
                add_customer_bot_id(head_id , cid)
                self.bot.send_message(cid , 'سلام')

        else:
            for id in get_all_family_id():
                text = f'کاربر {get_family_data(id)['FAMILY_NAME']} \n'
                text += " کلیک کنید ."+ f" [لینک](https://web.bale.ai/chat?uid={os.environ.get("bot_cid")}&start=family_{id}) " + "لطفا روی "
                self.bot.send_message(cid , text)