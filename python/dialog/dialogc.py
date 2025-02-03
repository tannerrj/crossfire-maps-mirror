#!/usr/bin/env python3
"""
dialogc.py -- Crossfire dialog compiler

Complies simple dialogs into CFDialog-compatible JSON. Works on standard input
and output when called from the command-line.
"""

def parse_dialog(s):
    rules = []

    # current block
    matches = None # None or list of string matches
    pre = []
    msgbuilder = [] # list of strings, to be joined with newlines
    replies = [] # list of reply keywords and reply text
    post = []

    def new_block():
        "Reset local variables when entering a new @match block."
        nonlocal pre, msgbuilder, replies, post
        pre = []
        msgbuilder = []
        replies = []
        post = []

    def end_block():
        "Add the current block to the rules dict."
        block = {}
        nonlocal matches
        if matches is None:
            if len(msgbuilder) > 0:
                # not in a @match block, and there is text: create a @match * block
                matches = ['*']
            else:
                return # empty initial block, don't generate it
        block['match'] = matches
        if len(pre) > 0:
            block['pre'] = pre
        block['msg'] = ["\n".join(msgbuilder)]
        if len(replies) > 0:
            block['replies'] = replies
        if len(post) > 0:
            block['post'] = post
        rules.append(block)

    new_block()
    lines = s.split("\n")
    for line in lines:
        if line.startswith('@match'):
            end_block()
            parts = line.split(' ', maxsplit=1)
            matches = parts[1].split('|')
            new_block()
        elif line.startswith('@reply'):
            parts = line.split(' ', maxsplit=2)
            key = parts[1]
            msg = parts[2]
            replies.append([key, msg])
        elif line.startswith('@identify'):
            post.append(["identify"])
        elif line.startswith('@pre'):
            parts = line.split(' ')
            pre.append(parts[1:])
        elif line.startswith('@post'):
            parts = line.split(' ')
            post.append(parts[1:])
        else:
            msgbuilder.append(line)
    end_block()

    dialog = {}
    dialog['rules'] = rules
    return dialog

if __name__ == '__main__':
    import json
    import sys
    dialog = parse_dialog(sys.stdin.read().strip())
    json.dump(dialog, sys.stdout)
    print('') # newline
