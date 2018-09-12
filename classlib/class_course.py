import classlib.class_teacher

class course(object):
    course_list=[]

    def __init__(self,name,teacherName):
        self.__course_name=name
        self.course_users=[]
        course.course_list.append(name)
        self.teacherInfo=classlib.class_teacher.teacher('')


    def getName(self):
        return self.__course_name