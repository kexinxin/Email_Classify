#encoding=utf-8
import jieba
import math

def split(text):
    result = jieba.cut(text,cut_all=False)
    list1=list(result)
    list2=[]
    
    stopWordsList =["我","与","的", "我们","要","自己","之","将","“","”","，","（","）","后","应","到","某","后","个","是","位","新","一","两","在","中","或","有","更","好","。","！","#","￥","&"]
    for word in list1:
        if (len(word)>1):
             word = word.encode('utf-8')
             if word not in stopWordsList:
                 list2.append(word)
    
    
    return list2

#str="10到12家生产工厂、200亿美元的投资猜想以及对再生能源、电商等行业的介入，富士康近日给印度接连发了几个“大红包”。在外界看来这是富士康作为全球制造代工巨头对未来趋势的战略选择，就连富士康总裁郭台铭也表示，公司将帮助当地企业设计、生产零部件和设备，使它们的产品能够走出印"
#for s in split(str):
#    print s
