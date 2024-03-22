# CFMail.py - CFMail class
# Rewritten to use CFSqlDb

import Crossfire
import CFSqlDb as cfdb

class CFMail:
    def __init__(self):
        self.maildb = cfdb.open()

    def init_schema(self):
        self.maildb.execute("CREATE TABLE IF NOT EXISTS mail ('recipient' TEXT, 'sender' TEXT, 'date' DATE, 'type' INT, 'message' TEXT);")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def send(self, type, toname, fromname, message):
        # type: 1=mailscoll, 2=newsletter, 3=mailwarning
        self.maildb.execute("INSERT INTO mail VALUES (?, ?, datetime('now'), ?, ?);", (toname, fromname, type, message))

    def receive(self, toname):
        c = self.maildb.cursor()
        c.execute("SELECT type, sender, message FROM mail WHERE recipient=?;", (toname,))
        mail = list()
        for el in c.fetchall():
            mail.append(el)
        c.execute("DELETE FROM mail WHERE recipient=?;", (toname,))
        return mail

    def countmail(self, toname):
        c = self.maildb.cursor()
        c.execute("SELECT COUNT(*) FROM mail WHERE recipient=?;", (toname,))
        return c.fetchone()[0]

    def close(self):
        self.maildb.commit()
        self.maildb.close()
