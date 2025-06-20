import time

def has_tag(ob):
    return len(ob.ReadKey('price')) != 0

def remove_tag(ob):
    ob.Unpaid = False
    ob.WriteKey('price', "", 0)
    ob.WriteKey('pshop_owner', "", 0)
    ob.WriteKey('pshop_timestamp', "", 0)

def tag(ob, owner, price):
    ob.Unpaid = True
    ob.WriteKey('price', str(price), 1)
    ob.WriteKey('pshop_owner', owner.Name, 1)
    ob.WriteKey('pshop_timestamp', "%d" % (int(time.time())), 1)

def seller(ob):
    return ob.ReadKey('pshop_owner')
