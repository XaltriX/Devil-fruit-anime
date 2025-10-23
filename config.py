# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "24955235"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "f317b3f7bbe390346d8b46868cff0de8")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002004278204"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "5706788169"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "-1002309557046")

#Port
PORT = os.environ.get("PORT", "8080")

#Database --⚠️ REQUIRED--
DB_URL = os.environ.get("DB_URL", "mongodb+srv://eno2223456:7Cdmqig5Ih2vrqW4@cluster0.ccpmee5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "HonistaRobot")

VERIFY_DB = os.environ.get("VERIFY_DB", "mongodb+srv://luffydb:12345@cluster0.nue5da5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DBV_NAME = os.environ.get("VERIFY_DBNAME", "Honista")


TOKEN_PIC = os.environ.get("TOKEN_PIC", "https://graph.org/file/f03274dfad4979c8f95d8-b0f06dbc9d0d0edb41.jpg")


#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/HTODLINKZ/2")


START_PIC = os.environ.get("START_PIC", "https://graph.org/file/8263af1da9ac363d8c580-a8912d879836f10ccd.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/9391e81b5959c012691fa-7082ef0f9fe62f2c56.jpg")

                        
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://graph.org/file/f03274dfad4979c8f95d8-b0f06dbc9d0d0edb41.jpg https://graph.org/file/9bb59500aad7bd82a5fed-a73aed8d1313fee973.jpg https://graph.org/file/8b18a066cbc95cbe49ca2-4a04fdb50bc94af59b.jpg https://graph.org/file/ad6982514284cbc8a8a29-5e214b4d10962fdd62.jpg https://graph.org/file/8263af1da9ac363d8c580-a8912d879836f10ccd.jpg")).split() #Required
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
