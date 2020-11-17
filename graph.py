import numpy as np
from itertools import combinations
# class node:
#     def __init__(self,index,numberOfNode):
#         self.index = index
#         self.array = np.zeros(numberOfNode)
#
#     def __array__(self):
#         return self.array
#
# class graph:
#     def __init__(self):
#         self.matrix =np.zeros()
# num = 8
# graph = np.array()
# for i in range(num):
#     graph = np.append(graph,node(i,num))

# num = 8
# graph = np.zeros(num*num)
# graph = graph.reshape(num,num)
# print(graph)
# marked = []
# graph[0][1:5] = np.array([1,1,1,-1,-1])

# def check_validity(index):
#     pair11,pair1_1,pair_11,pair_1_1=False
#     array = graph[index]
#     for i in graph:
#         for j in range(num):
#             if i[num]==1 and array[num]==1:
#                 pair11 = True
#             if i[num] ==1 and array[num] ==-1:
#                 pair1_1 = True
#             if i[num] ==-1 and array[num] ==1:
#                 pair_11 = True
#             if i[num] ==-1 and array[num]==-1:
#                 pair_1_1 = True
#         # if not pair11:
#         #         change(index,i,'11')
#         # if not pair1_1:
#         #         change(index,i,j,'1-1')
#         # if not pair_11:
#         #         change(index,i,j,'-11')
#         # if not pair_1_1:
#         #         change(index, i, j, '-1-1')\
#         if not (pair11 and pair1_1 and pair_11 and pair_1_1):
#             failed_condition = [i[1] for index,i in enumerate([(pair11,'11') , pair1_1 , pair_11 , pair_1_1]) if index ]
#
#             change(index,i,failed_condition)
#change y to fit x
def check_validity(tuple):
    pair11,pair1_1,pair_11,pair_1_1=False,False,False,False
    index = tuple[1]
    array = graph[index]#y
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
        # if not pair11:
        #         change(index,i,'11')
        # if not pair1_1:
        #         change(index,i,j,'1-1')
        # if not pair_11:
        #         change(index,i,j,'-11')
        # if not pair_1_1:
        #         change(index, i, j, '-1-1')\
    if not (pair11 and pair1_1 and pair_11 and pair_1_1):
        failed_condition = [v for (i,v) in [(pair11,'11') , (pair1_1,'1-1') , (pair_11,'-11') , (pair_1_1,'-1-1')] if not i ]
        # print(failed_condition)
        if not change(index,row,failed_condition):
           return False
        else:
            return True
    return True
pair = {
    '11':(1,1),
    '1-1':(1,-1),
    '-11':(-1,1),
    '-1-1':(-1,-1)
}
def firstEmpty(row,array):
    for i in range(len(row)):
        if row[i] == 0 and array[i] == 0:
            return i
    return -1
def corresponding0(row,array,num):
    for i in range(len(row)):
        if row[i] == num and array[i] ==0:
            return i
    return -1
    # for i in range(len(row)):
    #     if row[i] == 0 and array[i] == 0:
    #         return i
    # return -1
def zero_in_row(row,array,num):
    if firstEmpty(row,array) == -1:
        for i in range(len(row)):
            if row[i] == 0 and array[i]==num:
                return i
    return -1
def checkDuplication(row,array,num,num2):#num is the row's value, 1 or -1, to decide which 2 condition need to becheck
    # newarr = np.concatenate((row, array)).transpose()
    result = []
    # situation flip array
    for i in range(len(row)):
        if row[i] == num and array[i] == num2:
            result.append(i)
    #situation flip row

    if len(result)>1:
        return result
    else:
        return -1


def change(index,row,failed_condition):
    # row = graph[i]
    array = graph[index]
    for condition in failed_condition:

        situation1 = corresponding0(row,array,pair[condition][0])
        situation2 = zero_in_row(row,array,pair[condition][1])
        situation3 = firstEmpty(row,array)
        # situation5 = s5(row,array)
        situation4 = checkDuplication(row,array,pair[condition][0],pair[condition][1]*-1)
        if situation1>-1:
            array[situation1] = pair[condition][1]
        elif situation2>-1:
            row[situation2] = pair[condition][0]
        elif situation3>-1:
            row[situation3] = pair[condition][0]
            array[situation3] = pair[condition][1]
        elif situation4 != -1:
            for i in situation4:
                if [index,i] not in marked:
                    marked.append([index,i])
                    array[i] = array[i]*-1
                    for j in checking:
                        if index in j:
                            if check_validity(j):
                                pass
                            else:
                                return False
                        return True
                # else:
                #     return False
            return False
        else:
            return False
    return True





# def change(index,i,j,type):
#     array = graph[index]
#     if array[j]==0:
#         array[j] = pair[type][1]
#         return
#     elif [index,j] not in marked:
#         array[j] = -1*array[j]
#         marked.append([index,j])
#         check_validity(index)
#     elif [index,j] in marked:
        #find the one that has duplicate ture condition ,filp the number

    # else:
    #     if j+1 != index:
    #         array[j+1] = -1

# num = 9
# graph = np.zeros(num*num)
# graph = graph.reshape(num,num)
# print(graph)
# marked = []
# # graph[0][1:5] = np.array([1,1,1,-1,-1])
# graph[0] = np.array([0,0,1,1,-1,-1,0,0,0])
# np.fill_diagonal(graph,100)
# checking = []
# for i in list(combinations([0,1,2,3,4,5,6,7,8],2)):
#     checking.append(i)
#     marked = []
#     if not check_validity(i):
#         print('fail')
#         break
#     print(graph)
#     print(i)
num = 6
while True:

    combinationList = [i for i in range(num)]
    graph = np.zeros(num*num)
    graph = graph.reshape(num,num)
    marked = []
    # graph[0] = np.array([0,0,1,1,-1,-1]+[])
    firstLine = [0,0,1,1,-1,-1]
    for i in range(num-6):
        firstLine.append(0)
    graph[0] = np.array(firstLine)
    np.fill_diagonal(graph,100)
    checking = []
    success = True
    for i in list(combinations(combinationList,2)):
        checking.append(i)
        marked = []
        if not check_validity(i):
            print('n = '+str(num)+' fail')
            # print('fail')
            success = False
            break
        # print(graph)
        # print(i)
    if success == False:
        num = num+1
    else:
        print(graph)
        print('success at n='+str(num))
        break


    # print(graph)
    # break
