{
  "location" : "test_grandpa_01",
  "rules": [
  {
  "match" : ["gi"],
  "pre" : [],
  "post" : [["giveitem", "club"]],
  "msg" : ["giving a club"]
  }, {
  "match" : ["tai"],
  "pre" : [],
  "post" : [["takeitem", "club", "0"]],
  "msg" : ["Taking all clubs"]
  }, {
  "match" : ["ti"],
  "pre" : [],
  "post" : [["takeitem", "club"]],
  "msg" : ["Taking a club"]
  }, {
  "match" : ["gm"],
  "pre" : [],
  "post" : [["giveitem", "money", "61"]],
  "msg" : ["Here you go"]
  }, {
  "match" : ["tm"],
  "pre" : [],
  "post" : [["takeitem", "money", "61"]],
  "msg" : ["Well, thanks."]
  }, {
  "match" : ["hi", "hello"],
  "pre" : [["token", "hello", "0"]],
  "post" : [["settoken", "hello", "1"]],
  "msg" : ["Hello, lad!", "Hi, young fellow!", "Howdy!"]
  }, {
  "match" : ["hi", "hello"],
  "pre" : [["token", "hello", "1"]],
  "post" : [["settoken", "hello", "*"]],
  "msg" : ["I've heard, you know, I'm not deaf *grmbl*"],
  "replies" : [["really", "Are you sure?", "1"]]
  }, {
  "match" : ["*"],
  "pre" : [["token", "hello", "*"]],
  "post" : [["settoken", "hello", "*"]],
  "msg" : ["What ?", "Huh ?", "What do you want ?"],
  "replies" : [["hi", "hello, there"]]
  }
]}
