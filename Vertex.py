class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.listaNas = []
        self.vertexDegree = 0
        self.inVal = 0
        self.outVal = 0
        self.visited = False

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

