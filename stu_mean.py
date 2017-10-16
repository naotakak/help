'''
Naotaka Kinoshita & Vivien Lee
SoftDev1 pd 7
Homework #10 - Average
2017-10-16
'''

import sqlite3

database = "things.db"

db = sqlite3.connect(database)
c = db.cursor()

q = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id"

foo = c.execute( q )

for bar in foo:
    ##calculate avg
    

db.close()
