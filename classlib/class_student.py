from classlib import *


class student(object):
    def __init__(self, name, school_name, id):
        self.school_name = school_name
        self.student_id = id
        self.student_name = name
        self.course_dict = {}

