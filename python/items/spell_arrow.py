import Crossfire

who = Crossfire.WhoAmI()
victim = Crossfire.WhoIsOther();

spells = who.ReadKey("arrow_spell")
if spells and victim:
    spells = spells.split(";")
    for spell in spells:
        if ":" in spell:
            quantity, archetype = spell.split(":")
        else:
            quantity = 1
            archetype = spell
        spellob = Crossfire.CreateObjectByName(archetype)
        if spellob:
            for r in range(0, int(quantity)):
                victim.CastAbility(spellob, 0, "")
            spellob.Remove()
