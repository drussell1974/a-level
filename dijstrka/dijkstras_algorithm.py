class Vertex():
    def __init__(self, key):
        self.key = key
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
    
class Edge():

    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target


""" Use Python priority queue """
import heapq

def getShortestPath(vertices, startV, target):
    
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
                
    node = target
    shortestPath = []
    while node is not None:
        #print("%s > " % node, end="")
        shortestPath.append(node.key)
        node = node.previous
        
    return shortestPath

