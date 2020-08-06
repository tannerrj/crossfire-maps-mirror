import Crossfire

me = Crossfire.WhoAmI()
ac = Crossfire.WhoIsActivator()

ac.Write("You feel the "+me.Name+" bind to you.")
me.Cursed = 1
