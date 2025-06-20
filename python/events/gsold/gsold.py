import CFShop as shop
import CFPShop as pshop

shop.transact(sell=True)

# Remove player price tag, if one somehow makes it here, to avoid confusing the
# shopkeeper about the price of an item if someone wants to buy it.
item = Crossfire.WhoAmI()
pshop.remove_tag(item)
