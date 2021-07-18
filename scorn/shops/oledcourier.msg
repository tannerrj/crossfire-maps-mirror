{
  "location" : "scorn/oleds_cafe",
  "rules": [
  {
  "match" : ["name"],
  "pre" : [],
  "post" : [["settoken", "seenbefore", "yes"]],
  "msg" : ["My name is Jared. Yours?"]
  }, {
  "match" : ["hello", "hi"],
  "pre" : [["token", "seenbefore", "yes"]],
  "post" : [],
  "msg" : ["Hello $you, how can I help you?"]
  }, {
  "match" : ["hello", "hi"],
  "pre" : [],
  "post" : [],
  "msg" : ["Hello stranger, how can I help you?"]
  }, {
  "match" : ["mule"],
  "pre" : [],
  "post" : [],
  "msg" : ["Yeah, The Barking Mule? It's just a bit northwest of here, up that road."]
  }, {
  "match" : ["eswald", "oled", "coffee"],
  "pre" : [],
  "post" : [],
  "msg" : ["Coffee here is okay. Eswald use to have the BEST coffee! I wish I knew what happened."]
  }, {
  "match" : ["esmeralda"],
  "pre" : [],
  "post" : [],
  "msg" : ["I don't know who that is."]
  }, {
  "match" : ["goose", "bird"],
  "pre" : [],
  "post" : [],
  "msg" : ["Try Riverside."]
  }, {
  "match" : ["riverside", "where"],
  "pre" : [],
  "post" : [],
  "msg" : ["I've said too much already."]
  }, {
  "match" : ["*"],
  "pre" : [],
  "post" : [],
  "msg" : ["I'm on break right now."]
  }
]}
