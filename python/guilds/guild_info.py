"""
guild_info.py -- set the message text of the sign in front of guilds
"""
INACTIVE_DAYS = 365

import datetime
import time

import Crossfire

import CFGuilds
import CFLog

def guild_message(guildname):
    guild = CFGuilds.CFGuild(guildname)

    masters = []
    for member in guild.list_members():
        record = guild.info(member)
        if record:
            currentrank = record['Rank']
            if currentrank == 'GuildMaster':
                masters.append(member)

    log = CFLog.CFLog()

    message = "Welcome to the %s. The guild masters are:\n" % guildname
    active_count = 0
    inactive_count = 0

    now = datetime.datetime.now()
    for m in masters:
        message = message + "- %s" % m
        last_login = log.last_login(m)
        if last_login is not None:
            diff = now - datetime.datetime.fromtimestamp(time.mktime(last_login))
            if diff.days > INACTIVE_DAYS:
                message = message + "*"
                inactive_count = inactive_count + 1
            else:
                active_count = active_count + 1
        message = message + "\n"

    if inactive_count > 0:
        message = message + "Inactive guild masters are listed with an (*).\n"

    if active_count == 0:
        message = message + "There appear to be no active members. Contact a DM for help."

    return message

Crossfire.WhoAmI().Message = guild_message(Crossfire.ScriptParameters().split()[0])
