import commands
import os
import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, PicklePersistence, ConversationHandler, MessageHandler, Filters

with open(os.path.dirname(os.path.realpath(__file__)) + '/bot_token.txt') as file:
    TOKEN = file.readline().strip()

FIRST = 1
SECOND = 2

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Commands
    dispatcher.add_handler(CommandHandler('start', commands.cmd_start))
    dispatcher.add_handler(CommandHandler('help', commands.cmd_help))
    dispatcher.add_handler(CommandHandler('btcprice', commands.cmd_btcprice))
    dispatcher.add_handler(CommandHandler('ethprice', commands.cmd_ethprice))
    dispatcher.add_handler(CommandHandler('txinfo', commands.cmd_transactinfo))
    dispatcher.add_handler(CommandHandler(
        'price', commands.cmd_price, pass_args=True, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler(
        'alertme', commands.cmd_alertme, pass_args=True, pass_chat_data=True))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(
            'convert', commands.cmd_convert, pass_args=True, pass_chat_data=True)],
        states={FIRST: [CommandHandler('cancel', commands.cmd_cancel),
                        CallbackQueryHandler(
            commands.cb_first_to_second, pattern='patt_first_to_second', pass_chat_data=True),
            CallbackQueryHandler(commands.cb_second_to_first, pattern='patt_second_to_first', pass_chat_data=True)],
            SECOND: [CommandHandler('cancel', commands.cmd_cancel),
                     MessageHandler(Filters.text, commands.cb_get_value)]
        },
        fallbacks=[CommandHandler('cancel', commands.cmd_cancel)],
    )
    dispatcher.add_handler(conv_handler)

    # Start polling
    updater.start_polling()
    updater.idle()
