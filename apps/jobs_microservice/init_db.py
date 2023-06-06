#!/usr/bin/env python
import sqlite3

connection = sqlite3.connect("/tmp/jobs.db")

print ("running script to create tables")
with open("schema.sql") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
