from classlib import *

def getSchoolInfo(schoolName):
    school.get_school_name(schoolName)
    school.get_school_address(schoolName)

def school_manager():
    print('Welcome to school management system!')
    temp=school()

    print("Register your school:\n")
    temp.regSchool()
    # input("Main menu:\n")
    menuDict={'1':school.add_teacher,
              '2':school.add_course,
              '3':school.add_student,
              '4':getSchoolInfo,
              '5':exit}
    while not False:
        i = input("Main menu:\n"
                  "1. Add teacher.\n"
                  "2. Add course.\n"
                  "3. Add student.\n"
                  "4. Get school information.\n"
                  "5. exit.\n")
        if i == '5':
            return
        elif i in menuDict.keys():
            menuDict[i](temp)
