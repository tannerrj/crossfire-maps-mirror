#This is the madness maze, created by Alestan.  Like all of crossfire, it is distributed under the GNU license.
#Please report bugs to Alestan@meflin.com
#Created: 1 Aug 2008
import Crossfire

# Each entry: reply word -> (what the player asks, what the Guardian says,
# follow-up replies offered afterwards as (word, text) pairs).
# The menu is offered with Crossfire.AddReply() so the player gets a
# "Replies:" list instead of the Guardian speaking every option; this keeps
# the Guardian under the server's MAX_NPC limit of 5 Say() calls per event.
Q = Crossfire.ReplyType.QUESTION
S = Crossfire.ReplyType.SAY

menu = [
    ("1", "What is this place?"),
    ("2", "Who are you?"),
    ("3", "What information?"),
    ("4", "Die you freak!"),
]

topics = {
    "1": ("What is this place?", Q,
          "This is the Madness maze, leave before it is too late",
          [("5", "Too late?")]),
    "2": ("Who are you?", Q,
          "I am the Guardian of the Madness Maze.  As you see, I am armless, not much of a guardian eh?",
          [("6", "What happened to your arms?")]),
    "3": ("What information?", Q,
          "Many entered here, few return, those that do are... changed...  For the good of all, it has been closed.  I am here to give warning.",
          [("7", "Changed?")]),
    "4": ("Die you freak!", S,
          "Please, go ahead, kill me, I want to die.",
          []),
    "5": ("Too late?", Q,
          "If you go in there, you won't come back.",
          []),
    "6": ("What happened to your arms?", Q,
          "They cut them off, seemed to think I might be tempted by the maze, like I woulda been.  Figured I could warn people without arms, but I couldn't disarm the traps without arms.",
          []),
    "7": ("Changed?", Q,
          "That's what I said, changed.  Rarely for the better.",
          []),
}

whoami = Crossfire.WhoAmI()
if whoami.Name == "Guardian":
    text = Crossfire.WhatIsMessage().split() or [""]
    topic = topics.get(text[0])
    if topic:
        asked, kind, answer, replies = topic
        Crossfire.SetPlayerMessage(asked, kind)
        whoami.Say(answer)
    else:
        whoami.Say("I have some information you need.")
        replies = menu
    for word, reply in replies:
        Crossfire.AddReply(word, reply)
