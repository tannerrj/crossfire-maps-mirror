import os.path
import sqlite3

import Crossfire

def open():
    path = os.path.join(Crossfire.LocalDirectory(), 'crossfire.db')
    return sqlite3.connect(path)
