from Vertex import *
from termcolor import colored


class Graph:
    def __init__(self, dataVar):
        self.dataVar = dataVar
        #0 == Lista następników
        #1 == macierz sąsiedztwa
        self.verticesList = {}
        self.verticesCount = 0
        self.verticesMatrix = []
        self.sorted = []
        self.counter = 0
        stack = []
        self.start = 0

    def addVertex(self, key):
        if key not in self.verticesList:
            self.verticesCount += 1
            newVertex = Vertex(key)
            self.verticesList[key] = newVertex
            return newVertex

    def getVertex(self, vert):
        if vert in self.verticesList:
            return self.verticesList[vert]
        else:
            print("Vertex not found")
            return None

    def __contains__(self, item):
        return item in self.verticesList

    def addEdge(self, vFrom, vTo, cost=0):
        if vFrom not in self.verticesList:
            newVert = self.addVertex(vFrom)
        if vTo not in self.verticesList:
            newVert = self.addVertex(vTo)
        if self.dataVar == 0:
            if self.getVertex(vTo) not in self.getVertex(vFrom).listaNas:
                self.getVertex(vFrom).listaNas.append(vTo)
                self.getVertex(vFrom).outVal += 1
                self.getVertex(vTo).inVal += 1
        if self.dataVar == 1:
            if self.verticesMatrix[vFrom-1][vTo-1] != 1:
                self.verticesMatrix[vFrom-1][vTo-1] = 1
                self.verticesMatrix[vTo-1][vFrom-1] = 1
                self.getVertex(vFrom).vertexDegree += 1
                self.getVertex(vTo).vertexDegree += 1

    def isEven(self):
        s = 0
        for v in self.verticesList:
            if self.getVertex(v).vertexDegree % 2 != 0:
                return False
        return True

    def isInOut(self):
        for v in self.verticesList:
            vert = self.getVertex(v)
            if vert.inVal != vert.outVal:
                return False
        return True

    def getVertices(self):
        return self.verticesList.keys()

    def __iter__(self):
        return iter(self.verticesList.values())

    def displayMatrix(self):
        if self.dataVar == 1:
            print(end='  ')
            for i in range(1, len(self.verticesList) + 1):
                print(colored(i, 'red'), end='  ')
            print()
            for i in range(1, len(self.verticesList) + 1):
                print(colored(i, 'red'), end=' ')
                for j in range(len(self.verticesMatrix[i - 1])):
                    if self.verticesMatrix[i - 1][j] == 1:
                        print(colored(self.verticesMatrix[i - 1][j], 'green'), end=', ')
                    else:
                        print(self.verticesMatrix[i - 1][j], end=', ')
                print()

    def visitVertex(self, v):
        for i in range(self.verticesCount):
            if self.verticesMatrix[v.id - 1][i] == 1:
                if self.getVertex(i + 1).getColor() == 'white':
                    self.getVertex(i + 1).setColor('gray')
                    #v.setColor('gray')
                    self.visitVertex(self.getVertex(i + 1))
                    if self.getVertex(i + 1).getColor() == 'gray':
                        self.getVertex(i + 1).setColor('black')
                        self.sorted.insert(0, self.getVertex(i + 1).id)
                    elif not self.getVertex(i + 1).beginNas:
                        self.getVertex(i + 1).setColor('black')
                        self.sorted.insert(0, self.getVertex(i + 1).id)


    def DFS_msasiedztwa(self):
        self.sorted = []
        for u in self.verticesList:
            if self.getVertex(u).getColor() == 'white':
                self.visitVertex(self.getVertex(u))
        self.sorted.insert(0, list(self.verticesList.keys())[0])
        print(self.sorted)


    def HamiltonMSAS_recurrent(self, v, stack):
        vert = self.getVertex(v)
        stack.append(v)
        vert.visited = True
        print(stack)
        if self.verticesMatrix[v-1][self.start-1] ==1:
            if len(stack) == self.verticesCount:
                stack.append(self.start)
                self.start = -1
                return stack
            else:
                #stack.remove(v)
                #vert.visited = False
                for i in range(self.verticesCount):
                    if self.verticesMatrix[v - 1][i] == 1:
                        if not self.getVertex(i+1).visited:
                            self.HamiltonMSAS_recurrent(i+1, stack)
        else:
            for i in self.verticesList:
                if self.verticesMatrix[v - 1][i - 1] == 1:
                    if not self.getVertex(i).visited:
                        self.HamiltonMSAS_recurrent(i, stack)

    def HamiltonMSAS(self, v, stack):
        for u in self.verticesList:
            if self.start != -1:
                for k in self.verticesList:
                    self.getVertex(k).visited = False
                print(u)
                stack = []
                self.start = u
                self.HamiltonMSAS_recurrent(u, stack)
            else:
                return stack

    def HamiltonLNAS_recurrent(self, v, stack):
        vert = self.getVertex(v)
        stack.append(v)
        vert.visited = True
        if self.start in vert.listaNas:
            if len(stack) == self.verticesCount:
                stack.append(self.start)
                self.start = -1
                return stack
            elif len(vert.listaNas) == 1:
                stack.remove(v)
                vert.visited = False
            else:
                for u in vert.listaNas:
                    if not self.getVertex(u).visited:
                        self.HamiltonLNAS_recurrent(u, stack)
        else:
            for u in vert.listaNas:
                if not self.getVertex(u).visited:
                    self.HamiltonLNAS_recurrent(u, stack)

    def HamiltonLNAS(self, v, stack):
        for u in self.verticesList:
            if self.start != -1:
                for k in self.verticesList:
                    self.getVertex(k).visited = False
                stack = []
                self.start = u
                self.HamiltonLNAS_recurrent(u, stack)
            else:
                return stack

    def EulerMSAS(self, v, stack):
        for u in range(self.verticesCount):
            if self.verticesMatrix[v.id - 1][u] == 1:
                print(u+1)
                self.verticesMatrix[v.id - 1][u] = 0
                self.verticesMatrix[u][v.id - 1] = 0
                self.EulerMSAS(self.getVertex(u+1), stack)
        stack.append(v.id)
        return stack

    def EulerLNAS(self, v, stack):
        vert = self.getVertex(v)
        lista = list(vert.listaNas)
        for u in range(len(lista)):
            vert.listaNas.remove(lista[u])
            self.EulerLNAS(lista[u], stack)
        stack.append(v)
        return stack

