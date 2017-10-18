'''
Naotaka Kinoshita & Vivien Lee & Caleb Smith-Salzberg
SoftDev1 pd 7
Homework #10 - Average
2017-10-16
'''

import sqlite3

##important database things
database = "things.db"
db = sqlite3.connect(database)
c = db.cursor()

##writing mean function to be used to calculate mean later
def mean(name):
    tot = 0
    len = 0
    for mark in name['marks']:
        tot += mark
        len += 1
    return tot/len

def build_students():
    ##selecting all the people and their averages
    q = "SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id"
    foo = c.execute( q )
    student_grades = {}
    
    for bar in foo:
        #print bar
        student = bar[0]
        id = bar[1]
        mark = bar[2]
        if student in student_grades:
            student_grades[student]['avg'] = mean(student_grades[student])
            student_grades[student]['marks'].append(mark)
        else: 
            student_grades[student] = {}
            student_grades[student]['marks'] = []
            student_grades[student]['marks'].append(mark)
            student_grades[student]['avg'] = mark
            student_grades[student]['id'] = id

    return student_grades
    
def up_avgs(name, class_code, mark, student_id):
    grades = build_students()
    new_avg = mean(grades[name])
    q = "UPDATE peeps_avg SET average = " + str(new_avg) + " WHERE id = " + str(grades[name]['id'])
    c.execute( q )
    qq = "INSERT INTO courses VALUES ('" + class_code + "'," + str(mark) + "," + str(student_id) + ")"
    c.execute(qq)
    grades[name]['avg'] = new_avg
    return grades

##print statement in form Name: NAME ID: id Average: mean(all averages which are found after name and id in the list)
def print_grades(students):
    for student in students:
        grades = str(students[student]['marks'])
        grades = grades[1:len(grades) - 1]
        print("STUDENT: " + student + " ID: " + str(students[student]['id']) + " GRADES: " + grades + " AVG: " + str(students[student]['avg']))

def make_table():
    c.execute("CREATE TABLE peeps_avg(id INTEGER, average NUMERIC)")

make_table()

pre_add = build_students()

print ("Before adding courses:")
print_grades(pre_add)

after_add = up_avgs("kruder", "systems", 99, 1)

print ("After adding course 'kruder', 'systems', 99, 1")
print_grades(after_add)

##close database
db.commit()
db.close()
