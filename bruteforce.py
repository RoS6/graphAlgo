import numpy as np
from numba import jit,autojit
from itertools import combinations,permutations
@jit()
def check_validity(tuple,graph):
    pair11,pair1_1,pair_11,pair_1_1=False,False,False,False
    index = tuple[1]
    array = graph[index]#y
    rowindex = tuple[0]
    row = graph[tuple[0]]#x
    for j in range(num):
        if row[j]==1 and array[j]==1:
            pair11 = True
        if row[j] ==1 and array[j] ==-1:
            pair1_1 = True
        if row[j] ==-1 and array[j] ==1:
            pair_11 = True
        if row[j] ==-1 and array[j]==-1:
            pair_1_1 = True

    if  pair11 and pair1_1 and pair_11 and pair_1_1:
        return True
    else:
        return False
pair = {
    '11':(1,1),
    '1-1':(1,-1),
    '-11':(-1,1),
    '-1-1':(-1,-1)
}
@jit
def flip(graph):
    for i in range(len(graph)):
        for j in range(i):
            graph[i][j] = graph[j][i]

def sum(x,y):
    return x+y

def permute_unique(nums):
    perms = [[]]
    for n in nums:
        new_perm = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                # handle duplication
                if i < len(perm) and perm[i] == n: break
        perms = new_perm
    # print(len(perms))
    # print(len(set([tuple(t) for t in perms])))
    return perms

from functools import reduce
def permutationResult(num,i,sumofnumber):
    allnumbersinlist = [1]*(sumofnumber-i)+[-1]*i
    li = permute_unique(allnumbersinlist)
    print('permute finished')
    # print(li[0])
    result = []
    for i in li:
        content = list(li)
        upper = np.zeros((num,num))
        upper[np.triu_indices(num,1)] = list(i)
        result.append(upper)
        # print(upper)
    print('upper finished')
    return result
def checkV(graph):
    flip(graph)
    for j in combinations(combinationList, 2):
        if not check_validity(j,graph):
            # valid = False
            return False
    return True
for num in range(8,9):
    print(f"Checking n = {num}")
    valid = True
    sumofnumber = reduce(sum,range(1,num))
    combinationList = [i for i in range(num)]
    for i in range(1,sumofnumber+1):
        print(f"i = {i} / {sumofnumber}")
        # np.zeros(num*num)
        graphList = permutationResult(num,i,sumofnumber)
        # for graph in
        # break
        # for graph in graphList:
        #     flip(graph)
        if not (True in map(checkV,graphList)):
            valid = False

        if valid:
            print('graph')
            import sys
            sys.exit()


    #
    #
    #
    #     combinationList = [i for i in range(num)]
    #     graph = np.zeros(num*num)
    #     graph = graph.reshape(num,num)
    #     marked = []
    #     # graph[0] = np.array([0,0,1,1,-1,-1]+[])
    #
    #     np.fill_diagonal(graph,100)
    #     flip(graph)
    #     checking = []
    #     success = True
    #     for i in list(combinations(combinationList,2)):
    #         checking.append(i)
    #         marked = []
    #         if not check_validity(i):
    #             print('n = '+str(num)+' fail')
    #             # print('fail')
    #             success = False
    #             break
    #         # print(graph)
    #         # print(i)
    #     if success == False:
    #         num = num+1
    #         # break
    #     else:
    #         print(graph)
    #         print('success at n='+str(num))
    #         stop = True
    #         break
    # if stop:
    #     break
    #
    # # print(graph)
    # # break
