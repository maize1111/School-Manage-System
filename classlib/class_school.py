from classlib.class_teacher import teacher
from classlib.class_student import student
from classlib.class_course import course


class school(object):
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__teacher_list = []
        self.__student_list = []
        self.__course_list = []

    '''
    function ADD...
    '''

    def add_course(self, course_name):
        new_course=course(course_name)
        self.__course_list.append(new_course)
        print("Add course: " + course_name + '\n')

    def add_teacher(self, teacher_name):
        new_teacher=teacher(teacher_name)
        self.__teacher_list.append(new_teacher)
        print("Add teacher: " + teacher_name + '\n')

    def add_student(self, student_name):
        new_student=student(student_name)
        self.__student_list.append(new_student)
        print("Add student: " + student_name + '\n')

    '''
    function GET...
    '''

    def get_teacher_list(self):
        print("This school's teacher list:\n")
        for i in self.__teacher_list:
            print(i.teacher_name+'\n')

    def get_student_list(self):
        print("This school's student list:\n")
        for i in self.__student_list:
            print(i.student_name+'\n')

    def get_course_list(self):
        print("This school's course list:\n",
              self.__course_list , '\n')

    def get_school_name(self):
        print("This school's name is " +
              self.__name + '\n')

    def get_school_address(self):
        print("This school's address is" +
              self.__address + '\n')
