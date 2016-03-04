#encoding=utf-8
from django.test import TestCase
# Create your tests here.
import MySQLdb
import sys
reload(sys)
conn = MySQLdb.connect(host="localhost", user="root", passwd="kexinxin", db="test1",charset='utf8')
cursor = conn.cursor()
sql ="select * from sample"
cursor.execute(sql)

row=cursor.fetchone()

print row[2]

content=row[2]
str="元"

print content.count(str)


cursor.close()
conn.close() 
