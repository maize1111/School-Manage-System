from classlib.class_teacher import *
from classlib.class_student import *
from classlib.class_course import *


class school(object):
    school_list = []

    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__teacher_list = []
        self.__student_list = []
        self.__course_list = []

    # Register a new school
    def regSchool(self):
        print("------Registered School------")
        school_name = input("School name: ")
        school_address = input("School Address: ")
        school.school_list.append(school_name)
        self.__name = school_name
        self.__address = school_address
        print("------Registered Successful------\n")

    '''
    function ADD objects...
    '''

    def add_course(self, course_name, teacher_name):
        new_course = course(course_name,teacher_name)
        self.__course_list.append(new_course)
        course.course_list.append(course_name)
        new_course.teacherInfo.setName(teacher_name)
        print("Add course: " + course_name + '\n')

    def add_teacher(self, teacher_name):
        new_teacher = teacher(teacher_name)
        self.__teacher_list.append(new_teacher)
        print("Add teacher: " + teacher_name + '\n')

    # add student by input his/her information
    def add_student(self):
        new_student = student()
        new_student.signup()
        self.__student_list.append(new_student)
        # print("Add student: " + new_student.getName() + '\n')

    # add student with his/her name, school and id
    def add_student_details(self, name, school, id):
        new_student = student()
        new_student.setName(name)
        new_student.setSchool(school)
        new_student.setID(id)
        self.__student_list.append(new_student)
        print("Add student: " + name + '\n')

    '''
    function GET information...
    '''

    def get_teacher_list(self):
        print("This school's teacher list:\n")
        for i in self.__teacher_list:
            print(i.getName() + '\t')
        print()

    def get_student_list(self):
        print("This school's student list:\n")
        for i in self.__student_list:
            print(i.getName() + '\t')
        print()

    def get_course_list(self):
        print("This school's course list:\n")
        for i in self.__course_list:
            print(i.getName() + '\t')
        print()

    def get_school_name(self):
        print("This school's name is " +
              self.__name + '\n')

    def get_school_address(self):
        print("This school's address is " +
              self.__address + '\n')

    '''
    function SET...
    '''

