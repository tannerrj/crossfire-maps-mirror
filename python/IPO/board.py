# Script for say event of IPO message board
#
# Copyright (C) 2002 Joris Bontje
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# The author can be reached via e-mail at jbontje@suespammers.org
#
# help                - gives information about usage
#
#Updated to use new path functions in CFPython -Todd Mitchell

import Crossfire
import CFBoard

activator = Crossfire.WhoIsActivator()
whoami = Crossfire.WhoAmI()

boardname = Crossfire.ScriptParameters().strip()

def board_list(board):
    msgs = []
    for i, e in enumerate(board.list(boardname)):
        author, message = e
        msgs.append('<%d> (%s) %s'%(i + 1, author, message))
    if len(msgs) == 0:
        return ["The board is empty."]
    return msgs

def handle_say(board):
    text = Crossfire.WhatIsMessage().split(' ', 1)

    if text[0] == 'help' or text[0] == 'yes':
        return ['You can:\n- list\n- write <message>\n- remove <id>']

    elif text[0] == 'write':
        if len(text) == 2:
            board.write(boardname, activator.Name, text[1])
            return ["You post a message to the board."]
        else:
            return ['Usage "write <text>"']

    elif text[0] == 'list':
        return board_list(board)

    elif text[0] == 'remove':
        if len(text) != 2:
            return ["Which post do you want to remove?"]
        index = int(text[1])
        if not (board.getauthor(boardname, index) == activator.Name or activator.DungeonMaster):
            return ["You may not remove others' posts."]
        if not board.delete(boardname, index):
            return ["That post doesn't exist!"]
        return ["You remove a post."]

    else:
        return ['Do you need help?']

def main():
    Crossfire.SetReturnValue(1)
    if len(boardname) == 0:
        activator.Write("This board is not set up correctly. Ask a dungeon master for help.")
        return

    with CFBoard.CFBoard() as board:
        msg = []
        if Crossfire.WhatIsEvent().Subtype == Crossfire.EventType.APPLY:
            header = whoami.Message.strip()
            if (len(header) > 0):
                msg.append(header)
            msg = msg + board_list(board)
        else:
            msg = handle_say(board)
        activator.Write("\n".join(msg))

main()
