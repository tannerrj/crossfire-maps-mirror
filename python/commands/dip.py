import Crossfire

def find_fountain(pl):
    below = pl.Below
    while below is not None:
        if below.ArchName == "fountain":
            return below
        below = below.Below
    return None

def dip(pl):
    f = find_fountain(pl)
    if f is None:
        pl.Message("You must be at a fountain to dip an object into one.")
        return False

    ob = pl.MarkedItem
    if ob is None:
        pl.Message("Mark the item that you would like to dip.")
        return False

    name_before = ob.Name
    def something(s):
        pl.Message("You dip the %s into the %s. %s" % (name_before, f.Name, s))

    def nothing():
        something("Nothing happens.")

    if ob.ArchName == "wbottle_empty" or ob.ArchName == "potion_empty":
        ob.Quantity -= 1
        w = Crossfire.CreateObjectByName("water")
        w.Identified = 1
        w.InsertInto(pl)
        pl.Message("You fill the %s with water from the %s." % (name_before, f.Name))
    elif ob.ArchName == "scroll_new":
        ob.Quantity -= 1
        w = Crossfire.CreateObjectByName("scroll")
        w.Identified = 0
        w.InsertInto(pl)
        something("The magic runes fade away.")
    elif ob.Type == Crossfire.Type.BOOK:
        if ob.Message != None and len(ob.Message) != 0:
            ob.Message = ""
            something("The writing fades away.")
        else:
            something("It gets wet.")
    else:
        nothing()

dip(Crossfire.WhoAmI())
