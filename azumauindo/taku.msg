{
  "location" : "world_126_104",
  "rules": [
  {
  "match" : ["sail"],
  "pre" : [["quest", "quests/Azumauindo", "60"]],
  "post" : [],
  "msg" : ["Sorry, $me will be very busy fishing."]
  }, {
  "match" : ["boat"],
  "pre" : [["quest", "quests/Azumauindo", "60"]],
  "post" : [],
  "msg" : ["Fun story! Azumauindo men are very kind, so they gave me a new boat."]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "60"]],
  "post" : [],
  "msg" : ["Hum de dum, another day for $me to go fishing!"],
  "replies" : [["sail", "Can we set sail to Azumauindo again?"], ["boat", "How did you get a new boat?"]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["When you're ready to set sail, get in the boat."]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "30"], ["item", "fishfood", "10"]],
  "post" : [["quest", "quests/Azumauindo", "40"], ["takeitem", "fishfood", "10"]],
  "msg" : ["Ahh, wonderful! When $you is ready to go, get in $me's boat and $me will take you."]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "quests/Azumauindo", "30"]],
  "post" : [],
  "msg" : ["$me will be waiting for $you to return."]
  }, {
  "match" : ["fish"],
  "pre" : [["quest", "quests/Azumauindo", "20"]],
  "post" : [["quest", "quests/Azumauindo", "30"]],
  "msg" : ["10 fish to make it worth $me while!"],
  "replies" : [["okay", "Okay, I'll get you some fish."]]
  }, {
  "match" : ["azumauindo"],
  "pre" : [["quest", "quests/Azumauindo", "20"]],
  "post" : [],
  "msg" : ["Oooh, you want $me take $you to Azumauindo? $me will do, if you can give $me his day's fish!"],
  "replies" : [["fish", "Sure, how much fish do you want?"]]
  }, {
  "match" : ["doing"],
  "pre" : [["quest", "quests/Azumauindo", "20"]],
  "post" : [],
  "msg" : ["$me is going fishing!"],
  "replies" : [["azumauindo", "Could you take me to Azumauindo?"]]
  }, {
  "match" : ["where"],
  "pre" : [],
  "post" : [],
  "msg" : ["Where does $you want to go? $me is only simple fisherman.\n\n(Come back when you know where you want to go.)"]
  }, {
  "match" : ["doing"],
  "pre" : [],
  "post" : [],
  "msg" : ["$me is going fishing!"],
  "replies" : [["where", "Where can you take me?"]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "30"], ["item", "fishfood", "10"]],
  "post" : [],
  "msg" : ["Has $you brought $me his fish yet?"],
  "replies" : [["yes", "Yes, here you go."], ["no", "No, not yet."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "30"]],
  "post" : [],
  "msg" : ["Has $you brought $me his fish yet?"],
  "replies" : [["no", "No, not yet."]]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hum de dum, another day for $me to go fishing!"],
  "replies" : [["doing", "What are you doing out here?"]]
  }
]}
