import classlib.class_school
import classlib.class_course

class student(object):
    def __init__(self):
        self.__school_name = ''
        self.__student_id = ''
        self.__student_name = ''
        self.course_dict = {}  # key: course name    value: grade

    def signup(self):
        print("------Register Student------")
        self.__student_name = input("Your name: ")
        self.__school_name = input("Your school: ")
        temp_name=self.__school_name
        if temp_name not in classlib.class_school.school.school_list:
            print("No this school!\n"
                  "Registered filed!\n")
            del self
            return
        self.__student_id = input("Your ID: ")
        print("------Registered Successful！------\n")

    def setName(self,name):
        self.__student_name=name

    def setSchool(self,school):
        self.__school_name=school

    def setID(self,id):
        self.__student_id=id

    def getName(self):
        return self.__student_name

    def getID(self):
        return self.__student_id

    def getSchoolName(self):
        return self.__school_name

    def choose_course(self, course_name):
        for i in classlib.class_course.course.course_list:
            print(i+'\t')
        your_course = input("Choose your course: ")
        self.course_dict[your_course] = 0 #default grade is 0

    def check_grade(self):
        for i in self.course_dict.keys():
            print("Your Grade Is: \n"+i,":",self.course_dict[i],'\n')

