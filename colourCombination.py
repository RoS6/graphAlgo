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

firstLine = [Edge(),Edge('n'),Edge('r'),Edge(),Edge()]
graph =[firstLine]+[[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]+\
       [[Edge(),Edge(),Edge(),Edge(),Edge()]]

num = 5
for i in range(len(graph)):
    graph[i][i] = 0

connected = {'r':[['r','r'],['r','g'],['r','b'],['b','r'],['b','b'],['g','r'],['g','g']],
             'b':[['b','b'],['b','g'],['b','r'],['r','r'],['r','b'],['']]
             }

# print(graph)
i = 0
while True