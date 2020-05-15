import os.path

import Crossfire
import CFBank

def convert_bdb(bank):
    path = os.path.join(Crossfire.LocalDirectory(), 'ImperialBank_DB.db')
    if os.path.isfile(path):
        Crossfire.Log(Crossfire.LogInfo, "Converting ImperialBank_DB.db (BDB)")
        import berkeleydb.dbshelve as shelve
        accounts = shelve.open(path, 'r')
        for account in accounts.keys():
            name = account.decode('ascii')
            balance = accounts[account]
            bank.deposit(name, balance)
        accounts.close()
        bak_file = os.path.join(Crossfire.LocalDirectory(), 'ImperialBank_DB.db.bak')
        os.rename(path, bak_file)

def convert(bank):
    path = os.path.join(Crossfire.LocalDirectory(), 'ImperialBank_DB')
    if os.path.isfile(path):
        Crossfire.Log(Crossfire.LogInfo, "Converting ImperialBank_DB (DBM)")
        import shelve
        s = shelve.open(path, 'r')
        for name, balance in s.iteritems():
            bank.deposit(name, balance)
        s.close()
        bak_file = os.path.join(Crossfire.LocalDirectory(), 'ImperialBank_DB.bak')
        os.rename(path, bak_file)

def main():
    Crossfire.Log(Crossfire.LogInfo, "Initializing CFBank")
    with CFBank.CFBank() as bank:
        bank.init_schema()
        convert_bdb(bank)
        convert(bank)

main()
