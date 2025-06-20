import Crossfire

import CFBank
import CFShop as shop
import CFPShop as pshop

item = Crossfire.WhoAmI()
player = Crossfire.WhoIsActivator()
amount = Crossfire.WhoIsOther()

def event():
    if pshop.has_tag(item):
        seller = pshop.seller(item)
        with CFBank.open() as bank:
            bank.deposit(seller, amount)
        pshop.remove_tag(item)

        # don't log self-buy
        if player.Name == seller:
            return

        # the buy transaction is logged below, but we need to make a
        # corresponding sell transaction since the seller only tagged the item
        # and never actually sold it to the shop
        shop.transact(sell=True, seller=seller)

    shop.transact(sell=False)

event()
