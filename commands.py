import telegram
from telegram.ext.dispatcher import run_async
import utils
# =====================================
# Commands
# =====================================
# BotFatherList:
# btcprice - BTC-EUR price
# ethprice - ETH-EUR price
# price - ex. /price BTC-USD
# alertme - ex. /alertme BTC-EUR > 8300

welcome_text = """
WELCOME TO CRYPTOBOT!

Commands:
 /btcprice - BTC-EUR price
 /ethprice - ETH-EUR price
 /price - ex. /price BTC-USD
 /alertme - ex. /alertme BTC-EUR > 8300

BOT developed by arkeane"""

@run_async
def cmd_start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    context.bot.send_message(update.message.chat_id, text=welcome_text, parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
def cmd_btcprice(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    tick = 'BTC-EUR'
    price = str(tick)+": "+str(utils.get_price(tick))+'€'
    context.bot.send_message(update.message.chat_id, text=price, parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
def cmd_ethprice(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    tick = 'ETH-EUR'
    price = str(tick)+": "+str(utils.get_price(tick))+'€'
    context.bot.send_message(update.message.chat_id, text=price, parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
def cmd_price(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    if len(context.args) != 1:
        error_args_price(context.bot, update)
        return
    tick = context.args[0]
    price = str(tick)+": "+str(utils.get_price(tick))
    context.bot.send_message(update.message.chat_id, text=price, parse_mode=telegram.ParseMode.MARKDOWN)

@run_async
def cmd_alertme(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    chat_data = context.chat_data
    if len(context.args) != 3:
        error_args_reminder(context.bot, update)
        return

    if utils.is_number(context.args[2]) != True:
        error_format(context.bot, update)
        return

    chat_data['tick'] = context.args[0]
    chat_data['direction'] = context.args[1] 
    chat_data['alertvalue'] = context.args[2]
    utils.reminderth(chat_data['tick'], chat_data['direction'], chat_data['alertvalue'], context.bot, update, context)

@run_async
def cmd_convert(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

# =====================================
# Errors
# =====================================
def error_args_price(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, 
    text = ("ERROR: Must provide an argument -- try: /price BTC-USD"),
    parse_mode = telegram.ParseMode.MARKDOWN)

def error_args_reminder(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, 
    text = ("ERROR: Not Enough Arguments -- try: /alertme BTC-EUR > 8300"),
    parse_mode = telegram.ParseMode.MARKDOWN)

def error_format(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id,
    text = ("ERROR: Price is not a number -- try: /alertme BTC-EUR > 8300"),
    parse_mode = telegram.ParseMode.MARKDOWN)