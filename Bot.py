from telegram.ext import Updater
from telegram.ext import CommandHandler
import urllib
import requests
import logging

import Comunio
import main
from SecretKeys import *
from time import sleep, localtime, strftime


# message = "testmessage"
def init_bot():
    updater = Updater(token=API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    start_handler = CommandHandler("start", start)
    table_total_handler = CommandHandler("t", table_total)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(table_total_handler)

    updater.start_polling()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Servus")


def table_total(update, context):

    data = main.read_csv()
    table_string = main.get_table_total(data)

    context.bot.send_message(chat_id=update.effective_chat.id, text=table_string)

# def weekly_notification(message, hour, day):
#     while True:
#         current_hour = get_current_hour()
#         if current_hour is hour:
#             url_notif = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
#                 API_KEY, CHAT_ID, urllib.parse.quote_plus(message))
#             _ = requests.get(url_notif)
#             sleep(1380)  # sleep 23h
#
#
# def get_current_hour():
#     t = localtime()
#     current_time = strftime("%H", t)
#     return int(current_time)
