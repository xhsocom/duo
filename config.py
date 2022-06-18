## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu10poZ6nzqOLIuyOQddJ75CXV7ed9_GNvitZD81V_fMLzHK76aRDTCimLyaCKE5xfGicLgagdlp7cp4WTDkbz480oz-zFX9LVuKeSgCKKzh0xaxfSVADu7LoCzLtXXlM5XcbnUvX7g_b9jUryqyYPDOKv6IgGXCls5_TpoUFLXJMtMhbcFWtkHHWersokdTd4W8HBjDXse3NdmmuRdSzFwPCBoa8BaAPO_RVysiriS1HEkix-5Sm-koBgXb0BmD1wty8eMRPF327sVrs-_AdAOfXhYc07jBuEyDjFEWyVscaArHdcTJ8yIxcTisQUPZOzOEpm1iUGh2XZvbdO6X33MI=")
BOT_TOKEN = getenv("BOT_TOKEN", "5558231995:AAH-XmbUTvs5pBpVzAt0fekCag1PA7MXyf4")
BOT_NAME = getenv("BOT_NAME", ". ميوزك ckuba .")
API_ID = int(getenv("API_ID", "14262335"))
API_HASH = getenv("API_HASH", "c616a7e91bac7ec7bc7db434f1e7fb0c")
OWNER_NAME = getenv("OWNER_NAME", "Dusho")
OWNER_USERNAME = getenv("OWNER_USERNAME", "CC999")
ALIVE_NAME = getenv("ALIVE_NAME", "Dusho")
BOT_USERNAME = getenv("BOT_USERNAME", "CKUBABOT")
OWNER_ID = getenv("OWNER_ID", "1398221569")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ckubahelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ckuba")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ckuba")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "!").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
