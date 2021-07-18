{
  "location" : "scorn_riverside",
  "rules": [
  {
  "match" : ["joey"],
  "pre" : [],
  "post" : [],
  "msg" : ["Oh, Mark's friend. If you find Joey, Mark is always near by."]
  }, {
  "match" : ["mark", "where", "goth", "goths"],
  "pre" : [["quest", "scorn/CoffeeGoose", "30"]],
  "post" : [],
  "msg" : ["I can't even go to Goth's Tavern any more because Mark and Joey are always there!"]
  }, {
  "match" : ["mark"],
  "pre" : [],
  "post" : [],
  "msg" : ["That cheating bum... I hope I never see him again after I saw him with that lady!"]
  }, {
  "match" : ["door", "locked", "special"],
  "pre" : [],
  "post" : [],
  "msg" : ["Mark always keeps the key to that door with him."]
  }, {
  "match" : ["letter", "note", "ripped", "torn", "him", "cheat", "bum"],
  "pre" : [],
  "post" : [],
  "msg" : ["I don't want to talk about HIM right now."]
  }, {
  "match" : ["goose", "bird", "eswald"],
  "pre" : [["quest", "scorn/CoffeeGoose", "10-40"]],
  "post" : [],
  "msg" : ["I heard Eswald lost his goose, but... uh... I don't know anything about that."]
  }, {
  "match" : ["rent", "house", "yes", "key", "condo"],
  "pre" : [],
  "post" : [],
  "msg" : ["Ya, Condo #2 is available. 100 gold a week. Three weeks advance. I ain't fixin' nuthin so take it or leave it. Key's on the table if you want to check it out first."]
  }, {
  "match" : ["hello", "hi"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hello! Would you like to rent our Condo #2?"]
  }, {
  "match" : ["name", "job"],
  "pre" : [],
  "post" : [],
  "msg" : ["I'm Amy. The caretaker here at Riverside Manor."]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Want to rent our Condo #2?"]
  }
]}
