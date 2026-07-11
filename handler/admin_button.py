from backup.information_database_improved import DatabaseManager
from config import *
import shutil
import os
from services.admin_ser import *


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

        
    def make_family_link(self , message):
        cid = message.chat.id
        text_list = make_family_link_ser()
        for text in text_list:
            self.bot.send_message(cid , text)