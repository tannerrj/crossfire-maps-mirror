"""
powerbroker.py -- glowing crystals that buy and sell mana

Usage: add an event_apply and event_say to a non-pickable glowing crystal.
"""

import math

import Crossfire
import CFItemBroker

N0 = 10000 # initial stock
P0 = 10 # price per mana in silver at initial stock, N0
me = Crossfire.WhoAmI()

def charge(payer, quantity):
    return payer.PayAmount(quantity) == 1

def pay(payee, quantity):
    # we can't guarentee that the player has any particular type of coin already
    # so create the object first, then add 1 less than the total.
    if quantity >= 50:
        item = payee.CreateObject('platinum coin')
        CFItemBroker.Item(item).add(int(quantity/50))
    if quantity % 50 > 0:
        item = payee.CreateObject('gold coin')
        CFItemBroker.Item(item).add(int((quantity % 50)/10))
    if quantity % 50 > 0:
        item = payee.CreateObject('silver coin')
        CFItemBroker.Item(item).add(int(quantity % 10))

def on_apply():
    Crossfire.SetReturnValue(0)

def profit():
    return 0.1

def mana_stock():
    stock = Crossfire.GetPrivateDictionary().get('total_mana')
    if stock is None:
        stock = N0
    return stock

def change_stock(amount):
    Crossfire.GetPrivateDictionary()['total_mana'] = mana_stock() + amount

def base_price(sp):
    # 1 gold per spell point at nominal stock
    return sp * P0 * (1 + 1/N0*(N0 - mana_stock()))

def sell_price(sp):
    return math.floor(base_price(sp)*(1 - profit()))

def buy_price(sp):
    return max(1, math.ceil(base_price(sp)*(1 + profit())))

def buy_mana():
    message = Crossfire.WhatIsMessage().lower()
    try:
        amount = int(message)
        max_buy = min(me.MaxSP, mana_stock())
        if mana_stock() == 0:
            me.Say("Sorry, we are out of stock right now. Come back later.")
            return
        if amount > max_buy:
            me.Say("I can only sell you up to %d mana right now." % max_buy)
            amount = max_buy
        price = buy_price(amount)
        def do_buy_mana():
            if charge(Crossfire.WhoIsActivator(), price):
                me.Say("Bought %d mana for %s." % (amount, Crossfire.CostStringFromValue(price)))
                me.SP += amount
                change_stock(-amount)
            else:
                me.Say("You can't afford that!")
        confirm("%d mana would cost you %s. Buy?" % (amount, Crossfire.CostStringFromValue(price)), do_buy_mana)
    except ValueError:
        me.Say("How much mana would you like to buy? %d silver per mana point." % buy_price(1))

def sell_mana():
    message = Crossfire.WhatIsMessage().lower()
    price = sell_price(me.SP)
    if price <= 0:
        me.Say("Sorry, we're not interested in buying mana right now.")
        return

    def do_sell_mana():
        me.Say("Sold %d mana for %s." % (me.SP, Crossfire.CostStringFromValue(price)))
        pay(Crossfire.WhoIsActivator(), price)
        change_stock(me.SP)
        me.SP = 0
    confirm("Sell %d mana for %s?" % (me.SP, Crossfire.CostStringFromValue(price)), do_sell_mana)

def confirm(text, action):
    me.Say(text)
    Crossfire.AddReply("yes", "Yes!")
    Crossfire.AddReply("no", "No, thank you.")
    Crossfire.GetPrivateDictionary()['confirm_action'] = action

def check_confirm():
    action = Crossfire.GetPrivateDictionary().get('confirm_action')
    if action is not None:
        reply = Crossfire.WhatIsMessage().lower()
        if reply == "yes":
            action()
            del Crossfire.GetPrivateDictionary()['confirm_action']
        elif reply == "no":
            me.Say("Thank you, come again!")
            del Crossfire.GetPrivateDictionary()['confirm_action']
        else:
            me.Say("Please answer either 'yes' or 'no'.")
        return True
    return False

def status():
    me.Say("%d mana in stock, buy %d/sell %d silver per mana." % (mana_stock(), buy_price(1), sell_price(1)))

def stock(message):
    try:
        qty = int(message.split()[1])
        change_stock(qty)
        me.Say("Added %d mana to stock." % qty)
        status()
    except Exception:
        me.Say("I didn't understand that.")

def on_say():
    if check_confirm():
        return # don't do anything else

    message = Crossfire.WhatIsMessage().lower()
    if message == 'status' and Crossfire.WhoIsActivator().DungeonMaster:
        status()
    elif message.split()[0] == 'stock' and Crossfire.WhoIsActivator().DungeonMaster:
        stock(message)
    elif me.SP > 0:
        sell_mana()
    else:
        buy_mana()

if Crossfire.WhatIsEvent().Subtype == 1:
    on_apply()
elif Crossfire.WhatIsEvent().Subtype == 6:
    on_say()
