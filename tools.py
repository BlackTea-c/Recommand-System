

#预测准确度
import math
#均方根误差
#records存放用户评分数据;records[i]=[u,i,rui,pui]  u用户  i物品  rui 用户u对物品i的评分  pui 预测的评分
def RMSE(records):
    return  math.sqrt(sum([(rui-pui)**2 for u,i,rui,pui in records]))/len(records)

#records=[['a',1,5,3],['b',1,5,4],['c',1,5,5],['d',1,5,1],['e',2,5,2]]
#平均绝对误差
def MAE(records):
    return sum([abs(rui - pui) for u, i, rui, pui in records]) / len(records)




#准确率
#召回率
#覆盖率
#物品流行度 #大多数物品流行度符合长尾分布
