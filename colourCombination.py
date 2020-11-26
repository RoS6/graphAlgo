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
        if [rowx[i],rowy[i]] in failedCombination:
            failedCombination.remove([rowx[i],rowy[i]])
    return failedCombination

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


def checkValidity(indexX,indexY):
    rowx = graph[indexX]
    rowy = graph[indexY]
    if rowx[indexY].colour == 'u' and rowy[indexX].colour=='u':
        combinations = notconnected
        fail = checkFailedCombination(rowx,rowy,combinations)
        for combi in fail:
            for col in range(num):
                if rowx[col].colour == combi[0] and rowy[col].colour == 'u' and rowy[col].not_colour != combi[1]:
                    rowy[col].colour = combi[1]
                    searchForbidden(indexX,col)



firstLine = [Edge(),Edge('n'),Edge('r'),Edge(),Edge()]
graph =[firstLine]+[[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
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
