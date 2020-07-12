import commands
import os
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, PicklePersistence, ConversationHandler

with open(os.path.dirname(os.path.realpath(__file__)) + '/bot_token.txt') as file:
    TOKEN = file.readline().strip()

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    #Commands
    dispatcher.add_handler(CommandHandler('start', commands.cmd_start))
    dispatcher.add_handler(CommandHandler('btcprice', commands.cmd_btcprice))
    dispatcher.add_handler(CommandHandler('ethprice', commands.cmd_ethprice))
    dispatcher.add_handler(CommandHandler('price', commands.cmd_price, pass_args=True, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler('alertme', commands.cmd_alertme, pass_args=True, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler('convert', commands.cmd_convert, pass_args=True, pass_chat_data=True))
    
    #Start polling
    updater.start_polling()
