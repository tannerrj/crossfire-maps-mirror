"""
Crossfire stubs. Auto-generated file, don't edit.
"""

def WhoAmI() -> any: ...

def WhoIsActivator() -> any: ...

def WhoIsOther() -> any: ...

def WhatIsMessage() -> any: ...

def ScriptName() -> any: ...

def ScriptParameters() -> any: ...

def WhatIsEvent() -> any: ...

def MapDirectory() -> any: ...

def UniqueDirectory() -> any: ...

def TempDirectory() -> any: ...

def ConfigDirectory() -> any: ...

def LocalDirectory() -> any: ...

def PlayerDirectory() -> any: ...

def DataDirectory() -> any: ...

def ReadyMap() -> any: ...

def CreateMap() -> any: ...

def FindPlayer(name: str) -> Player:
	"""
Find the specified player from its name.
:param name Player's name, case-sensitive.
:return Player, None if no player matches.
	"""
...

def MatchString() -> any: ...

def GetReturnValue() -> any: ...

def SetReturnValue() -> any: ...

def PluginVersion() -> any: ...

def CreateObject() -> any: ...

def CreateObjectByName() -> any: ...

def GetPrivateDictionary() -> any: ...

def GetSharedDictionary() -> any: ...

def GetPlayers() -> any: ...

def GetArchetypes() -> any: ...

def GetMaps() -> any: ...

def GetParties() -> any: ...

def GetRegions() -> any: ...

def GetFriendlyList() -> any: ...

def RegisterCommand() -> any: ...

def RegisterGlobalEvent() -> any: ...

def UnregisterGlobalEvent() -> any: ...

def GetTime() -> any: ...

def DestroyTimer() -> any: ...

def MapHasBeenLoaded() -> any: ...

def Log() -> any: ...

def FindFace() -> any: ...

def FindAnimation() -> any: ...

def GetSeasonName() -> any: ...

def GetMonthName() -> any: ...

def GetWeekdayName() -> any: ...

def GetPeriodofdayName() -> any: ...

def AddReply() -> any: ...

def SetPlayerMessage() -> any: ...

def NPCSay() -> any: ...

def CostStringFromValue() -> any: ...

class Object:

	@property
	def Name(self) -> any: ...

	@Name.setter
	def Name(self, value: any) -> None: ...

	@property
	def NamePl(self) -> any: ...

	@NamePl.setter
	def NamePl(self, value: any) -> None: ...

	@property
	def Title(self) -> any: ...

	@Title.setter
	def Title(self, value: any) -> None: ...

	@property
	def Race(self) -> any: ...

	@Race.setter
	def Race(self, value: any) -> None: ...

	@property
	def Skill(self) -> any: ...

	@Skill.setter
	def Skill(self, value: any) -> None: ...

	@property
	def Map(self) -> any: ...

	@Map.setter
	def Map(self, value: any) -> None: ...

	@property
	def Cha(self) -> any: ...

	@Cha.setter
	def Cha(self, value: any) -> None: ...

	@property
	def Con(self) -> any: ...

	@Con.setter
	def Con(self, value: any) -> None: ...

	@property
	def Dex(self) -> any: ...

	@Dex.setter
	def Dex(self, value: any) -> None: ...

	@property
	def Int(self) -> any: ...

	@Int.setter
	def Int(self, value: any) -> None: ...

	@property
	def Pow(self) -> any: ...

	@Pow.setter
	def Pow(self, value: any) -> None: ...

	@property
	def Str(self) -> any: ...

	@Str.setter
	def Str(self, value: any) -> None: ...

	@property
	def Wis(self) -> any: ...

	@Wis.setter
	def Wis(self, value: any) -> None: ...

	@property
	def HP(self) -> any: ...

	@HP.setter
	def HP(self, value: any) -> None: ...

	@property
	def MaxHP(self) -> any: ...

	@MaxHP.setter
	def MaxHP(self, value: any) -> None: ...

	@property
	def SP(self) -> any: ...

	@SP.setter
	def SP(self, value: any) -> None: ...

	@property
	def MaxSP(self) -> any: ...

	@MaxSP.setter
	def MaxSP(self, value: any) -> None: ...

	@property
	def Grace(self) -> any: ...

	@Grace.setter
	def Grace(self, value: any) -> None: ...

	@property
	def MaxGrace(self) -> any: ...

	@MaxGrace.setter
	def MaxGrace(self, value: any) -> None: ...

	@property
	def Food(self) -> any: ...

	@Food.setter
	def Food(self, value: any) -> None: ...

	@property
	def AC(self) -> any: ...

	@AC.setter
	def AC(self, value: any) -> None: ...

	@property
	def WC(self) -> any: ...

	@WC.setter
	def WC(self, value: any) -> None: ...

	@property
	def Dam(self) -> any: ...

	@Dam.setter
	def Dam(self, value: any) -> None: ...

	@property
	def Luck(self) -> any: ...

	@property
	def Exp(self) -> any: ...

	@Exp.setter
	def Exp(self, value: any) -> None: ...

	@property
	def ExpMul(self) -> any: ...

	@property
	def TotalExp(self) -> any: ...

	@property
	def Message(self) -> any: ...

	@Message.setter
	def Message(self, value: any) -> None: ...

	@property
	def Slaying(self) -> any: ...

	@Slaying.setter
	def Slaying(self, value: any) -> None: ...

	@property
	def Cursed(self) -> any: ...

	@Cursed.setter
	def Cursed(self, value: any) -> None: ...

	@property
	def Damned(self) -> any: ...

	@Damned.setter
	def Damned(self, value: any) -> None: ...

	@property
	def Weight(self) -> any: ...

	@Weight.setter
	def Weight(self, value: any) -> None: ...

	@property
	def WeightLimit(self) -> any: ...

	@WeightLimit.setter
	def WeightLimit(self, value: any) -> None: ...

	@property
	def Above(self) -> any: ...

	@property
	def Below(self) -> any: ...

	@property
	def Inventory(self) -> any: ...

	@property
	def X(self) -> any: ...

	@property
	def Y(self) -> any: ...

	@property
	def Direction(self) -> any: ...

	@Direction.setter
	def Direction(self, value: any) -> None: ...

	@property
	def Facing(self) -> any: ...

	@Facing.setter
	def Facing(self, value: any) -> None: ...

	@property
	def Unaggressive(self) -> any: ...

	@Unaggressive.setter
	def Unaggressive(self, value: any) -> None: ...

	@property
	def God(self) -> any: ...

	@God.setter
	def God(self, value: any) -> None: ...

	@property
	def Pickable(self) -> any: ...

	@Pickable.setter
	def Pickable(self, value: any) -> None: ...

	@property
	def Quantity(self) -> any: ...

	@Quantity.setter
	def Quantity(self, value: any) -> None: ...

	@property
	def Invisible(self) -> any: ...

	@Invisible.setter
	def Invisible(self, value: any) -> None: ...

	@property
	def Speed(self) -> any: ...

	@Speed.setter
	def Speed(self, value: any) -> None: ...

	@property
	def SpeedLeft(self) -> any: ...

	@SpeedLeft.setter
	def SpeedLeft(self, value: any) -> None: ...

	@property
	def LastSP(self) -> any: ...

	@LastSP.setter
	def LastSP(self, value: any) -> None: ...

	@property
	def LastGrace(self) -> any: ...

	@LastGrace.setter
	def LastGrace(self, value: any) -> None: ...

	@property
	def LastEat(self) -> any: ...

	@LastEat.setter
	def LastEat(self, value: any) -> None: ...

	@property
	def Level(self) -> any: ...

	@Level.setter
	def Level(self, value: any) -> None: ...

	@property
	def Face(self) -> any: ...

	@Face.setter
	def Face(self, value: any) -> None: ...

	@property
	def Anim(self) -> any: ...

	@Anim.setter
	def Anim(self, value: any) -> None: ...

	@property
	def AnimSpeed(self) -> any: ...

	@AnimSpeed.setter
	def AnimSpeed(self, value: any) -> None: ...

	@property
	def AttackType(self) -> any: ...

	@AttackType.setter
	def AttackType(self, value: any) -> None: ...

	@property
	def BeenApplied(self) -> any: ...

	@BeenApplied.setter
	def BeenApplied(self, value: any) -> None: ...

	@property
	def Identified(self) -> any: ...

	@Identified.setter
	def Identified(self, value: any) -> None: ...

	@property
	def Alive(self) -> any: ...

	@Alive.setter
	def Alive(self, value: any) -> None: ...

	@property
	def DungeonMaster(self) -> any: ...

	@DungeonMaster.setter
	def DungeonMaster(self, value: any) -> None: ...

	@property
	def WasDungeonMaster(self) -> any: ...

	@WasDungeonMaster.setter
	def WasDungeonMaster(self, value: any) -> None: ...

	@property
	def Applied(self) -> any: ...

	@Applied.setter
	def Applied(self, value: any) -> None: ...

	@property
	def Unpaid(self) -> any: ...

	@Unpaid.setter
	def Unpaid(self, value: any) -> None: ...

	@property
	def Monster(self) -> any: ...

	@property
	def Friendly(self) -> any: ...

	@Friendly.setter
	def Friendly(self, value: any) -> None: ...

	@property
	def Generator(self) -> any: ...

	@property
	def Thrown(self) -> any: ...

	@property
	def CanSeeInvisible(self) -> any: ...

	@CanSeeInvisible.setter
	def CanSeeInvisible(self, value: any) -> None: ...

	@property
	def Rollable(self) -> any: ...

	@Rollable.setter
	def Rollable(self, value: any) -> None: ...

	@property
	def Turnable(self) -> any: ...

	@Turnable.setter
	def Turnable(self, value: any) -> None: ...

	@property
	def UsedUp(self) -> any: ...

	@UsedUp.setter
	def UsedUp(self, value: any) -> None: ...

	@property
	def Splitting(self) -> any: ...

	@property
	def Blind(self) -> any: ...

	@Blind.setter
	def Blind(self, value: any) -> None: ...

	@property
	def CanUseSkill(self) -> any: ...

	@property
	def KnownCursed(self) -> any: ...

	@KnownCursed.setter
	def KnownCursed(self, value: any) -> None: ...

	@property
	def Stealthy(self) -> any: ...

	@Stealthy.setter
	def Stealthy(self, value: any) -> None: ...

	@property
	def Confused(self) -> any: ...

	@Confused.setter
	def Confused(self, value: any) -> None: ...

	@property
	def Sleeping(self) -> any: ...

	@Sleeping.setter
	def Sleeping(self, value: any) -> None: ...

	@property
	def Lifesaver(self) -> any: ...

	@Lifesaver.setter
	def Lifesaver(self, value: any) -> None: ...

	@property
	def Floor(self) -> any: ...

	@property
	def HasXRays(self) -> any: ...

	@HasXRays.setter
	def HasXRays(self, value: any) -> None: ...

	@property
	def CanUseRing(self) -> any: ...

	@property
	def CanUseBow(self) -> any: ...

	@property
	def CanUseWand(self) -> any: ...

	@property
	def CanSeeInDark(self) -> any: ...

	@CanSeeInDark.setter
	def CanSeeInDark(self, value: any) -> None: ...

	@property
	def KnownMagical(self) -> any: ...

	@KnownMagical.setter
	def KnownMagical(self, value: any) -> None: ...

	@property
	def CanUseWeapon(self) -> any: ...

	@property
	def CanUseArmour(self) -> any: ...

	@property
	def CanUseScroll(self) -> any: ...

	@property
	def CanCastSpell(self) -> any: ...

	@property
	def ReflectSpells(self) -> any: ...

	@ReflectSpells.setter
	def ReflectSpells(self, value: any) -> None: ...

	@property
	def ReflectMissiles(self) -> any: ...

	@ReflectMissiles.setter
	def ReflectMissiles(self, value: any) -> None: ...

	@property
	def Unique(self) -> any: ...

	@Unique.setter
	def Unique(self, value: any) -> None: ...

	@property
	def RunAway(self) -> any: ...

	@RunAway.setter
	def RunAway(self, value: any) -> None: ...

	@property
	def Scared(self) -> any: ...

	@Scared.setter
	def Scared(self, value: any) -> None: ...

	@property
	def Undead(self) -> any: ...

	@Undead.setter
	def Undead(self, value: any) -> None: ...

	@property
	def BlocksView(self) -> any: ...

	@BlocksView.setter
	def BlocksView(self, value: any) -> None: ...

	@property
	def HitBack(self) -> any: ...

	@HitBack.setter
	def HitBack(self, value: any) -> None: ...

	@property
	def StandStill(self) -> any: ...

	@StandStill.setter
	def StandStill(self, value: any) -> None: ...

	@property
	def OnlyAttack(self) -> any: ...

	@OnlyAttack.setter
	def OnlyAttack(self, value: any) -> None: ...

	@property
	def MakeInvisible(self) -> any: ...

	@MakeInvisible.setter
	def MakeInvisible(self, value: any) -> None: ...

	@property
	def Money(self) -> any: ...

	@property
	def Type(self) -> any: ...

	@property
	def Subtype(self) -> any: ...

	@property
	def Value(self) -> any: ...

	@Value.setter
	def Value(self, value: any) -> None: ...

	@property
	def ArchName(self) -> any: ...

	@property
	def Archetype(self) -> any: ...

	@property
	def OtherArchetype(self) -> any: ...

	@property
	def Exists(self) -> any: ...

	@property
	def NoSave(self) -> any: ...

	@NoSave.setter
	def NoSave(self, value: any) -> None: ...

	@property
	def Env(self) -> any: ...

	@property
	def MoveType(self) -> any: ...

	@MoveType.setter
	def MoveType(self, value: any) -> None: ...

	@property
	def MoveBlock(self) -> any: ...

	@MoveBlock.setter
	def MoveBlock(self, value: any) -> None: ...

	@property
	def MoveAllow(self) -> any: ...

	@MoveAllow.setter
	def MoveAllow(self, value: any) -> None: ...

	@property
	def MoveOn(self) -> any: ...

	@MoveOn.setter
	def MoveOn(self, value: any) -> None: ...

	@property
	def MoveOff(self) -> any: ...

	@MoveOff.setter
	def MoveOff(self, value: any) -> None: ...

	@property
	def MoveSlow(self) -> any: ...

	@MoveSlow.setter
	def MoveSlow(self, value: any) -> None: ...

	@property
	def MoveSlowPenalty(self) -> any: ...

	@property
	def Owner(self) -> any: ...

	@Owner.setter
	def Owner(self, value: any) -> None: ...

	@property
	def Enemy(self) -> any: ...

	@Enemy.setter
	def Enemy(self, value: any) -> None: ...

	@property
	def Count(self) -> any: ...

	@property
	def GodGiven(self) -> any: ...

	@GodGiven.setter
	def GodGiven(self, value: any) -> None: ...

	@property
	def IsPet(self) -> any: ...

	@IsPet.setter
	def IsPet(self, value: any) -> None: ...

	@property
	def AttackMovement(self) -> any: ...

	@AttackMovement.setter
	def AttackMovement(self, value: any) -> None: ...

	@property
	def Duration(self) -> any: ...

	@Duration.setter
	def Duration(self, value: any) -> None: ...

	@property
	def GlowRadius(self) -> any: ...

	@GlowRadius.setter
	def GlowRadius(self, value: any) -> None: ...

	@property
	def Animated(self) -> any: ...

	@Animated.setter
	def Animated(self, value: any) -> None: ...

	@property
	def NoDamage(self) -> any: ...

	@NoDamage.setter
	def NoDamage(self, value: any) -> None: ...

	@property
	def RandomMovement(self) -> any: ...

	@RandomMovement.setter
	def RandomMovement(self, value: any) -> None: ...

	@property
	def Material(self) -> any: ...

	@property
	def Container(self) -> any: ...

	@property
	def ItemPower(self) -> any: ...

	@ItemPower.setter
	def ItemPower(self, value: any) -> None: ...

	def Remove(self) -> any: ...

	def Apply(self) -> any: ...

	def Drop(self) -> any: ...

	def Clone(self) -> any: ...

	def Split(self) -> any: ...

	def Fix(self) -> any: ...

	def Say(self) -> any: ...

	def Speak(self) -> any: ...

	def Take(self) -> any: ...

	def Teleport(self) -> any: ...

	def Reposition(self) -> any: ...

	def QueryName(self) -> any: ...

	def GetResist(self) -> any: ...

	def SetResist(self) -> any: ...

	def ActivateRune(self) -> any: ...

	def CheckTrigger(self) -> any: ...

	def Cast(self) -> any: ...

	def LearnSpell(self) -> any: ...

	def ForgetSpell(self) -> any: ...

	def KnowSpell(self) -> any: ...

	def CastAbility(self) -> any: ...

	def PayAmount(self) -> any: ...

	def Pay(self) -> any: ...

	def CheckInventory(self) -> any: ...

	def CheckArchInventory(self) -> any: ...

	def OutOfMap(self) -> any: ...

	def CreateObject(self) -> any: ...

	def InsertInto(self) -> any: ...

	def ReadKey(self) -> any: ...

	def WriteKey(self, key: str, value: str, add_key: int=0) -> bool:
		"""
Add a key with the specified value to the object.
:param key Key name.
:param value Value to give the key.
:param add_key If 1 then the key is set, if 0 then the key is only updated if it exists.
:return True if the key was added or updated, False else.
		"""
	...

	def CreateTimer(self) -> any: ...

	def AddExp(self) -> any: ...

	def Move(self) -> any: ...

	def MoveTo(self) -> any: ...

	def ChangeAbil(self) -> any: ...

	def Event(self) -> any: ...

	def RemoveDepletion(self) -> any: ...

	def Arrest(self) -> any: ...

	def PermExp(self) -> any: ...

class Player(Object):

	@property
	def Title(self) -> any: ...

	@Title.setter
	def Title(self, value: any) -> None: ...

	@property
	def IP(self) -> any: ...

	@property
	def MarkedItem(self) -> Object:
		"""
Marked item, used by some actions.
		"""
	...

	@MarkedItem.setter
	def MarkedItem(self, value: Object) -> None:
		"""
Marked item, used by some actions.
		"""
	...

	@property
	def Party(self) -> any: ...

	@Party.setter
	def Party(self, value: any) -> None: ...

	@property
	def BedMap(self) -> any: ...

	@BedMap.setter
	def BedMap(self, value: any) -> None: ...

	@property
	def BedX(self) -> any: ...

	@BedX.setter
	def BedX(self, value: any) -> None: ...

	@property
	def BedY(self) -> any: ...

	@BedY.setter
	def BedY(self, value: any) -> None: ...

	@property
	def Transport(self) -> any: ...

	def Message(self) -> any: ...

	def Write(self) -> any: ...

	def CanPay(self) -> any: ...

	def QuestStart(self) -> any: ...

	def QuestGetState(self) -> any: ...

	def QuestSetState(self) -> any: ...

	def QuestWasCompleted(self) -> any: ...

	def KnowledgeKnown(self) -> any: ...

	def GiveKnowledge(self) -> any: ...

class Map:

	@property
	def Difficulty(self) -> any: ...

	@property
	def Path(self) -> any: ...

	@Path.setter
	def Path(self, value: any) -> None: ...

	@property
	def TempName(self) -> any: ...

	@property
	def Name(self) -> any: ...

	@property
	def ResetTime(self) -> any: ...

	@property
	def ResetTimeout(self) -> any: ...

	@property
	def Players(self) -> any: ...

	@property
	def Light(self) -> any: ...

	@property
	def Darkness(self) -> any: ...

	@property
	def Width(self) -> any: ...

	@property
	def Height(self) -> any: ...

	@property
	def EnterX(self) -> any: ...

	@property
	def EnterY(self) -> any: ...

	@property
	def Message(self) -> any: ...

	@property
	def Region(self) -> any: ...

	@property
	def Unique(self) -> any: ...

	def Print(self) -> any: ...

	def ObjectAt(self) -> any: ...

	def CreateObject(self) -> any: ...

	def Check(self) -> any: ...

	def Next(self) -> any: ...

	def Insert(self) -> any: ...

	def InsertAround(self) -> any: ...

	def ChangeLight(self) -> any: ...

	def TriggerConnected(self) -> any: ...

class Party:

	@property
	def Name(self) -> any: ...

	@property
	def Password(self) -> any: ...

	@property
	def Next(self) -> any: ...

	def GetPlayers(self) -> any: ...

class Region:

	@property
	def Name(self) -> any: ...

	@property
	def Longname(self) -> any: ...

	@property
	def Message(self) -> any: ...

	@property
	def Next(self) -> any: ...

	@property
	def JailX(self) -> any: ...

	@property
	def JailY(self) -> any: ...

	@property
	def JailPath(self) -> any: ...

	def GetParent(self) -> any: ...

class Archetype:

	@property
	def Name(self) -> any: ...

	@property
	def Next(self) -> any: ...

	@property
	def More(self) -> any: ...

	@property
	def Head(self) -> any: ...

	@property
	def Clone(self) -> any: ...

	def NewObject(self) -> any: ...

class Direction(enum):
	NORTH = 1
	NORTHEAST = 2
	EAST = 3
	SOUTHEAST = 4
	SOUTH = 5
	SOUTHWEST = 6
	WEST = 7
	NORTHWEST = 8

class Type(enum):
	PLAYER = 1
	TRANSPORT = 2
	ROD = 3
	TREASURE = 4
	POTION = 5
	FOOD = 6
	POISON = 7
	BOOK = 8
	CLOCK = 9
	DRAGON_FOCUS = 10
	ARROW = 13
	BOW = 14
	WEAPON = 15
	ARMOUR = 16
	PEDESTAL = 17
	ALTAR = 18
	LOCKED_DOOR = 20
	SPECIAL_KEY = 21
	MAP = 22
	DOOR = 23
	KEY = 24
	TIMED_GATE = 26
	TRIGGER = 27
	GRIMREAPER = 28
	MAGIC_EAR = 29
	TRIGGER_BUTTON = 30
	TRIGGER_ALTAR = 31
	TRIGGER_PEDESTAL = 32
	SHIELD = 33
	HELMET = 34
	MONEY = 36
	CLASS = 37
	AMULET = 39
	PLAYERMOVER = 40
	TELEPORTER = 41
	CREATOR = 42
	SKILL = 43
	EARTHWALL = 45
	GOLEM = 46
	THROWN_OBJ = 48
	BLINDNESS = 49
	GOD = 50
	DETECTOR = 51
	TRIGGER_MARKER = 52
	DEAD_OBJECT = 53
	DRINK = 54
	MARKER = 55
	HOLY_ALTAR = 56
	PLAYER_CHANGER = 57
	BATTLEGROUND = 58
	PEACEMAKER = 59
	GEM = 60
	FIREWALL = 62
	CHECK_INV = 64
	MOOD_FLOOR = 65
	EXIT = 66
	ENCOUNTER = 67
	SHOP_FLOOR = 68
	SHOP_MAT = 69
	RING = 70
	FLOOR = 71
	FLESH = 72
	INORGANIC = 73
	SKILL_TOOL = 74
	LIGHTER = 75
	WALL = 77
	MISC_OBJECT = 79
	MONSTER = 80
	LAMP = 82
	DUPLICATOR = 83
	SPELLBOOK = 85
	CLOAK = 87
	SPINNER = 90
	GATE = 91
	BUTTON = 92
	CF_HANDLE = 93
	HOLE = 94
	TRAPDOOR = 95
	SIGN = 98
	BOOTS = 99
	GLOVES = 100
	SPELL = 101
	SPELL_EFFECT = 102
	CONVERTER = 103
	BRACERS = 104
	POISONING = 105
	SAVEBED = 106
	WAND = 109
	SCROLL = 111
	DIRECTOR = 112
	GIRDLE = 113
	FORCE = 114
	POTION_RESIST_EFFECT = 115
	EVENT_CONNECTOR = 116
	CLOSE_CON = 121
	CONTAINER = 122
	ARMOUR_IMPROVER = 123
	WEAPON_IMPROVER = 124
	SKILLSCROLL = 130
	DEEP_SWAMP = 138
	IDENTIFY_ALTAR = 139
	SHOP_INVENTORY = 150
	RUNE = 154
	TRAP = 155
	POWER_CRYSTAL = 156
	CORPSE = 157
	DISEASE = 158
	SYMPTOM = 159
	BUILDER = 160
	MATERIAL = 161
	MIMIC = 162
	LIGHTABLE = 163

class Move(enum):
	WALK = 1
	FLY_LOW = 2
	FLY_HIGH = 4
	FLYING = 6
	SWIM = 8
	BOAT = 16
	ALL = 31

class MessageFlag(enum):
	NDI_BLACK = 0
	NDI_WHITE = 1
	NDI_NAVY = 2
	NDI_RED = 3
	NDI_ORANGE = 4
	NDI_BLUE = 5
	NDI_DK_ORANGE = 6
	NDI_GREEN = 7
	NDI_LT_GREEN = 8
	NDI_GREY = 9
	NDI_BROWN = 10
	NDI_GOLD = 11
	NDI_TAN = 12
	NDI_UNIQUE = 256
	NDI_ALL = 512
	NDI_ALL_DMS = 1024

class AttackType(enum):
	PHYSICAL = 1
	MAGIC = 2
	FIRE = 4
	ELECTRICITY = 8
	COLD = 16
	CONFUSION = 32
	ACID = 64
	DRAIN = 128
	WEAPONMAGIC = 256
	GHOSTHIT = 512
	POISON = 1024
	SLOW = 2048
	PARALYZE = 4096
	TURN_UNDEAD = 8192
	FEAR = 16384
	CANCELLATION = 32768
	DEPLETE = 65536
	DEATH = 131072
	CHAOS = 262144
	COUNTERSPELL = 524288
	GODPOWER = 1048576
	HOLYWORD = 2097152
	BLIND = 4194304
	INTERNAL = 8388608
	LIFE_STEALING = 16777216
	DISEASE = 33554432

class AttackTypeNumber(enum):
	PHYSICAL = 0
	MAGIC = 1
	FIRE = 2
	ELECTRICITY = 3
	COLD = 4
	CONFUSION = 5
	ACID = 6
	DRAIN = 7
	WEAPONMAGIC = 8
	GHOSTHIT = 9
	POISON = 10
	SLOW = 11
	PARALYZE = 12
	TURN_UNDEAD = 13
	FEAR = 14
	CANCELLATION = 15
	DEPLETE = 16
	DEATH = 17
	CHAOS = 18
	COUNTERSPELL = 19
	GODPOWER = 20
	HOLYWORD = 21
	BLIND = 22
	INTERNAL = 23
	LIFE_STEALING = 24
	DISEASE = 25

class EventType(enum):
	APPLY = 1
	ATTACK = 2
	ATTACKS = 33
	BOUGHT = 34
	CLOSE = 11
	DEATH = 3
	DESTROY = 13
	DROP = 4
	PICKUP = 5
	SAY = 6
	SELLING = 32
	STOP = 7
	TIME = 8
	THROW = 9
	TRIGGER = 10
	TIMER = 12
	USER = 31
	BORN = 14
	CLOCK = 15
	CRASH = 16
	GKILL = 18
	KICK = 28
	LOGIN = 19
	LOGOUT = 20
	MAPENTER = 21
	MAPLEAVE = 22
	MAPLOAD = 30
	MAPRESET = 23
	MAPUNLOAD = 29
	MUZZLE = 27
	PLAYER_DEATH = 17
	REMOVE = 24
	SHOUT = 25
	TELL = 26

HOURS_PER_DAY = 28
DAYS_PER_WEEK = 7
WEEKS_PER_MONTH = 5
MONTHS_PER_YEAR = 17
SEASONS_PER_YEAR = 5
PERIODS_PER_DAY = 6

SAY = 0
REPLY = 1
QUESTION = 2

DISTATT = 1
RUNATT = 2
HITRUN = 3
WAITATT = 4
RUSH = 5
ALLRUN = 6
DISTHIT = 7
WAIT2 = 8
PETMOVE = 16
CIRCLE1 = 32
CIRCLE2 = 48
PACEH = 64
PACEH2 = 80
RANDO = 96
RANDO2 = 112
PACEV = 128
PACEV2 = 144

LogError = 1
LogInfo = 2
LogDebug = 3
LogMonster = 4
