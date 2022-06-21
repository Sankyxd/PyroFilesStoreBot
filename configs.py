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

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @SD4UZ

👥 **Support:** [📢 Telegram Channel 📢](https://t.me/CJR_OFFICIAL)

📢 **Updates Channel:** [👆 CLIC HERE 👆](https://t.me/+ME3VIAyvhIRhODYx)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @SD4UZ

Developer is Super Noob. Just Learning from Official Docs. Please Support the developer for Keeping the Service Alive.
"""
	HOME_TEXT = """
**Hey👋**, [{}](tg://user?id={})\n\n**This is Permanent** **CJR File Store Bot**.

**Check My Information. Also! Check **About Bot Button**.😉
"""
