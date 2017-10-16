'''
Naotaka Kinoshita & Vivien Lee
SoftDev1 pd 7
Homework #10 - Average
2017-10-16
'''

import sqlite3

##important database things
database = "things.db"
db = sqlite3.connect(database)
c = db.cursor()

##setting up the intial list to be added to using foo: makes list [NAME, ID] using the first element from the command
get_first = c.execute("SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id LIMIT 1")
for first in get_first:
    #print first
    current_person = first[0]
    current_id = first[1]

##master_list will be a list of current_lists in the format [ [NAME, ID, AVG1, AVG2, ...], ... ]
current_list = [current_person, current_id]
master_list = []

##selecting all the people and their averages
q = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id"
foo = c.execute( q )

##if the name is the same as previous name, add the average to the current list. Otherwise, add the current_list to master_list
##and generate a new current_list using the new name and ID
for bar in foo:
    #print bar
    if (current_person == bar[0]):
        current_list.append(bar[2])
        #print current_list
    else:
        master_list.append(current_list)  
        current_person = bar[0]
        current_id = bar[1]
        current_list = [current_person, current_id, bar[2]]
        #print master_list 
        #print current_list

##writing mean function to be used to calculate mean later
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

##print statement in form Name: NAME ID: id Average: mean(all averages which are found after name and id in the list)
print
for person in master_list:
    avg = mean(person[2:])
    print("Person: " + person[0] + " ID: " + str(person[1]) + " Average: " + str(avg) )        
print

##close database
##no committing because we shouldn't be changing the database
db.close()
