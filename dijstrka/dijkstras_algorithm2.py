class Vertex():
    
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.min_distance_from_start = float("inf")
        self.previous = None
        self.edges = []
        
    def __cmp__(self, other):
        """ Override Compare (Used to prioritise the Vertex in the priority queue """
        return self.cmp(self.min_distance_from_start, other.min_distance_from_start)
    
    def __lt__(self, other):
        """ Override Less Than (Used to prioritise the Vertex in the priority queue """
        selfP = self.min_distance_from_start
        otherP = other.min_distance_from_start
        return selfP < otherP
    
    def __str__(self):
        """ string """
        return str(self.key)
    
class Edge():

    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target


""" Use Python priority queue """
import heapq

class Dijkstra():
    def calculate(self, vertices, startV):
        """ The priority queue """
        queue = []
        
        startV.min_distance_from_start = 0
        
        """ add the starting vertex to the priority queue """
        heapq.heappush(queue, startV)
        
        while len(queue) > 0:
            """return the smallest item from the heap"""
            currV = heapq.heappop(queue)
            
            for edge in currV.edges:
                u = edge.start
                v = edge.target
                distance = u.min_distance_from_start + edge.weight
                #print("checking if new distance", distance, "is less than", v.min_distance_from_start)
                if distance < v.min_distance_from_start:
                    v.previous = u;
                    v.min_distance_from_start = distance
                    """ add to the priority queue """
                    heapq.heappush(queue, v)
                    
    def shortestPathTo(self, target):
        print("Shortest path is")
        node = target
        
        while node is not None:
            print("%s --> " % node)
            node = node.previous



nodeB = Vertex("B")
nodeC = Vertex("C")
nodeG = Vertex("G")
nodeI = Vertex("I")
nodeS = Vertex("S")
nodeT = Vertex("T")

edgeBG = Edge(17, nodeB, nodeG)
edgeBS = Edge(14, nodeB, nodeS)
edgeTG = Edge(13, nodeT, nodeG)
edgeTC = Edge(9, nodeT, nodeC)
edgeGC = Edge(9, nodeG, nodeC)
edgeCG = Edge(9, nodeC, nodeG)
edgeGB = Edge(17, nodeG, nodeB)
edgeGS = Edge(9, nodeG, nodeS)
edgeCS = Edge(14, nodeC, nodeS)
edgeCI = Edge(15, nodeC, nodeI)
edgeBS = Edge(14, nodeB, nodeS)
edgeIS = Edge(15, nodeI, nodeS)

nodeB.edges.append(edgeBG)
nodeB.edges.append(edgeBS)
nodeT.edges.append(edgeTG)
nodeT.edges.append(edgeTC)
nodeG.edges.append(edgeGC)
nodeG.edges.append(edgeGS)
nodeC.edges.append(edgeCG)
nodeC.edges.append(edgeCS)
nodeC.edges.append(edgeCI)
nodeI.edges.append(edgeIS)

vertices = {nodeB, nodeC, nodeG, nodeI, nodeS, nodeT}


dijk = Dijkstra()
dijk.calculate(vertices, nodeT)
dijk.shortestPathTo(nodeS)
