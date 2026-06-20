{ "location"   : "zel_princess",
  "rules"      :
  [{ "match"   : ["help"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["I've been able to subsidize the increase for Rudy so far. As long as the Court doesn't find out, I should be able to keep doing it. I do appreciate the offer, though."]
   },
   { "match"   : ["reason"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["I've tried talking some sense into them, but they refuse to see their absolutism for what it is. They've even raised the taxes on Rudy Oneeye over in the magic shop in retaliation for being a dragon! Can you imagine? Rudy's been here for *ages*, longer than some of them have even been alive.\nSomehow ol' Mosely's escaped their notice, but I wonder for how long."],
     "replies" : [["help", "Maybe I can help?", "6"]
                 ]
   },
   { "match"   : ["dress"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["Gavarthyrax has offered to conveniently destroy the dress the night before the jubilee. That gives little time for it to be repaired, and hopefully gives me cover for not going."]
   },
   { "match"   : ["paid"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["What, did you think I'd have a dragon risk their life in my dungeon for free? Nonono. That would be cruel."]
   },
   { "match"   : ["talk"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["Oh, commoner, you clearly don't understand the awful mess of formal manners that'll be expected of me if I go. Not talking to people while there would be a slight against them, tarnishing the image of the kingdom itself."],
     "replies" : [["kingdom", "The *whole* kingdom?", "8"]
                 ]
   },
   { "match"   : ["ransom"],
     "pre"     : ["quest", "scorn/Aristocracy", "10-60"],
     "post"    : [],
     "msg"     : ["I'm surprised they haven't mentioned anything to you yet, seeing how you keep wandering into the castle looking for quests to do. Ah well, I'm sure they'll have you do their dirty work soon enough. The Royal Court is clamping down on *all* dragons, regardless of affiliation, as a result of the situation."],
     "replies" : [["reason", "Surely they're open to reason?", "5"]
                 ]
   },
   { "match"   : ["ransom"],
     "pre"     : ["quest", "scorn/Aristocracy", "70-90"],
     "post"    : [],
     "msg"     : ["Well, not anymore. I hear some hero went and stole an artifact from the group of dragons making the ransom in order to give my father some leverage. Hasn't caused the Royal Court to be any less absolutist about dragons, though."],
     "replies" : [["reason", "Surely they're open to reason?", "5"]
                 ]
   },
   { "match"   : ["ransom"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["There you go, jumping to absolutes. A *specific* group of dragons is ransoming Scorn. Most dragons don't even interact with them. And now the Royal Court is leery of dragons as a whole."],
     "replies" : [["reason", "Surely they're open to reason?", "5"]
                 ]
   },
   { "match"   : ["made"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["Well, it's only more dangerous if the elementals or the skeletons get out. The electric dragon has a stash of amulets of lifesaving, and is paid well for their role here."],
     "replies" : [["paid", "So, the electric dragon is paid to be here?", "10"]
                 ]
   },
   { "match"   : ["friend"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["We had a chance encounter back then. I was on an official trip, and stopped at Hermes' Inn. Some giants tried to cause trouble at the inn, and Gavarthyrax decided to defend the inn as he was passing by. Goofball over here still won't tell me his justification for doing so.\n*Gavarthyrax grins cheekily*\nAfter that, he started dropping in for a chat from time to time. Was even on the up and up with the Court until a different group of dragons started trying to ransom Scorn."],
     "replies" : [["ransom", "Dragons are ransoming Scorn?", "2"]
                 ]
   },
   { "match"   : ["why"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["I dunno. It felt more, interesting, more fulfilling that the vapid posturing of noble life. I look at this and realize that I did something. Made something. Plenty of nobles really only know how to make money. It's disheartening."],
     "replies" : [["made", "And making a dungeon is fulfilling? Doesn't that just make more dangerous places around?", "9"]
                 ]
   },
   { "match"   : ["be"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["I... I'm still figuring that out, to be honest. Taking the time to reframe how I look at the world and see what really is rather than what I was told to see has been, well, challenging. And through that journey I've been finding bits and pieces of myself, things I'd been taught to hold inside and never let out. I've ultimately come to realize that nobility is less about making things and more about taking credit for things done at your behest, and that irks me for reasons I haven't yet figured out. Building this dungeon with Gavarthyrax? That's something that fills the void inside."]
   },
   { "match"   : ["dragon"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["Oh, Gavarthyrax? We've been friends for a long time. Since I was 10, I think."],
     "replies" : [["friend", "How did you two become friends, then?", "4"]
                 ]
   },
   { "match"   : ["go"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["I, well, just don't. I don't want to wear the fancy, bulky, unwieldy dress I'll be expected to wear. I don't want to make small talk with the same cadre of nobles I've seen my entire life. And I don't want to be lectured over spending my time out here. The Royal Court, erm, really frowns upon me associating with dragons. Even ones that have nothing to do with the ridiculous ransom."],
     "replies" : [["dress", "What if something happened to that dress at the last moment?", "2"],
                  ["talk", "What if you just don't talk to people?", "2"],
                  ["ransom", "Dragons are ransoming Scorn?", "2"]
                 ]
   },
   { "match"   : ["summons"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["A feast to celebrate my father's 60th year of rule. And yet, I don't want to go."],
     "replies" : [["go", "Why not go?", "1"]
                 ]
   },
   { "match"   : ["princess"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["This? Oh, I made this. With the help of Gavarthyrax here, of course."],
     "replies" : [["why", "Why build a dungeon?", "3"]
                 ]
   },
   { "match"   : ["casual"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["It's always proper this, and proper that. What if I just want to be me?"],
     "replies" : [["be", "And what does being you entail?", "7"]
                 ]
   },
   { "match"   : ["*"],
     "pre"     : [],
     "post"    : [],
     "msg"     : ["*sigh* I'd much rather stay here than abide by that Royal Summons."],
     "replies" : [["dragon", "So, uh, what's with the dragon?", "0"],
                  ["summons", "A Summons? That sounds interesting.", "0"],
                  ["princess", "What is princess doing in the countryside in a dungeon, anyway?", "0"],
                  ["casual", "I'm surprised a princess is so willing to talk so casually. Especially in front of company.", "0"]
                 ]
   }
  ]
}
