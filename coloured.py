import numpy as np
class Edge():
    def __init__(self,colour = 'u'):
        self.colour = colour
        self.not_colour = []
    def addNotColour(self,colour):
        for i in colour:
            if colour not in self.not_colour:
                self.not_colour.append(i)
    # def changeColour(self,index):
    #     self.colour = index
    def __repr__(self):
        return self.colour
    # def __eq__(self,obj):
    #     return obj == self.colour

def searchForbidden(indexOfRow,indexOfColumn):
    edge = graph[indexOfRow][indexOfColumn]
    row = graph[indexOfRow]
    for col in range(num):
        if row[col] ==0:
            continue
        elif row[col].colour != edge.colour and row[col].colour != 'u':
            graph[indexOfColumn][col].addNotColour(findTheRemainingOne(row[col],edge))
            graph[col][indexOfColumn].addNotColour(findTheRemainingOne(row[col],edge))
def findTheRemainingOne(edgex,edgey):
    result = ['r','g','b']
    result.remove(edgex.colour)
    result.remove(edgey.colour)
    return result
# def firstu(row):
#     for i in row:
#         if i.colour =='u':
#             return i
##initialize graph
def requiredColour(row):
    result = ['r','g','b']
    for i in row:
        try:
            result.remove(i.colour)
        except:
            pass
    return result

def addColour(row_index):
    global num, graph
    row = graph[row_index]
    required_colour = requiredColour(row)
    if required_colour == []:
        return
    for colour in required_colour.copy():
        for j in range(row_index,num):
            if row[j] ==0:
                continue
            elif row[j].colour != 'u':
                continue
            if colour not in row[j].not_colour:
                # ind_first_u = firstu(row)
                row[j].colour = colour
                graph[j][row_index].colour = colour
                searchForbidden(row_index,j)
                searchForbidden(j,row_index)
                required_colour.remove(colour)
                break

    if required_colour == []:
        # print(graph)
        return
    else:
        num = num + 1
        new_row = []
        for i in graph:
            # print(i)
            # print(num)
            i.append(Edge())
            new_row.append(Edge())
        new_row.append(0)
        graph.append(new_row)
        addColour(row_index)
        print(num)
        # print(graph)
        # graph[row_index][num] = Edge(required_colour[0])
        # searchForbidden(row_index,num)
        # graph[num][row_index] = Edge(required_colour[0])
        # searchForbidden(num,row_index)
        # required_colour.remove(required_colour[0])
        # if required_colour != []:
        #     add
firstLine = [Edge(),Edge('r'),Edge(),Edge(),Edge()]
graph =[firstLine]+[[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]

num = 5
for i in range(len(graph)):
    graph[i][i] = 0

# print(graph)
i = 0
while True:
        # for j in
        # addColour()
    # copy= num
    # for i in range(200):
    if i<num:
        addColour(i)
            # print(graph)
        i+=1
    if i == num:
        print(graph)
        import sys
        sys.exit()
            # break
    # if i<num:
    #     break

    # if num == copy:
    #     break
        # searchForbidden(i)