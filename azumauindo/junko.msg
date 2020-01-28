{
  "location" : "azumauindo/misc/entrance1",
  "rules": [
  {
  "match" : ["sail"],
  "pre" : [["quest", "quests/Azumauindo", "100"]],
  "post" : [],
  "msg" : ["Yes, of course. Get in the boat whenever you're ready."]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "100"]],
  "post" : [],
  "msg" : ["Ah... you are the one who returned the Kabuto."],
  "replies" : [["sail", "Can you take me to Azumauindo?"]]
  }, {
  "match" : ["sail"],
  "pre" : [],
  "post" : [],
  "msg" : ["You're a foreigner! Of course not."]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hmph..."],
  "replies" : [["sail", "Can you take me to Azumauindo?"]]
  }
]}
