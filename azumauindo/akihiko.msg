{
  "location": "azumauindo/misc/crashlanding1",
  "rules": [
  {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "100"]],
  "post" : [],
  "msg" : ["Welcome back, $you. Thank you for returning the Kabuto."]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "60"], ["item", "Kabuto of Geisya"]],
  "post" : [["takeitem", "Kabuto of Geisya"], ["quest", "quests/Azumauindo", "100"]],
  "msg" : ["Is this true? Yes... yes it is. Very well adventurer, you have proven yourself worthy of entry to Azumauindo, and you are hereby granted an audience with the Shogun himself. My guards shall bring the Kabuto to him shortly."]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "60"]],
  "post" : [],
  "msg" : ["Where is it then?"]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "quests/Azumauindo", "60"]],
  "post" : [],
  "msg" : ["Return once you have the Kabuto."],
  "replies" : []
  },

  {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "50"]],
  "post" : [["quest", "quests/Azumauindo", "60"]],
  "msg" : ["Very well. You may leave. A ship will take you to the port city of Wolfsburg. Return once you have the Kabuto."]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "quests/Azumauindo", "50"]],
  "post" : [],
  "msg" : ["I will be waiting for your decision."]
  }, {
  "match" : ["kabuto"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [["quest", "quests/Azumauindo", "50"]],
  "msg" : ["It is a sacred relic of ours, lost long ago. Our library here will have information on where it may be. If you can somehow retrieve this artifact for us, you may enter Azumauindo. Will you do this?"],
  "replies" : [["no", "No, let me think about it."], ["yes", "Yes, I will."]]
  }, {
  "match" : ["trust"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["There... is something you can do. Have you heard of the Kabuto of Geisya?"],
  "replies" : [["kabuto", "Kabuto of Geisya?"]]
  }, {
  "match" : ["shogun"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["He is our leader. He mistrusts foreigners, and with good reason."],
  "replies" : [["trust", "How can I earn his trust?"]]
  }, {
  "match" : ["leave"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["You are a foreigner. The Shogun forbids foreigners from entering Azumauindo. Traveling here was an egregious offense."],
  "replies" : [["shogun", "Who is the Shogun? Why does he forbid foreigners from entering?"]]
  },
  {
  "match" : ["gates"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["Why, to prevent you from leaving, of course."],
  "replies" : [["leave", "Wait, I can't leave?"]]
  },

  {
  "match" : ["who"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["I am Akhihiko. My men and I guard the coasts of Azumauindo."],
  "replies" : [["gates", "Why are there gates blocking the doors?"]]
  }, {
  "match" : ["city"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["Yes, Azumauindo, the city of the East Wind. None are its equal."],
  "replies" : [["who", "Who are you?"]]
  }, {
  "match" : ["where"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["Taku has fully recovered, and we expect him to be fishing very soon. And where are you? My friend, you are at the entrance to the greatest city in the world."],
  "replies" : [["city", "Greatest city...?"]]
  }, {
  "match" : ["what"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["Your ship was hit by a terrible storm, and we found your mangled body lying on the coast. My men rescued you and nursed you back to health."],
  "replies" : [["where", "Where am I? Where's Taku?"], ["gates", "Why are there gates blocking the doors?"]]
  },

  {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "60"]],
  "post" : [],
  "msg" : ["Do you have the Kabuto?"],
  "replies" : [["no", "No, not yet."], ["yes", "Yes, here it is."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "50"]],
  "post" : [],
  "msg" : ["Have you come to a decision yet?"],
  "replies" : [["no", "No, let me think about it."], ["yes", "Yes, I will."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "40"]],
  "post" : [],
  "msg" : ["Greetings traveler. I trust that your wounds have healed?"],
  "replies" : [["what", "What happened? I was on a ship..."]]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hey, you shouldn't be here! (Quest not started)"]
  }
]}
