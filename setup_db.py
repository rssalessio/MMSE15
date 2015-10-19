#!/usr/bin/env python3

import sqlite3

print("> setup db")

# executes script "tables" located in the SQLDatabase folder.
# It Will destroy all database tables and reinstall everything.
# User data is lost, Warning
connectionName = "SEP.db"
connection = sqlite3.connect(connectionName)
cursor = connection.cursor()
cursor.executescript(open('./mmse15project/model/SQLDatabase/tables', 'r').read())
connection.commit()
connection.close()

print("Database installed")