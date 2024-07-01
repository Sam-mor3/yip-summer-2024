student_grade = [("Billy", 93), ("Jen", 82), ("Max", 98), ("Anne", 65), ("Charlie", 71)]

for record in student_grade:
    name, grade = record 
    #insert format string here
    print("{0} got a {1}".format(name, grade))
 
   # print (f"{name} got a {grade}")
