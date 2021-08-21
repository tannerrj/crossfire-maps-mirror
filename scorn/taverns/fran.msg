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
  "match" : ["alfalfa", "dress", "key"],
  "pre" : [["quest", "scorn/OrcDress", "=50"], ["item", "Alfalfa's Front Door Key"]],
  "post": [["takeitem", "Alfalfa's Front Door Key"]],
  "msg" : ["Thanks SO much!  Alfalfa appreciates you, even though they won't let her out.  Have you talked to the Magistrate in the castle yet?  Maybe you can win their favor."]
  },{
  "match" : ["alfalfa", "dress", "key"],
  "pre" : [["quest", "scorn/OrcDress", "=50"]],
  "post": [],
  "msg" : ["Alfalfa appreciates you getting her dress, even though they won't let her out of prison.  Have you talked to the Magistrate in the castle yet?  Maybe you can win their favor."]
  },{
  "match" : ["alfalfa", "dress", "key"],
  "pre" : [["quest", "scorn/OrcDress", "20-40"], ["item", "Alfalfa's Front Door Key"]],
  "post": [],
  "msg" : ["You are so nice for offering to retrieve her dress for her.  She takes good care of her friends."]
  },{
  "match" : ["alfalfa", "key"],
  "pre" : [["quest", "scorn/OrcDress", "20-40"]],
  "post": [["giveitem", "Alfalfa's Front Door Key"]],
  "msg" : ["Did you lose Alfalfa's key?!  Good thing someone found it and returned it... one more time."]
  },{
  "match" : ["alfalfa", "key"],
  "pre" : [["quest", "scorn/OrcDress", "=10"]],
  "post": [["giveitem", "Alfalfa's Front Door Key"],["quest", "scorn/OrcDress", "20"]],
  "msg" : ["Alfalfa sent you to get the key to her house?  Ok then, here you go."]
  },{
  "match" : ["*"],
  "pre" : [],
  "post": [],
  "msg" : ["Hey kitchen is off limits! Keep it in your scabbard and take a seat there chum."]
  }
]}
