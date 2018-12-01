import pymysql.cursors
import configparser
from testdata.getpath import GetTestConfig

config=configparser.ConfigParser()
config.read(GetTestConfig('dbconfig.conf'))

db='TESTDB'
host = config[db]['host']
user = config[db]['user']
password = config[db]['passwd']
db = config[db]['db']

class MySQLcaozuo():
    def __init__(self):
        try:
            # host = "127.0.0.1"
            # user = "root"
            # password = "1234"
            # db = "polls"
            # db = 'TESTDB'
            # host = config[db]['host']
            # user = config[db]['user']
            # password = config[db]['passwd']
            # db = config[db]['db']
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                user=user,
                password=password,
                db=db,
                # charset=config[db]['charset'],
                charset='utf',
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()

    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def select(self, table_name):
        real_sql = "select * from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            all_data=cursor.fetchall()
            print(all_data)
            self.connection.commit()

    def update(self,table_name,key1,key2,value1,value2):
        real_sql="update "+table_name+" set "+key2+"="+value2+" where "+key1+"="+value1+";"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def update1(self, table_name, data1,data2):
        key1 = data1[0]
        value1 = data1[1]
        key2 = data2[0]
        value2 = data2[1]
        real_sql = "update " + table_name + " set " + key2 + "=" + value2 + " where " + key1 + "=" + value1 + ";"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def close(self):
        self.connection.close()