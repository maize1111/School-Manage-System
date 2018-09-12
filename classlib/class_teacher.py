from classlib import *


class teacher(object):
    def __init__(self, name):
        self.__teacher_name = name

    def getName(self):
        return self.__teacher_name
    def setName(self,name):
        self.__teacher_name=name