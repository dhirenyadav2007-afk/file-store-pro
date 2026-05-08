import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5090'
OWNER_ID = 5915807321

MSG_EFFECT = 5046509860389126442

SHORT_URL = "shrinkme.io" # shortner url 
SHORT_API = "xxxxxxxxxxx45e6887xxxxxxxxxxx" # shortner API
SHORT_TUT = "https://t.me/ANIME_X_FLEX/19" # shortner tutorial link

# Bot Configuration
SESSION = "BotifyX-Botz"
TOKEN = "7877034637:AAGlODRLCbWY4LrnQTLxrv7Nr-F42YXtHas" # Bot token
API_ID = "21484586" # API ID
API_HASH = "d1d12be1da9b5a1cb8356c0bf0695a23" # API HASH
WORKERS = 5

DB_URI = "mongodb+srv://ANI_OTAKU:ANI_OTAKU@cluster0.t3frstc.mongodb.net/?appName=Cluster0" # MongoDB URI
DB_NAME = "Maskman-Real_Mask_Man"

FSUBS = [[-1001669538512, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1002298993427   # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [5915807321]
# Bot Settings
DISABLE_BTN = True
PROTECT = False # For content protection stops message forwarding and copying from the bot and same goes for the screenshot

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!! {mention}× sᴇɴᴘᴀɪ 🎊\n</b><blockquote><b>ᴜɴʟᴏᴄᴋ ᴛʜᴇ ᴇɴɪɢᴍᴀ ᴏꜰ Aᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛs ᴡʜᴇʀᴇ ᴅᴇsɪʀᴇ ʟɪɴɢᴇʀs ʙᴇʏᴏɴᴅ ᴇᴠᴇʀʏ ꜰʀᴀᴍᴇ, ᴅʀᴀᴡɪɴɢ ʏᴏᴜ ɪɴᴛᴏ ᴀ ʀᴇᴀʟᴍ ᴏꜰ ʜɪᴅᴅᴇɴ ꜰᴀɴᴛᴀsɪᴇs ᴀɴᴅ sɪʟᴇɴᴛ ᴏʙsᴇssɪᴏɴs.</b></blockquote>\n<blockquote>››ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Real_Mask_Man'>Mask Man ™</a></blockquote>",
    "FSUB": "<blockquote>›› ʜᴇʏ × sᴇɴᴘᴀɪ 🎊</blockquote>\n<blockquote><b>ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b></blockquote>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: <a href='https://t.me/Real_Mask_Man'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>\n<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/BotifyX_Pro_Botz'>ʙᴏᴛɪғʏx_ᴏғғɪᴄɪᴀʟ</a> \n›› ᴏᴡɴᴇʀ: @Real_Mask_Man\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ITS_shun_x</b></blockquote>",
    "CHANNELS":"<blockquote expandable>›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Real_Mask_Man'>ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ</a>\n›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/BotifyX_Pro_Botz'>Bᴏᴛɪғʏx ʙᴏᴛs</a>\n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ITSANIMEN</b></blockquote>",
    "REPLY": "<b>ғᴜᴄᴋ ᴏғғ ʙɪᴛᴄʜ !!!</b>",
    "SHORT_MSG": "<blockquote><b>✧ TOKEN EXPIRED</b></blockquote>\n<blockquote>›› ᴘʟᴇᴀsᴇ ᴠᴇʀɪғʏ ᴛᴏ ʀᴇɢᴀɪɴ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ғɪʟᴇs\n›› ᴠᴀʟɪᴅ ᴄʀᴇᴅɪᴛs: 5 ᴄʀᴇᴅɪᴛs</blockquote>\n────────────────────────\n<blockquote>›› ᴡʜᴀᴛ ɪs ᴀ ᴛᴏᴋᴇɴ?</blockquote>\n<blockquote>≡  ᴇᴀᴄʜ ᴀᴅ ʙʏᴘᴀss ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ 5 ᴄʀᴇᴅɪᴛs.ᴏɴᴇ ᴄʀᴇᴅɪᴛ ɪs ᴄᴏɴsᴜᴍᴇᴅ ᴘᴇʀ ғɪʟᴇ/ʟɪɴᴋ ᴀᴄᴄᴇss.</blockquote>",
    "START_PHOTO": "https://ibb.co/ch6kvnMf",
    "FSUB_PHOTO": "https://ibb.co/C5q41g1C",
    "SHORT_PIC": "https://ibb.co/XxMhdhDs",
    "SHORT": "https://ibb.co/mC9H5kmF",
    "SHORT_VERIFY": "https://ibb.co/rGg6R2q6",
    "PREMIUM_PLANS_PIC": "https://ibb.co/8Dzq5n9G",
    "QR_PAYMENT_PIC": "https://ibb.co/kVPDT5cP"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
