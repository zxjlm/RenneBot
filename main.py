# -*-coding:utf-8 -*-

"""
# Company    : astute
# Author     ：zhang.xinjian
# Description：
"""

import os
import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler

updater = Updater(token=os.getenv('TG_BOT_TOKEN'), use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def ping(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="pong")


start_handler = CommandHandler('start', start)
ping_handler = MessageHandler(Filters.regex(r'ping'), ping)

dispatcher.add_handler(ping_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
