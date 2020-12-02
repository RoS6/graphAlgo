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
def checkFailedCombination(rowx,rowy,combination):
    failedCombination = combination.copy()
    for i in range(num):
        if rowx[i] == 0 or rowy[i]==0:
            continue
        elif [rowx[i].colour,rowy[i].colour] in failedCombination:
            failedCombination.remove([rowx[i].colour,rowy[i].colour])
    return failedCombination

def searchForbidden(indexOfRow,indexOfColumn):
    edge = graph[indexOfRow][indexOfColumn]
    row = graph[indexOfRow]
    for col in range(num):
        if row[col] == 0 or row[col].colour =='n':
            continue
        elif row[col].colour != edge.colour and row[col].colour != 'u':
            graph[indexOfColumn][col].addNotColour(findTheRemainingOne(row[col],edge))
            graph[col][indexOfColumn].addNotColour(findTheRemainingOne(row[col],edge))
def findTheRemainingOne(edgex,edgey):
    result = ['r','g','b']
    result.remove(edgex.colour)
    result.remove(edgey.colour)
    return result


def checkValidity(indexX,indexY):
    global graph,num
    rowx = graph[indexX]
    rowy = graph[indexY]
    fail = []
    combinations = []
    if rowx[indexY].colour == 'n':
        combinations = notconnected
    # combinations = (notconnected if (rowx[indexY].colour == 'u' and rowy[indexX].colour=='u') else connected)
    # fail = checkFailedCombination(rowx,rowy,combinations)
    elif rowx[indexY].colour == 'u':
        if len(rowx[indexY].not_colour) ==3:
            rowx[indexY].colour = 'n'
            rowy[indexX].colour = 'n'
            combinations = notconnected
        else:
            for i in ['r', 'g', 'b']:
                if i not in rowx[indexY].not_colour:
                    rowx[indexY].colour = i
                    rowy[indexX].colour = i
                    combinations = connected[i]
                    searchForbidden(indexX,indexY)
                    searchForbidden(indexY,indexX)
    else:
        combinations = connected[rowx[indexY]]
    fail = checkFailedCombination(rowx, rowy, combinations)
    if combinations == []:
        import sys
        sys.exit()
    for combi in fail:
        for col in range(num):
            # if rowx[col].colour == combi[0] and rowy[col].colour == 'u' and rowy[col].not_colour != combi[1]:
            if rowx[col] == 0 or rowx[col].colour == 'n':
                continue
            if rowx[col].colour == combi[0] and rowy[col].colour == 'u' and combi[1] not in rowy[col].not_colour:
                rowy[col].colour = combi[1]
                graph[col][indexY].colour = combi[1]
                searchForbidden(indexY,col)
                searchForbidden(col,indexY)
                fail.remove(combi)
            elif rowy[col].colour == combi[1] and rowx[col].colour == 'u' and combi[0] not in rowx[col].not_colour:
                rowx[col].colour = combi[0]
                graph[col][indexX].colour = combi[0]
                searchForbidden(indexX,col)
                searchForbidden(col,indexX)
                fail.remove(combi)
            elif rowx[col].colour == 'u' and rowy[col].colour == 'u' and (combi[0] not in rowx[col].not_colour) and (combi[1] not in rowy[col].not_colour):
                rowx[col].colour = combi[0]
                rowy[col].colour = combi[1]
                graph[col][indexY].colour = combi[1]
                graph[col][indexX].colour = combi[0]
                searchForbidden(indexX,col)
                searchForbidden(indexY,col)
                searchForbidden(col,indexX)
                searchForbidden(col,indexY)

    if fail == []:
        return
    else:
        num = num + 1
        new_row = []
        for i in graph:
            # print(i)
            # print(num)
            i.append(Edge())
            new_row.append(Edge())
        new_row.append(Edge())
        graph.append(new_row)
        checkValidity(indexX,indexY)
        print(num)


firstLine = [Edge(),Edge('n'),Edge('r'),Edge(),Edge()]
graph =[firstLine]+[[Edge('n'),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]

num = 5
for i in range(len(graph)):
    graph[i][i] = 0

connected = {'r':[['r','r'],['r','g'],['r','b'],['b','r'],['b','b'],['g','r'],['g','g']],
             'b':[['b','b'],['b','g'],['b','r'],['r','r'],['r','b'],['g','b'],['g','g']],
             'g':[['g','g'],['g','b'],['g','r'],['r','r'],['r','g'],['b','g'],['b','b']]
             }
notconnected = [['r','r'],['r','g'],['r','b'],
                ['g','r'],['g','g'],['g','b'],
                ['b','r'],['b','g'],['b','b']]
# print(graph)
i = 0

while True:
    while i < num:
        j = i+1
        while j<num:
            checkValidity(i,j)

