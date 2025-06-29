import Crossfire

def find_fountain(pl):
    below = pl.Below
    while below is not None:
        if below.Name.startswith("fountain"):
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

    empty_bottles = {"wbottle_empty", "potion_empty", "boozebottle_empty"}
    qty = max(1, pl.CmdCount)
    qty = min(ob.Quantity, qty)

    if ob.ArchName in empty_bottles:
        ob.Quantity -= qty
        w = Crossfire.CreateObjectByName("water")
        w.Identified = 1 # prevent infinite exp farming by dip/identify/drink/repeat
        pl.Message("You fill the %s with water from the %s." % (name_before, f.Name))
        w.Quantity = qty
        pl.Map.Insert(w, pl.X, pl.Y)
        pl.Take(w) # can fail
    elif ob.ArchName == "scroll_new":
        ob.Quantity -= qty
        w = Crossfire.CreateObjectByName("scroll")
        w.Identified = 0
        w.Quantity = qty
        pl.Map.Insert(w, pl.X, pl.Y)
        pl.Take(w) # can fail
        something("The magic runes fade away.")
    elif ob.Type == Crossfire.Type.BOOK:
        if ob.Message != None and len(ob.Message) != 0:
            ob.Message = ""
            something("The writing fades away.")
        else:
            something("It gets wet.")
        ob.WriteKey("knowledge_marker", None, 0)
        ob.Name = ob.Archetype.Clone.Name
        ob.NamePl = ob.Archetype.Clone.NamePl
    else:
        nothing()

dip(Crossfire.WhoAmI())
