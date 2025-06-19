import Crossfire
import CFSqlDb as cfdb

def init():
    with cfdb.open() as db:
        db.execute("CREATE TABLE IF NOT EXISTS shop_transactions('shop' TEXT, 'time' DATE, 'player' TEXT, 'arch' TEXT, 'name' TEXT, 'quantity' INT, 'amount' INT);")

def transact(sell):
    """
    sell is True when a player sells an item to a shop. Since transactions are
    recorded from a shop's perspective, a sell results in positive quantity
    (gain in stock) but negative amount (paid the player). This way, you can
    sum quantity to determine shop stock and sum amount to get shop net
    earnings.
    """
    with cfdb.open() as db:
        item = Crossfire.WhoAmI()
        player = Crossfire.WhoIsActivator()
        amount = Crossfire.WhoIsOther()

        sign = 1
        if sell:
            sign = -1

        db.execute("INSERT INTO shop_transactions VALUES (?, datetime('now'), ?, ?, ?, ?, ?);",
                   (player.Map.Path, player.Name, item.Archetype.Name, item.QueryName(), item.Quantity * -sign, amount * sign))
        db.commit()

