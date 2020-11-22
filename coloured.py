import numpy as np
class Edge():
    def __init__(self,colour = 'u'):
        self.colour = colour
        self.not_colour = []
    def add_not_colour(self,index):
        self.not_colour.append(index)
    def change_colour(self,index):
        self.colour = index
    def __repr__(self):
        return self.colour
    def __eq__(self,obj):
        return obj == self.colour

def searchForbidden(indexOfColumn,indexOfRow):
    edge = graph[indexOfRow][indexOfColumn]
    row = graph[indexOfRow]
    for col in range(indexOfColumn):
        if row[col] != edge.colour:
            graph[indexOfColumn][col].add_not_colour(findTheRemainingOne(row[col],edge))
            graph[col][indexOfColumn].add_not_colour(findTheRemainingOne(row[col],edge))
def findTheRemainingOne(edgex,edgey):
    result = ['r','g','b']
    return str(result.remove(edgex.colour).remove(edgey.colour))
def firstu(row):
    for i in row:
        if i =='u':
            return i
##initialize graph
def addColour(row):
    result = ['r','g','b']
    for i in row:
        try:
            result.remove(i.colour)
        except ValueError:
            pass
        if result is []:
            return
    if result is not []:
        col = firstu(row)
        row[col].change_colour(str(result[0]))
        searchForbidden()

firstLine = [Edge(),Edge('r'),Edge('g'),Edge('b'),Edge()]
graph =[firstLine]+[[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]\

for i in range(len(graph)):
    graph[i][i] = 0

# print(graph)

while True:
    for i in range(len(graph)):
        # for j in
        # addColour()
        addColour(i)
        searchForbidden(i)
