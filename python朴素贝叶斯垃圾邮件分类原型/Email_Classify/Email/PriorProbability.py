#encoding=utf-8
import TrainingDataManager
def calculatePc(c):
    ret = 0.0
    Nc = TrainingDataManager.getTrainingCountOfClassification(c)
    N = TrainingDataManager.getTrainingCount()
    ret = float(Nc) /float( N)
    return ret

#print calculatePc('businise')