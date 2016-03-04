#encoding=utf-8
import TrainingDataManager
M = 0.0
def calculatePxc(x, c):
    ret = 0.0
    Nxc = TrainingDataManager.getCountContainKeyOfClassification(c, x)
    Nc = TrainingDataManager.getTrainingCountOfClassification(c)
    V = len(TrainingDataManager.getTraningClassifications())
    ret = float((Nxc + 1)) / float((Nc + M + V))
    return ret;

#s1=unicode('我', 'utf-8')
#print calculatePxc(s1, 'car')