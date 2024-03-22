import os.path

import Crossfire
import CFMail

def convert_bdb(mail):
    filename = 'crossfiremail.db'
    path = os.path.join(Crossfire.LocalDirectory(), filename)
    if os.path.isfile(path):
        Crossfire.Log(Crossfire.LogInfo, "Converting crossfiremail.db (BDB)")
        import berkeleydb.dbshelve as shelve
        old_db = shelve.open(path, 'r')
        for to in old_db.keys():
            allmail = old_db[to]
            toname = to.decode('ascii')
            for (t, fromname, msg) in allmail:
                mail.send(t, toname, fromname, msg)
        old_db.close()
        bak_file = os.path.join(Crossfire.LocalDirectory(), filename + '.bak')
        os.rename(path, bak_file)

def main():
    Crossfire.Log(Crossfire.LogInfo, "Initializing CFMail")
    with CFMail.CFMail() as mail:
        mail.init_schema()
        convert_bdb(mail)

main()
