{
  "rules": [
  {
  "match" : ["treasure"],
  "pre" : [["quest", "wolfsburg/treasure-island", "=10"], ["npctoken", "state", "job"]],
  "post" : [["quest", "wolfsburg/treasure-island", "20"]],
  "msg" : ["Yarh, I do happen. You need a magic shovel. Talk to my friend Long John Silver in this tavern, he knows more than I do."]
  }, {
  "match" : ["pirate", "job"],
  "pre" : [["quest", "wolfsburg/treasure-island", "=10"]],
  "post" : [["setnpctoken", "state", "job"]],
  "msg" : ["I search the seven seas looking for treasure."],
  "replies" : [["treasure", "Talking of treasure, you don't happen to know anything about the so-called treasure island?", "2"]]
  }, {
  "match" : ["name"],
  "pre" : [],
  "post" : [],
  "msg" : ["Arrr, I am Black Beard the pirate!"],
  "replies" : [["job", "So, what is your, arrr, job?", "2"]]
  }, {
  "match" : ["pirate", "job"],
  "pre" : [],
  "post" : [],
  "msg" : ["I search the seven seas looking for treasure, arrr!"],
  "replies" : [["treasure", "Do you know where I can find some treasure?", "2"]]
  }, {
  "match" : ["treasure"],
  "pre" : [],
  "post" : [],
  "msg" : ["Yaarr, it would not be so easy if I told ye everything!"]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["ARRRRRRR MATEY!!!!!"],
  "replies" : [["name", "What is your name, erm, arrr?", "2"]]
  }
]}
