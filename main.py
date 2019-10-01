#logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#custom config
import config

#telegram dependency
from telegram.ext import (Updater, CommandHandler)
updater = Updater(token=config.teleConfig.botToken, use_context=True)
dp = updater.dispatcher

#requests & json
import requests
import json

#definer file
from definer import *

#start telegram bot
updater.start_polling()
print("Telegram bot is running....")