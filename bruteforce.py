import numpy as np
from numba import jit,autojit
from itertools import combinations,permutations

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
def flip(graph):
    for i in range(len(graph)):
        for j in range(i):
            graph[i][j] = graph[j][i]

def sum(x,y):
    return x+y
@jit
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

def equivalence_permutations(x, o):
    """Create all unique permutations with `x` x'es and `o` o's."""
    total = x+o
    for indices in combinations(range(total), x):
        lst = [1]*total
        for index in indices:
            lst[index] = -1
        yield lst

from functools import reduce
def permutationResult(num,i,sumofnumber):
    # allnumbersinlist = [1]*(sumofnumber-i)+[-1]*i
    # li = permute_unique(allnumbersinlist)
    # print('permute finished')
    # print(li[0])
    # result = []
    # valid = False
    # for i in li:
    #     content = list(li)
    #     upper = np.zeros((num,num))
    #     upper[np.triu_indices(num,1)] = list(i)
    #     # result.append(upper)
    #     if checkV(upper):
    #         valid = True
    #         break
    # if True in map(checkV2,permute_unique(allnumbersinlist)):
    #     return True
    if True in map(checkV2,list(equivalence_permutations(sumofnumber-i,i))):
        return True

    #     valid = True
    # if valid:
    #     return True

        # print(upper)
    print('not true')
    # return result
# def checkV(graph):
#     flip(graph)
#     for j in combinations(combinationList, 2):
#         if not check_validity(j,graph):
#             # valid = False
#             return False
#     return True

def checkV2(i):
    # flip(graph)
    upper = np.zeros((num, num))
    upper[np.triu_indices(num, 1)] = list(i)
    # graph = upper
    flip(upper)
    print(upper)
    for j in combinations(combinationList, 2):
        if not check_validity(j, upper):
                # valid = False
            return False
    return True
        # upper = np.zeros((num,num))
        # upper[np.triu_indices(num,1)] = list(i)


for num in range(9,10):
    print(f"Checking n = {num}")
    # valid = True
    result = False
    sumofnumber = reduce(sum,range(1,num))
    combinationList = [i for i in range(num)]
    for i in range(17,sumofnumber+1):
        print(f"i = {i} / {sumofnumber}")
        # np.zeros(num*num)
        result = permutationResult(num,i,sumofnumber)
        # for graph in
        # break
        # for graph in graphList:
        #     flip(graph)
        # if not (True in map(checkV,graphList)):
        #     valid = False

        if result:
            print('graph')
            import sys
            sys.exit()




# egg = [
#     [0, -1, -1, 1, 1, -1, 1, 1], [-1, 0, 1, -1, 1, 1, -1, 1], [-1, 1, 0, 1, 1, 1, -1, -1],
#     [1, -1, 1, 0, -1, 1, 1, -1],[1,1,1,-1,0,-1,-1,1],[-1,1,1,1,-1,0,1,-1],[1,-1,-1,1,-1,1,0,-1,1],
#     [1,1,-1,-1,1,-1,1,0,1]]
# eg = np.array(egg)
# eg2 = [
#     [0,1,-1,-1,1,-1,1,-1,1],
#     [1,0,1,-1,-1,-1,-1,1,1],
#     [-1,1,0,-1,-1,1,1,1,-1],
#     [-1,-1,-1,0,1,1,-1,1,1],
#     [1,-1,-1,1,0,-1,1,1,-1],
#     [-1,-1,1,1,-1,0,1,-1,1],
#     [1,-1,1,-1,1,1,0,-1,-1],
#     [-1,1,1,1,1,-1,-1,0,-1],
#     [1,1,-1,1,-1,1,-1,-1,0]
# ]
# num = 9
# print(f"Checking n = {num}")
# # valid = True
# # result = False
# sumofnumber = reduce(sum, range(1, num))
# combinationList = [i for i in range(num)]
#
#     # np.zeros(num*num)
# # result = permutationResult(num, 14, sumofnumber)
# for j in combinations(combinationList, 2):
#     if not check_validity(j, eg2):
#         # valid = False
#         print(j)
#     # for graph in
#     # break
#     # for graph in graphList:
#     #     flip(graph)
#     # if not (True in map(checkV,graphList)):
#     #     valid = False
# #
# # if result:
# #     print('graph')
# #     import sys
#
#     sys.exit()
# li = [1]*10+[-1]*8
# from time import time
# start = time()
# # permute_unique(li)
# print(permute_unique(li))
# print(time()-start)
#
# start = time()
# print(set(equivalence_(li,18)))
# print(time()-start)

from itertools import combinations

# def equivalence_permutations(one, mone):
#     """Create all unique permutations with `x` x'es and `o` o's."""
#     lst = [[]]
#     total = one+mone
#     for indices in combinations(range(total), one):
#         lst = [1]*one
#         for index in indices:
#             lst[index] = -1
#         return lst


# start = time()
# print(list(equivalence_permutations(10,8)))
# print(time()-start)