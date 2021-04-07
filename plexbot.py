#imports
import requests
import re
from functools import wraps
from telegram.ext import Updater
from telegram.ext import CommandHandler
from plexapi.myplex import MyPlexAccount
updater = Updater(token='{{TELEGRAM_TOKEN}}', use_context=True)

plexaccount = MyPlexAccount('{{PLEX_USERNAME}}', '{{PLEX_PASSWORD}}')
plexserver = plexaccount.resource('{{PLEX_SERVER}}').connect()

#idk
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

######################## /start
def start(update, context):
    # Change the text to your liking
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to Gopniknet PLEX, to get access to the server use the /invite command")
    print("start")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
########################

######################## /invite
def invite(update, context):
    if context.args == [] :
        r = "Send an account name after the command eg. /invite username"
    elif len(context.args) > 1 :
        r = "only send one account name"
    else:
        try:
            plexaccount.inviteFriend(context.args[0],plexserver)
            r = "invited ", context.args[0], ", check your mailbox to accept."
        except:
            r = "Error inviting, the server is most certainly full or you are already invited."
    context.bot.send_message(chat_id=update.message.chat_id, text=r)
    print("invited : ", r)

code_handler = CommandHandler('invite', invite)
dispatcher.add_handler(code_handler)
########################


updater.start_polling()


#Examples

#def caps(update, context):
#    text_caps = ' '.join(context.args).upper()
#    context.bot.send_message(chat_id=update.message.chat_id, text=text_caps)

#caps_handler = CommandHandler('caps', caps)
#dispatcher.add_handler(caps_handler)

#echo anything
#def echo(update, context):
#    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

#from telegram.ext import MessageHandler, Filters
#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)
