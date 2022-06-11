import Crossfire
activator=Crossfire.WhoIsActivator()
mymap=activator.Map

whoami=Crossfire.WhoAmI()

if whoami.Name=="Big Chest":

	# Remove all forces, in case player had more than one
	check = activator.Inventory
	while check:
		below = check.Below
		if check.Name == "BigChest":
			check.Remove()
		check = below

	Card=activator.CreateObject("event_apply")
	Card.Name="BigChest"

	myPath=mymap.Path
	Card.Title=myPath
else:
	Target=activator.CheckInventory("BigChest")
	if Target==None:
		whoami.Say("I'm sorry, I can't send you home.  It seems my attachment to the material plane has shifted.")
	else:
		Path=Target.Title
		Map=Crossfire.ReadyMap(Path)
		Target.Remove()

		activator.Teleport(Map, 1,9)
