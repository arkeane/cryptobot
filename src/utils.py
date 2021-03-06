import cbpro as cbp
import time
import threading
import commands
import telegram
import requests

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
        return
    elif direction == '<':
        while float(alertvalue) <= float(get_price(tick)):
            time.sleep(300)
            pass
        msg = 'REMINDER: '+tick+' is lower than '+str(alertvalue)
        context.bot.send_message(update.message.chat_id, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
        return
    else:
        commands.error_format(bot, update)
        return

def reminderth(tick, direction, alertvalue, bot, update, context):
    reminder_thread = threading.Thread(target=reminder, args=(tick, direction, alertvalue, bot, update, context))
    reminder_thread.start()
    context.bot.send_message(update.message.chat_id, text="REMINDER SET", parse_mode=telegram.ParseMode.MARKDOWN)
    return

def convert(value, tick, direction):
    price = float(get_price(tick))
    value = float(value)
    if direction == 1:
        convalue = value*price
        return convalue
    elif direction == 2:
        convalue = value/price
        return convalue
        
def value_conversion(update, context):
    direction = 1
    chat_data = context.chat_data
    tick = str(chat_data['first'])+"-"+str(chat_data['second'])
    value = chat_data['value']
    return

def get_transactioninfo(hash):
    info = requests.get('https://mempool.space/api/tx/'+ hash +'/status')
    return info