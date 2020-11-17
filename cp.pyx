import numpy as np
# cimport numpy as cnp
from itertools import combinations,permutations
def check_validity( tuple):
    pair11,pair1_1,pair_11,pair_1_1=False,False,False,False
    cdef int[:] array
    cdef int[:] row
    index = tuple[1]
    array = graph[index]#y
    rowindex = tuple[0]
    # def list row
    row = graph[tuple[0]]#x
    cdef unsigned int j
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
cdef dict pair
pair = {
    '11':(1,1),
    '1-1':(1,-1),
    '-11':(-1,1),
    '-1-1':(-1,-1)
}
def flip(graph):
    cdef unsigned int i
    cdef unsigned int j
    for i in range(len(graph)):
        for j in range(i):
            graph[i][j] = graph[j][i]

def sum(x,y):
    return x+y

cpdef list permute_unique(int[:] nums):
    cdef list perms
    cdef unsigned int i
    perms = [[]]
    cdef int n
    cdef list new_perm
    for n in nums:
        # cdef list new_perm=[]
        new_perm = []
        # cdef list perm
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                # handle duplication
                if i < len(perm) and perm[i] == n: break
        perms = new_perm
    return perms
# ctypedef cnp.int_t DTYPE_t
from functools import reduce
cpdef permutationResult(int num,int minus,int sumofnumber):
    cdef int[:] allnumbersinlist
    allnumbersinlist = [1]*(sumofnumber-minus)+[-1]*minus
    cdef int[:,:] li
    li = permute_unique(allnumbersinlist)
    result = []
    cdef list i
    for i in li:
        content = list(li)
        # cdef cnp.ndarray[cnp.int_t,ndim=2] upper
        upper = np.zeros((num,num),dtype=int)
        upper[np.triu_indices(num,1)] = list(i)
        result.append(upper)
        # print(upper)
    return result

cdef unsigned int num
cdef int sumofnumber
cdef list combinatinList
cdef list graphList

cdef int minus
cdef tuple j

for num in range(4,9):
    print(f"Checking n = {num}")
    valid = True
    sumofnumber = reduce(sum,range(1,num))
    combinationList = [i for i in range(num)]
    for minus in range(1,sumofnumber+1):
        print(f"i = {minus} / {sumofnumber}")
        # np.zeros(num*num)
        graphList = permutationResult(num,minus,sumofnumber)
        # for graph in
        # break
        for graph in graphList:
            flip(graph)

            for j in combinations(combinationList, 2):
                if not check_validity(j):
                    valid = False
                    break
        if valid:
            print('graph')
            import sys
            sys.exit()

