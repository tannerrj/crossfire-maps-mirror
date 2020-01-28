{
  "location": "navar_city/magara/houses/museum",
  "rules": [
  {
  "match" : ["lost"],
  "pre" : [["quest", "quests/Azumauindo", "90"], ["item", "kog"]],
  "post" : [],
  "msg" : ["No you didn't. I see it right there."]
  }, {
  "match" : ["display"],
  "pre" : [["quest", "quests/Azumauindo", "90"]],
  "post" : [],
  "msg" : ["Well... that's because it's an... ahem... replica. I can't have anyone know I sold this priceless artifact to a random adventurer."]
  }, {
  "match" : ["lost"],
  "pre" : [["quest", "quests/Azumauindo", "90"]],
  "post" : [],
  "msg" : ["What? And you want another one? Well, too bad. That artifact was one of a kind."],
  "replies" : [["display", "I still see the Kabuto on display."]]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "80"], ["item", "ambercoin"]],
  "post" : [["quest", "quests/Azumauindo", "90"], ["takeitem", "ambercoin"], ["givecontents", "kabuto"]],
  "msg" : ["Herfan says: Oh... you really do have a lot of money! Well... take it then!"]
  }, {
  "match" : ["yes"],
  "pre" : [["quest", "quests/Azumauindo", "80"]],
  "post" : [],
  "msg" : ["Where is it then?"]
  }, {
  "match" : ["no"],
  "pre" : [["quest", "quests/Azumauindo", "80"]],
  "post" : [],
  "msg" : ["Hmph... you're wasting my time."],
  "replies" : []
  }, {
  "match" : ["money"],
  "pre" : [["quest", "quests/Azumauindo", "70"]],
  "post" : [["quest", "quests/Azumauindo", "80"]],
  "msg" : ["Really? Fine. We'll part with it for 1 amberium coin, no less."],
  "replies" : [["no", "I'll have to think about it."], ["yes", "Fine, I have the money."]]
  }, {
  "match" : ["kabuto"],
  "pre" : [["quest", "quests/Azumauindo", "70"]],
  "post" : [],
  "msg" : ["Er... the Kabuto? It's a prized possession of the museum. It's not for sale."],
  "replies" : [["money", "Are you sure? I have a lot of money..."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "90"]],
  "post" : [],
  "msg" : ["Hmph... can't you see I'm busy right now?"],
  "replies" : [["lost", "I lost the Kabuto."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "80"]],
  "post" : [],
  "msg" : ["Hmph... have you come to a decision yet?"],
  "replies" : [["no", "I'll have to think about it."], ["yes", "Fine, I have the money."]]
  }, {
  "match" : ["*"],
  "pre" : [["quest", "quests/Azumauindo", "70"]],
  "post" : [],
  "msg" : ["Hmph... can't you see I'm busy right now?"],
  "replies" : [["kabuto", "I want the Kabuto of Geisya."]]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hmph... can't you see I'm busy right now?"],
  "replies" : []
  }
]}