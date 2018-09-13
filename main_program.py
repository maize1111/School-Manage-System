from classlib import *
from interface import *

flag = False
choice = {'1': school_manager, '2': teacher_manager, '3': student_manager, '4': exit}
while not flag:
    i = input("Choose your character:\n"
              "1: School Manager.\n"
              "2: Teacher.\n"
              "3: Student.\n"
              "4: Exit.\n")
    if i in choice.keys():
        choice[i]()
