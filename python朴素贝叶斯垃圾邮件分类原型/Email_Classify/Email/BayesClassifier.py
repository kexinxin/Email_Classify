#encoding=utf-8
import TrainingDataManager
import ChineseSpliter
import PriorProbability
import ClassConditionalProbability

zoomFactor = 10.0
def calcProd(X,Cj):
    ret = 1.0
    for Xi in X:
        ret *=ClassConditionalProbability.calculatePxc(Xi, Cj)*zoomFactor
    ret *= PriorProbability.calculatePc(Cj)
    return ret




def classify(text):
    terms= ChineseSpliter.split(text)
    
#    for term in terms:
#        print term
        
    Classes = TrainingDataManager.getTraningClassifications()
    probility = 0.0
    crs={}
    for Ci in Classes:
        probility = calcProd(terms, Ci)
        print "In process...."
        print Ci + "：" + str(probility)
        crs[Ci]=probility
    #sorted(crs,probility)
    #count = { 'a': 120, 'b': 120, 'c': 100 }
    highest = max(crs.values())
    for k,v in crs.items(): 
        if v == highest:
            return k

def getClassify(text):    
#text ="新华网天津７月７日体育专电（记者张泽伟）７日，权健集团与天津松江俱乐部联合召开新闻发布会，宣布权健集团正式全资收购松江俱乐部。权健集团董事长束昱辉表示，投资足球将不留余力、不留私心，要做就做最好。未来俱乐部的发展目标将分四步走：保级、冲超、参加亚冠、参加世俱杯。"
     result = classify(text)
     return result

#s="我们"
#print StopWordsHandler.isStopWord(s)