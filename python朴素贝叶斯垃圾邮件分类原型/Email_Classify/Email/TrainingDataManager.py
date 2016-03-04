#encoding=utf-8
import DBUtil
import MySQLdb

traningClassifications =['businise','PE','health','travel']
trainingCount=0
map={}
contentMap={}

connection = DBUtil.getConnection();
sql = "select type from list";
cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
cursor.execute(sql)
result = cursor.fetchall()
for s in result:
    print s['type']
cursor.close()    
DBUtil.closeConnection(connection)


for type in traningClassifications:
    connection = DBUtil.getConnection();
    sql="select count(sample.id) from sample,list where sample.id=list.id and list.type=%s";
    cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute(sql,type)
    result = cursor.fetchall()
    map[type]=result[0]['count(sample.id)']
    trainingCount+=result[0]['count(sample.id)']
cursor.close()    
DBUtil.closeConnection(connection)

#print trainingCount
#print map['car']

connection = DBUtil.getConnection();
sql = "select content from sample,list where sample.id=list.id and list.type=%s";
cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

for type in traningClassifications:
    i=0
    cursor.execute(sql,type)
    result = cursor.fetchall()
#    print result
    for dic_result in result:
         contentMap[type+str(i)]=dic_result['content']
         i=i+1
    
cursor.close()    
DBUtil.closeConnection(connection)

#print contentMap['car3']


def getTraningClassifications():
    return traningClassifications

def getTrainingCountOfClassification(classification):
    return map[classification]

def getTrainingCount():
    return trainingCount

def getCountContainKeyOfClassification(classification,key):
    ret = 0
    for i  in  range(0,map[classification]):
        text=contentMap[classification+str(i)]
        text = text.encode('utf-8')
        if(text.count(key)):
                ret=ret+1
    return ret

#s1=unicode('凭借陆风的强势品牌形象和完善服务网络', 'utf-8')
#print getCountContainKeyOfClassification('car',s1)    
#print getCountContainKeyOfClassification('car',u'我们')
