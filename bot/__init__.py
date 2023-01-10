

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("24326221"))

API_HASH = os.environ.get("00e648d133cab6649bb364b5fb3630d3")

BOT_TOKEN = os.environ.get("5852387662:AAEAWLY72zF_e59xzUlrl_D0nP4Sm7c4Ezk")

DB_URI = os.environ.get("mongodb+srv://hbhavar12:Hrishi@123@cluster0.qunj8nu.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQCWRZEcRnYZwdonCCbSTov-mGHVD5wxytiu-UvKWLfl9cgh-qhH-NDk2n8MqTx7uNYTIvNK_p-t2NXXqXNYKScvIo_sXmh1guV0akxV2DfnXOwuIXZwwtlMIt6QiSyyDhLQAS_zFHm67Gw_gc3jSuwcTQ-aYGFC-_SbqG17z14_ueVCJs-L3PdU3hB-EUXvQosNDORWJ8K5RbZOIEODgZsj2u4jQ4vP6kofZsgpC0nO3SBq1DAw3krIwPDrbw4EC-FS7Aoqrr_jMQuAP-6dusRJ4n3Mf_fpfD_geI9c9tMYOvTYi_NCsZ0YVWYmyn53tIA16rQGTKsqrTG8lwWaV7sZAAAAADz2O-QA")

BUTTON = os.environ.get("BUTTON", "Channel - https://t.me/hrishi_bhavar_0819")  # Button - link

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
