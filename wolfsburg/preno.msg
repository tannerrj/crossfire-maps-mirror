{
  "location" : "wolfsburg",
  "rules": [
  {
  "match" : ["*"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=50"]],
  "post" : [],
  "msg" : ["Hello $you, I hope you are still hunting dragons with all your power!"]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=40"], ["quest", "quests/Nilplur", "=30"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""], ["quest", "wolfsburg/dragon-hunter", "50"], ["giveknowledge", "alchemy:4:15834:Assassinating Dragons"], ["giveknowledge", "alchemy:4:13394:Assassinating Dragons"]],
  "msg" : ["Impressive!\n\nWell, you obviously proved your worth in dragon hunting, thus I can safely give you my secret for missiles against them.\n\nMy recipe is to combine a scorpion's stinger, some water of emerald, a dragon's heart, and the projectiles.\n\nWith this, you can kill those beasts in a single shot!"]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=40"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Hum, somehow I don't believe you..."]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=40"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Hunting is quite a challenge, you obviously aren't experienced enough, keep trying!"]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=40"]],
  "post" : [["setnpctoken", "state", "ask"]],
  "msg" : ["Welcome back $you, how is your hunting coming along? Did you slay Nilplur?"],
  "replies" : [["yes", "Yes, really easy if you ask me.", "0"], ["no", "No, I'm still searching its traces.", "0"]]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=30"], ["item", "black dragon scale"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""], ["quest", "wolfsburg/dragon-hunter", "40"], ["takeitem", "black dragon scale"]],
  "msg" : ["Great!\n\nAs your last challenge, I'd like you to prove you are a hunter.\n\nPlease find and slay Nilplur the dragon."]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=30"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Sorry, but you don't seem to have it..."]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=30"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["I'm sure you'll manage to eventually find one."]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=30"]],
  "post" : [["setnpctoken", "state", "ask"]],
  "msg" : ["Welcome back $you, what about that black dragon scale?"],
  "replies" : [["yes", "Yes, it wasn't simple, but here it is.", "0"], ["no", "No, unfortunately, those are pretty rare it seems...", "0"]]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=20"], ["item", "blue dragon scales", "3"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""], ["quest", "wolfsburg/dragon-hunter", "30"], ["takeitem", "blue dragon scales", "3"]],
  "msg" : ["Well done!\n\nBut I'm afraid that's not yet enough...\n\nWhat about bringing me a black dragon scale?"]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=20"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Where are they, then?"]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=20"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Come on, blue dragons aren't that uncommon, are they?"]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=20"]],
  "post" : [["setnpctoken", "state", "ask"]],
  "msg" : ["Hello $you, did you find blue dragon scales?"],
  "replies" : [["yes", "Yes, of course!", "0"], ["no", "No, I didn't yet kill enough dragons.", "0"]]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=10"], ["item", "red dragon scales", "5"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""], ["quest", "wolfsburg/dragon-hunter", "20"], ["takeitem", "red dragon scales", "5"]],
  "msg" : ["Great!\n\nWell, that's impressive, but red dragons are pretty common.\n\nCould you bring me 3 blue dragon scales?"]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=10"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Where are they, then?"]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=10"], ["npctoken", "state", "ask"]],
  "post" : [["setnpctoken", "state", ""]],
  "msg" : ["Ha well, next time maybe..."]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "wolfsburg/dragon-hunter", "=10"]],
  "post" : [["setnpctoken", "state", "ask"]],
  "msg" : ["Hello, so did you bring me those 5 red dragon scales?"],
  "replies" : [["yes", "Yes, of course!", "0"], ["no", "No, I didn't yet kill enough dragons.", "0"]]
  }, {
  "match" : ["share"],
  "pre" : [["npctoken", "state", "slay"]],
  "post" : [["quest", "wolfsburg/dragon-hunter", "10"]],
  "msg" : ["Well...\n\nI guess I can use any help.\n\nBut you'll have to prove your worth first!\n\nPlease bring me 5 scales of a red dragon."]
  }, {
  "match" : ["impressive"],
  "pre" : [["npctoken", "state", "weapon"]],
  "post" : [["setnpctoken", "state", "slay"]],
  "msg" : ["Ha, don't mention it...\n\nI'm particularly fond of my special missiles.\n\nThere are missiles crafted to particulary hit dragons, but mine are ever more powerful - they can slay one beast in a single shot!"],
  "replies" : [["share", "That's quite impressive, indeed... Would you consider sharing your missiles so I can help you exterminate those beasts?", "1"]]
  }, {
  "match" : ["really"],
  "pre" : [["npctoken", "state", "2"]],
  "post" : [["setnpctoken", "state", "weapon"]],
  "msg" : ["Well, yes...\n\nI even designed my own weapons to fight them!"],
  "replies" : [["impressive", "That's quite impressive!", "0"]]
  }, {
  "match" : ["why"],
  "pre" : [["npctoken", "state", "1"]],
  "post" : [["setnpctoken", "state", "2"]],
  "msg" : ["Well\n\n*shrug*\n\nI just HATE them!\n\nI hunt them, without respite, to exterminate them!"],
  "replies" : [["really", "Really? It must be quite a hard task...", "0"]]
  }, {
  "match" : ["dragon", "dragons"],
  "pre" : [["item", "preno_dragon"]],
  "post" : [["setnpctoken", "state", "1"]],
  "msg" : ["Yes, I HATE dragons!"],
  "replies" : [["why", "Why do you hate dragons?", "2"]]
  }, {
  "match" : ["*"],
  "pre" : [["item", "preno_dragon"]],
  "post" : [],
  "msg" : ["Hello stranger.\n\nFeel free to look at my collection of animated stuffed creatures -- you could swear they are real!"],
  "replies" : [["dragon", "You have quite a big dragon collection.", "0"]]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hello stranger.\n\nFeel free to look at my collection of animated stuffed creatures -- you could swear they are real!"]
  }
]}
