


#余弦相似度
import math
'''在协同过滤推荐系统中，C 和 N 是计算用户相似度矩阵（W）时的中间变量。这些变量的作用如下：

C（用户间共同评分次数）： C[u][v] 表示用户 u 和用户 v 之间共同评价过的物品数量。通过统计用户对相同物品的评分次数，
可以度量两个用户的兴趣相似程度。共同评分次数越多，用户之间的相似度可能越高。

N（用户评分物品的次数）： N[u] 表示用户 u 评价过的物品的数量。它用于归一化用户相似度矩阵中的共同评分次数。
通过除以用户 u 评价过的物品数量的平方根，可以考虑到不同用户评价物品数量的差异，避免评价物品数量较大的用户对相似度的影响过大。

这两个变量的计算是在遍历训练数据时进行的，目的是为了计算用户相似度矩阵 W。最终的相似度矩阵 W 是基于用户对物品的共同评分次数，
通过归一化的方式得到的，用于衡量用户之间的相似度。在推荐系统中，用户相似度矩阵 W 用于预测用户对未评分物品的兴趣程度，从而进行推荐。'''


'''
在协同过滤算法中，使用字典而不是NumPy数组主要是为了灵活性和节省空间。
协同过滤算法中的用户-物品评分矩阵通常是非常稀疏的，大多数用户只评价了少数物品。
使用字典来表示共同评分次数可以有效地存储和管理这种稀疏数据。'''
import math

def UserSimilarity(train):
    item_users = dict()

    # 初始化字典
    C = dict()
    N = dict()
    W = dict()

    for u, items in train.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)  # 将用户添加进物品i，建立倒排表

    # 初始化字典
    for i in item_users:
        C.setdefault(i, {})
        for u in item_users[i]:
            N.setdefault(u, 0)
            '''
setdefault() 是字典（dictionary）方法，用于返回指定键的值。如果键存在于字典中，则返回对应的值；如果键不存在，则插入该键并设置默认值，然后返回默认值。'''
            C[u] = C.get(u, {})
            '''C.get(key, default) 是字典（dictionary）方法，用于返回指定键 key 的值。如果键存在于字典中，则返回对应的值；
            如果键不存在，则返回 default 指定的默认值，而不会修改字典本身。'''
            W.setdefault(u, {})

    # 计算相似度
    for i, users in item_users.items():
        for u in users:
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                C[u][v] = C[u].get(v, 0) + 1
    # 计算相似度矩阵 W
    print(N)
    print(C)
    for u, related_users in C.items():
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])

    return W


train = {
    'user1': {'item1': 3, 'item2': 4, 'item3': 1}, #item1 物品   3 评分
    'user2': {'item1': 2, 'item2': 5, 'item5': 4},
    'user3': {'item2': 3, 'item5': 2, 'item6': 4},
    'user4': {'item4': 5, 'item5': 2, 'item6': 4},

    # ... 其他用户及其评分信息
}

W=UserSimilarity(train)
print(W)
def Recommand(user,train,W,K):
    rank=dict()
    interacted_items=train[user] #用户u的所有接触物品

    #然后遍历相关度最高的前K个用户，且这K个用户与目标item有过行为





