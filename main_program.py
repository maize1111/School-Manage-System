from classlib import *
from interface import *
from mysqldb import *

# MySql Execute Test - Successful
# db=connect(host='localhost',port=3306,user='root',passwd='584121035',db='school_management_system',charset='utf8')
# cursors=db.cursor()
#
# sq1="INSERT INTO school_manager(name,address,id)values ('Fudan University','Xuhui','3')"
#
# try:
#     cursors.execute(sq1)
#     db.commit()
# except:
#     db.rollback()
#
# cursors.close()
# db.close()



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
