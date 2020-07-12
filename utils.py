import cbpro as cbp
import time
import threading
import commands
import telegram
from telegram.ext.dispatcher import run_async

def get_price(tick):
    public_client = cbp.PublicClient()
    ticker = public_client.get_product_ticker(tick)
    price = ticker['price']
    return price

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def reminder(tick, direction, alertvalue, bot, update, context):
    if direction == '>':
        while float(alertvalue) >= float(get_price(tick)):
            time.sleep(300)
            pass
        msg = 'REMINDER: '+tick+' is higher than '+str(alertvalue)
        context.bot.send_message(update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    elif direction == '<':
        while float(alertvalue) <= float(get_price(tick)):
            time.sleep(300)
            pass
        msg = 'REMINDER: '+tick+' is lower than '+str(alertvalue)
        context.bot.send_message(update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        commands.error_format(bot, update)

def reminderth(tick, direction, alertvalue, bot, update, context):
    reminder_thread = threading.Thread(target=reminder, args=(tick, direction, alertvalue, bot, update, context))
    reminder_thread.start()