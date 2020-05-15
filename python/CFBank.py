"""
Created by: Joris Bontje <jbontje@suespammers.org>

This module stores bank account information.
"""

import Crossfire
import CFSqlDb as cfdb

class CFBank:
    def __init__(self):
        self.bankdb = cfdb.open()

    def init_schema(self):
        self.bankdb.execute("CREATE TABLE IF NOT EXISTS bank_accounts ('name' TEXT PRIMARY KEY, 'balance' INT);")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def ensure(self, user):
        self.bankdb.execute("INSERT OR IGNORE INTO bank_accounts VALUES (?, 0)", (user,))

    def deposit(self, user, amount):
        if amount > 0:
            self.ensure(user)
            self.bankdb.execute("UPDATE bank_accounts SET balance = balance + ? WHERE name=?", (amount, user))

    def withdraw(self, user, amount):
        if self.getbalance(user) - amount < 0:
            return 0
        else:
            self.bankdb.execute("UPDATE bank_accounts SET balance = balance - ? WHERE name=?", (amount, user))
            return 1

    def getbalance(self, user):
        self.convert_legacy_balance(user)
        c = self.bankdb.cursor()
        c.execute("SELECT balance FROM bank_accounts WHERE name=?", (user,))
        result = c.fetchone()
        if result is not None:
            return result[0]
        else:
            return 0

    def remove_account(self, user):
        c.execute("DELETE FROM bank_accounts WHERE name=?", (user,))

    def close(self):
        self.bankdb.commit()
        self.bankdb.close()

    def convert_legacy_balance(self, name):
        """Move a player's balance from the player file to the bank."""
        player = Crossfire.FindPlayer(name)
        if player is None:
            return
        balance_str = player.ReadKey("balance")
        try:
            old_balance = int(balance_str)
            Crossfire.Log(Crossfire.LogInfo, "Converting bank account for %s with %d silver" % (name, old_balance))
            self.deposit(name, old_balance)
        except ValueError:
            pass
        player.WriteKey("balance", None, 0)

def open():
    return CFBank()
