{
  "location" : "scorn/oled",
  "rules": [
  {
  "match" : ["hello", "hi"],
  "pre" : [["token", "seenbefore", "yes"]],
  "post" : [["settoken", "offercoffee", "yes"]],
  "msg" : ["Hello $you, would you like some coffee?"]
  }, {
  "match" : ["hello", "hi"],
  "pre" : [],
  "post" : [["settoken", "offercoffee", "yes"]],
  "msg" : ["Hello stranger, would you like some coffee?"],
  "replies" : [["name", "What's your name?"]]
  }, {
  "match" : ["name"],
  "pre" : [],
  "post" : [["settoken", "seenbefore", "yes"]],
  "msg" : ["I'm Oled. I brew the finest coffee in Scorn."],
  "replies": [["coffee", "Can I have some coffee?"]]
  }, {
  "match" : ["lady", "friend", "Fran"],
  "pre" : [["token", "seenbefore", "yes"]],
  "post" : [],
  "msg" : ["Yeah, Fran's a sweet lady. She's probably over at the 'Mule right now."]
  }, {
  "match" : ["amy"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hey, whatever she told you is a lie, okay? That lady Mark was talking to was a sick friend of mine."]
  }, {
  "match" : ["mark"],
  "pre" : [],
  "post" : [],
  "msg" : ["Who? Never heard of him... Would you like a cup of coffee?"]
  }, {
  "match" : ["eswald"],
  "pre" : [["quest", "scorn/CoffeeGoose", "60"]],
  "post" : [],
  "msg" : ["That skunk Eswald and his stupid goose, now that he's got it back, they are undercutting my prices again."]
  }, {
  "match" : ["riverside", "mule"],
  "pre" : [],
  "post" : [],
  "msg" : ["I'm a little busy now."]
  }, {
  "match" : ["eswald", "lost", "goose", "esmeralda"],
  "pre" : [["quest", "scorn/CoffeeGoose", "20"]],
  "post" : [],
  "msg" : ["You say that Eswald has lost his goose? That's fantastic news; they've been undercutting my prices for years. \n\n Err... I mean, oh dear, what a shame, I am sorry to hear that."]
  }, {
  "match" : ["eswald"],
  "pre" : [],
  "post" : [],
  "msg" : ["That skunk Eswald and his stupid goose Undercutting my prices. One day..."]
  }, {
  "match" : ["no"],
  "pre" : [["token", "offercoffee", "yes"]],
  "post" : [["settoken", "offercoffee", "0"]],
  "msg" : ["No problem friend, come back later if you change your mind."]
  }, {
  "match" : ["yes", "like", "cup"],
  "pre" : [["token", "offercoffee", "yes"], ["item", "money", "3"]],
  "post" : [["giveitem", "Oled's coffee"], ["settoken", "offercoffee", "0"], ["takeitem", "money", "3"]],
  "msg" : ["Here you go."]
  }, {
  "match" : ["yes", "like", "cup"],
  "pre" : [["token", "offercoffee", "yes"]],
  "post" : [["settoken", "offercoffee", "0"]],
  "msg" : ["You'll need money to pay for the coffee, friend."]
  }, {
  "match" : ["coffee", "fresh", "cup"],
  "pre" : [],
  "post" : [["settoken", "offercoffee", "yes"]],
  "msg" : ["Coffee is 3 silver a cup, would you like some?"],
  "replies" : [["yes", "Yes, please!"], ["no", "No, thank you."]]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["Have a cup of coffee! Fresh coffee!"]
  }
]}
