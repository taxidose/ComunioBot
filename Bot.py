from telegram.ext import Updater
from telegram.ext import CommandHandler
import urllib
import requests
import logging
# import Comunio
import main
from SecretKeys import *


# from time import sleep, localtime, strftime


# message = "testmessage"
def init_bot():
    updater = Updater(token=API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    start_handler = CommandHandler("start", start)
    info_handler = CommandHandler(("info", "i", "help"), info)
    table_total_handler = CommandHandler(("t", "tabelle", "gesamt"), table_total)
    last_matchday_handler = CommandHandler(("l", "letzter", "spieltag"), last_matchday)
    f_vs_j_handler = CommandHandler(("vs", "franken", "jecken", "lol"), f_vs_j)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(table_total_handler)
    dispatcher.add_handler(last_matchday_handler)
    dispatcher.add_handler(f_vs_j_handler)
    logging.info("...............................bot initialized")
    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text("Servus")


def info(update, context):
    update.message.reply_text(
        f"ComunioBot v0.1\nBefehle:\n/t --> Gesamttabelle\n/l --> letzter Spieltag\n/vs --> Franken vs Jecken")


def table_total(update, context):
    data = main.read_csv()
    table_string = main.get_table_total(data)
    update.message.reply_text(table_string)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=table_string)
    logging.info("table total after request sent")


def last_matchday(update, context):
    data = main.read_csv()
    last_matchday_string = main.get_last_matchday(data)
    update.message.reply_text(last_matchday_string)
    logging.info("last matchday after request sent")


def f_vs_j(update, context):
    data = main.read_csv()
    f_vs_j_string = main.franken_vs_jecken(data)
    update.message.reply_text(f_vs_j_string)
    # context.bot.send_message(chat_id=update.effective_chat.id, text=f_vs_j_string)
    logging.info("franken_vs_jecken after request sent")


def weekly_notification(message):
    url_notif = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        API_KEY, CHAT_ID, urllib.parse.quote_plus(message))
    _ = requests.get(url_notif)
    logging.info("weekly table notficiation sent")

#
#
# def get_current_hour():
#     t = localtime()
#     current_time = strftime("%H", t)
#     return int(current_time)
