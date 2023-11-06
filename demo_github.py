# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:15:21 2023

@author: Anna
"""
from sklearn.semi_supervised import LabelSpreading
import numpy as np
from scipy.spatial.distance import pdist,squareform

def BN_BER (Data, Label):
    
    visited, result, conf = set(), [], []
    n = len(Label)
    Store_Matrix = np.zeros((n,n))
    ### Index matrix that store the neighbor indexs of samples
    
    Sorted_Index = np.argsort(squareform(pdist(Data,'euclidean'),force='no',checks=True))
    for i in range(n):
        label_i = Label[i]
        for j in range(n):
            if label_i == Label[Sorted_Index[i][j]]:
                Store_Matrix[i][Sorted_Index[i][j]] = 1
            else:
                break
    Store_Matrix = Store_Matrix.astype(int)
    ### Insert reverse neighbor information
    for i in range (n):
        Store_Matrix[i,np.nonzero(Store_Matrix[:,i])[0]] = 1
    ###BFS
    def BFS(Store_Matrix,s):
        queue = []
        queue.append(s) # 向list添加元素，用append()
        seen = set() # 此处为set, python里set用的是hash table, 搜索时比数组要快。
        seen.add(s) # 向set添加函数，用add()
        while (len(queue) > 0):
            vertex = queue.pop(0)  #提取队头
            nodes = np.nonzero(Store_Matrix[vertex,:])  #获得队头元素的邻接元素
            for w in list(nodes)[0]:
                if w not in seen:
                    queue.append(w) #将没有遍历过的子节点入队
                    seen.add(w) #标记好已遍历 
        return seen    
        
    for i in range(n):
        if  i not in visited:
            seen = BFS(Store_Matrix,i)
            visited = visited | set(seen)
            result.append(seen)  
    result_s = sorted(result, key = lambda inx : -len(inx) )
    
    for i in range(len(result_s)):
        if len(result_s[i]) > 3:
            conf.extend(result_s[i])
    unconf = list(set(list(range(n)))-set(conf))
    label_prop_model = LabelSpreading()
    label_c = np.copy(Label)
    label_c[unconf] = -1
    label_prop_model.fit(Data, label_c)
    label_p = label_prop_model.predict(Data)
    ber = len(np.where(Label-label_p!=0)[0])/n
    
    return ber


filename='iris_4_3_150.txt'
Datasets = np.loadtxt(filename,delimiter=',')
[InstanceNum,AttributeNum] = Datasets.shape
Data = Datasets[:,:AttributeNum-1]
Label = (Datasets[:,AttributeNum-1]).astype(int)


ber = BN_BER (Data, Label)