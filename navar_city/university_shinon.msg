{
  "location" : "navar_city/university",
  "rules": [
  {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["You have? That is quite spectacular. If you find anything of interest there, please come to me. I would be more than glad to help."]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "quests/Azumauindo", "20"]],
  "post" : [],
  "msg" : ["That's a shame. It would be an extraordinary accomplishment."]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["Welcome back. Have you found Azumauindo yet?"],
  "replies" : [["no", "No, I haven't."], ["yes", "Yes, I have."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "20"]],
  "post" : [],
  "msg" : ["Welcome back. Have you found Azumauindo yet?"],
  "replies" : [["no", "No, I haven't."]]
  }, {
  "match" : ["azumauindo"],
  "pre" : [["quest", "quests/Azumauindo", "10"]],
  "post" : [["quest", "quests/Azumauindo", "20"]],
  "msg" : ["Azumauindo is an island nation off the far-northeast corner of this continent. It has been isolated from the main land for some time. No ships from the major ports stop there."]
  }, {
  "match" : ["book"],
  "pre" : [["quest", "quests/Azumauindo", "10"]],
  "post" : [],
  "msg" : ["In my studies, I have only come across one language which matches your description. This sounds like a script from Azumauindo."],
  "replies" : [["azumauindo", "Where is Azumauindo?"]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "10"]],
  "post" : [],
  "msg" : ["Another day of studying scriptures..."],
  "replies" : [["book", "I found a strange book written with boxy runes. Could you tell me more about it?"]]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Another day of studying scriptures...\n\n(Come back when you have something to show $me.)"]
  }
]}
