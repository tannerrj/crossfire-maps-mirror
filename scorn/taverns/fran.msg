{
  "location" : "scorn_riverside",
  "rules": [
  {
  "match" : ["cornerbrook"],
  "pre" : [],
  "post": [],
  "msg" : ["Just south of here."]
  }, {
  "match" : ["swabbie"],
  "pre" : [],
  "post": [],
  "msg" : ["That run down ole pirate has been hiding away at his place in Cornerbrook the last few days. Very odd."]
  }, {
  "match" : ["bird", "goose"],
  "pre" : [["token", "service", "yes"], ["quest", "scorn/CoffeeGoose", "30"]],
  "post": [],
  "msg" : ["Ya I heard Mark and Swabbie stole a goose."]
  },{
  "match" : ["bird", "goose"],
  "pre" : [["token", "service", "yes"], ["quest", "scorn/CoffeeGoose", "20"]],
  "post": [["quest", "scorn/CoffeeGoose", "30"]],
  "msg" : ["Ya I heard Mark and Swabbie stole a goose."]
  },{
  "match" : ["bird", "goose"],
  "pre" : [["token", "service", "yes"]],
  "post": [],
  "msg" : ["Ya I heard Mark and Swabbie stole a goose."]
  },{
  "match" : ["mark"],
  "pre" : [["token", "service", "yes"]],
  "post": [],
  "msg" : ["That bum, all this time he had a girl on the side. Too bad he was coming into some coin too... Some deal with that bird of his."]
  }, {
  "match" : ["amy"],
  "pre" : [["token", "service", "yes"]],
  "post": [],
  "msg" : ["She broke up with Mark. Can't blame her one bit."]
  }, {
  "match" : ["pincher"],
  "pre" : [["token", "service", "yes"]],
  "post": [],
  "msg" : ["You try it an I'll deck you I says to him..."]
  },{
  "match" : ["oled"],
  "pre" : [["token", "service", "yes"]],
  "post": [],
  "msg" : ["He's okay to work for, but he's a pincher if you know what I mean. He's usually pretty mellow, but lately he seems a bit tense."]
  },{
  "match" : ["job", "jobs"],
  "pre" : [],
  "post": [["settoken", "service", "yes"]],
  "msg" : ["Ya I work part time at Oled's Cafe too."]
  },{
  "match" : ["service", "order"],
  "pre" : [],
  "post": [["settoken", "service", "yes"]],
  "msg" : ["Hey buddy just take a seat, I work two jobs you know."]
  },{
  "match" : ["who"],
  "pre" : [],
  "post": [],
  "msg" : ["You're pretty nosey there fella."]
  },{
  "match" : ["alfalfa"],
  "pre" : [["quest", "scorn/OrcDress", "=10"]],
  "post": [["giveitem", "Alfalfa's Front Door Key"],["quest", "scorn/OrcDress", "20"]],
  "msg" : ["Alfalfa sent you to get the key to her house? Ok then, here you go."]
  },{
  "match" : ["*"],
  "pre" : [],
  "post": [],
  "msg" : ["Hey kitchen is off limits! Keep it in your scabbard and take a seat there chum."]
  }
]}
