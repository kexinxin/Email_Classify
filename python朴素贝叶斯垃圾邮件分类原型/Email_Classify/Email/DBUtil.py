
__author__ = 'Smile'

import MySQLdb

def getConnection():
    connection = MySQLdb.connect(host='localhost',user='root',passwd='kexinxin',db='trainset',charset='utf8')
    return connection

def closeConnection(connection):
    if connection!=None:
        connection.close()



'''
connection = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='trainset')
cursor = connection.cursor()

cursor.execute('insert into list VALUES ("c00001","hehe")')
connection.commit()
cursor.close()
connection.close()0
    '''
