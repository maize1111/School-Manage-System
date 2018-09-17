from pymysql import *


class mysql_connect:
    def auto_connection(self):
        self.host = 'localhost'
        self.port = 3306
        self.db = 'school_management_system'
        self.user = 'root'
        self.passwd = '584121035'
        self.charset = 'utf8'
        self.conn = connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            passwd=self.passwd,
                            db=self.db,
                            charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def exc(self, sql):
        try:
            self.auto_connection()
            self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except:
            print('Error! Roll back!')
            self.conn.rollback()
            self.close()

# test=mysql_connect()
# sql="INSERT INTO school_manager(name, address, id) VALUES ('Test','Test',4)"
# res=test.exc(sql)
# print(res)
# Test Successful
