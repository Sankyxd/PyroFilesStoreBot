# (c) @Sankyxd

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**This is Permanent Files Store Bot!**

🤖 **ᴍʏ ɴᴀᴍᴇ:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **ʟᴀɴɢᴜᴀɢᴇ:** [Python3](https://www.python.org)

📚 **ʟɪʙʀᴀʀʏ:** [Pyrogram](https://docs.pyrogram.org)

📡 **ʜᴏꜱᴛᴇᴅ ᴏɴ:** [Heroku](https://heroku.com)

🧑🏻‍💻 **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** @SD4UZ

👥 **ꜱᴜᴘᴘᴏʀᴛ:** [📢 Telegram Channel 📢](https://t.me/CJR_OFFICIAL)

📢 **ᴜᴘᴅᴀᴛᴇꜱ:** [👆 CLIC HERE 👆](https://t.me/+ME3VIAyvhIRhODYx)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** @SD4UZ

**𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚒𝚜 𝚂𝚞𝚙𝚎𝚛 𝙽𝚘𝚘𝚋. 𝙹𝚞𝚜𝚝 𝙻𝚎𝚊𝚛𝚗𝚒𝚗𝚐 𝚏𝚛𝚘𝚖 𝙾𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝙳𝚘𝚌𝚜. 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚝𝚑𝚎 𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚏𝚘𝚛 𝙺𝚎𝚎𝚙𝚒𝚗𝚐 𝚝𝚑𝚎 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙰𝚕𝚒𝚟𝚎.**
"""
	HOME_TEXT = """
**𝐇𝐞𝐲👋**, [{}](tg://user?id={})\n\n**𝐓𝐡𝐢𝐬 𝐢𝐬 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭** 𝐂𝐉𝐑 𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭**.

**𝐂𝐡𝐞𝐜𝐤 𝐌𝐲 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧. 𝐀𝐥𝐬𝐨! 𝐂𝐡𝐞𝐜𝐤 **𝐀𝐛𝐨𝐮𝐭 𝐁𝐨𝐭 𝐁𝐮𝐭𝐭𝐨𝐧**.😉
"""
