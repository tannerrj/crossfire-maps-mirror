import Crossfire
import CFPShop as pshop

Crossfire.SetReturnValue(1) # do not run default handler

import importlib
importlib.reload(pshop)

activator = Crossfire.WhoIsActivator()
marked = activator.MarkedItem

def handle_event():
    if marked is None:
        activator.Message("Mark an item in your inventory, then use 'count' to set its price.")
        return

    # Do not allow selling money. That would let someone else spend someone's
    # unpaid money to buy stuff.
    if marked.Type == Crossfire.Type.MONEY:
        activator.Message("You cannot label money for sale.")
        return

    owner = marked.ReadKey('pshop_owner')
    if len(owner) == 0 and marked.Unpaid:
        activator.Message("This item belongs to the shop.")
        return

    if len(owner) != 0 and owner != activator.Name:
        activator.Message("This item belongs to %s." % (owner))
        return

    count = activator.CmdCount
    if count == 0:
        # tag removal mode
        if pshop.has_tag(marked):
            pshop.remove_tag(marked)
            activator.Message("You remove the price tag from the %s." % (marked.Name))
        else:
            activator.Message("The %s does not have a price tag to remove." % (marked.Name))
    else:
        # tagging mode
        # need to get name before it becomes unpaid
        activator.Message("You attach a label: %s (%s)" % (Crossfire.CostStringFromValue(count), activator.Name))
        pshop.tag(marked, activator, count)

handle_event()
